# pylint: skip-file
# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and SoyMilkWhisky
"""
...
"""
import os
import sys
from typing import List, Tuple


def load_pkg():
    """
    ...
    """
    addon_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.join(addon_dir, 'plib'))


load_pkg()

import librosa
import numpy as np


# 加载音频文件
def load_audio(file_path):
    """
    ...
    """
    y, sr = librosa.load(file_path, sr=16000)  # 加载音频（采样率 16kHz）
    return y, sr


def extract_formants_with_denoise(y, sr, frame_length=512, hop_length=256,
                                  # pylint: disable=too-many-arguments,too-many-positional-arguments
                                  db_threshold=-20,
                                  rms_threshold=0.01):
    """
    ...
    """
    frames = librosa.util.frame(y, frame_length=frame_length, hop_length=hop_length)
    formants = []
    timestamps = []
    for i, frame in enumerate(frames.T):
        # 计算帧的分贝值
        frame_db = 10 * np.log10(np.mean(frame ** 2) + 1e-10)  # 防止log(0)
        frame_rms = np.sqrt(np.mean(frame ** 2))  # 计算帧的 RMS 值

        # 如果分贝或 RMS 低于阈值，标记为静音
        if frame_db < db_threshold or frame_rms < rms_threshold:
            formants.append((None, None))  # 静音帧，不提取共振峰
            timestamps.append((i * hop_length) / sr)
            continue

        # 计算频谱
        spectrum = np.abs(np.fft.rfft(frame)) ** 2
        freqs = np.fft.rfftfreq(len(frame), 1 / sr)

        # 找到共振峰（简化版）
        peaks = np.argsort(-spectrum)[:2]  # 找到两个最大峰
        f1, f2 = freqs[peaks[0]], freqs[peaks[1]]
        formants.append((f1, f2))

        # 计算时间戳
        timestamp = (i * hop_length) / sr  # 帧的起始时间
        timestamps.append(timestamp)

    return formants, timestamps


# 判断元音类型
def classify_vowel(formants):
    vowels = []
    for f1, f2 in formants:
        # 如果无法提取共振峰，标记为静音
        if f1 is None and f2 is None:
            vowels.append('silence')
            continue

        # 元音分类规则
        if f1 > 700 and 1000 <= f2 <= 1200:
            vowels.append('a')
        elif 500 <= f1 <= 700 and f2 > 1700:
            vowels.append('e')
        elif f1 < 400 and f2 > 2000:
            vowels.append('i')
        elif 400 <= f1 <= 600 and 800 <= f2 <= 1000:
            vowels.append('o')
        elif f1 < 400 and f2 < 1000:
            vowels.append('u')
        else:
            vowels.append('a')  # 未知音素，默认标记为 "unknown"
    return vowels


def rosa(audio_path, db_threshold=-50, rms_threshold=0.01):
    y, sr = load_audio(audio_path)
    formants, timestamps = extract_formants_with_denoise(y, sr, db_threshold=db_threshold,
                                                         rms_threshold=rms_threshold)

    # 分类元音
    vowels = classify_vowel(formants)

    # 将元音和时间戳结合
    vowel_sequence_with_timestamps = [
        {"vowel": vowel, "timestamp": timestamp}
        for vowel, timestamp in zip(vowels, timestamps)
    ]
    # import pprint
    # pprint.pprint(vowel_sequence_with_timestamps)
    vowels = process_vowel_sequence(vowel_sequence_with_timestamps)
    res = replace_vowels(vowels)
    # for item in res:
    #     print(item)

    return res


def process_vowel_sequence(vowel_sequence_with_timestamps: List[dict]) -> (
        List)[Tuple[float, float, str]]:
    """
    ...
    """
    filtered_vowels = [item for item in vowel_sequence_with_timestamps if
                       item["vowel"] != "silence"]

    grouped_vowels = []
    if not filtered_vowels:
        return grouped_vowels

    start_time = filtered_vowels[0]["timestamp"]
    current_vowel = filtered_vowels[0]["vowel"]

    for i in range(1, len(filtered_vowels)):
        current_item = filtered_vowels[i]
        if current_item["vowel"] != current_vowel:
            # Save the current vowel group
            grouped_vowels.append((start_time, filtered_vowels[i - 1]["timestamp"], current_vowel))
            # Start a new group
            start_time = current_item["timestamp"]
            current_vowel = current_item["vowel"]

    # Append the last group
    grouped_vowels.append((start_time, filtered_vowels[-1]["timestamp"], current_vowel))

    adjusted_vowels = []
    for start, end, vowel in grouped_vowels:
        duration = end - start
        if duration < 0.01:  # Treat as a single frame
            adjusted_start = max(0, start - 0.25)
            adjusted_end = end + 0.25
            adjusted_vowels.append((adjusted_start, adjusted_end, vowel))
        else:
            adjusted_vowels.append((start, end, vowel))

    final_vowels = []
    for start, end, vowel in adjusted_vowels:
        duration = end - start
        if duration <= 0.5:
            # Extend duration to 0.5s, split evenly around the original segment
            center = (start + end) / 2
            new_start = center - 0.25
            new_end = center + 0.25
            final_vowels.append((new_start, new_end, vowel))
        else:
            # Split the duration into chunks of approximately 0.5s, avoiding overlaps
            num_chunks = int(duration / 0.5)
            remainder = duration % 0.5
            chunk_duration = 0.5 + (remainder / num_chunks) if num_chunks > 0 else 0.5

            current_start = start
            for _ in range(num_chunks):
                current_end = current_start + chunk_duration
                final_vowels.append((current_start, current_end, vowel))
                current_start = current_end

            # Add any remaining duration as the last chunk
            if current_start < end:
                final_vowels.append((current_start, end, vowel))

    # Ensure no overlapping chunks for the same vowel
    non_overlapping_vowels = []
    for i, (start, end, vowel) in enumerate(final_vowels):
        if i > 0 and vowel == final_vowels[i - 1][2]:
            # Ensure the current segment starts after the previous one
            prev_end = non_overlapping_vowels[-1][1]
            if start < prev_end:
                start = prev_end
            end = max(end, start)  # Ensure end > start
        non_overlapping_vowels.append((start, end, vowel))

    return non_overlapping_vowels


# # Output Result
# for item in result:
#     print(item)

def replace_vowels(vowel_sequences: List[Tuple[float, float, str]]) -> (
        List)[Tuple[float, float, str]]:
    """
    ...
    """
    replacement_map = {
        "a": "AA",
        "e": "EH",
        "o": "AO",
        "i": "IY",
        "u": "UW"
    }

    replaced_sequences = [
        (start, end, replacement_map.get(vowel, vowel))  # 如果元音存在于替换表中，替换；否则保持原样
        for start, end, vowel in vowel_sequences
    ]

    return replaced_sequences

# rosa("F:\\OBS_Video\\test_whiskyai_xyz_16000.wav",-50,0.01)

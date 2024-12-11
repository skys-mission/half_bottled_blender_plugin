# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and SoyMilkWhisky
"""
音素处理代码
"""

import json
import os
from typing import List, Tuple, Dict


class Phoneme:
    """
    ...
    """
    cmu_dict = {}

    @staticmethod
    def load_cmu_dict(file_path: str) -> Dict[str, List[str]]:
        """
        加载 CMU 字典到内存中。
        :param file_path: CMU 字典文件路径
        :return: 一个字典，键是单词，值是音素列表
        """
        cmu_dict = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # 跳过注释行
                if line.startswith(";;;"):
                    continue
                # CMU 字典格式：WORD  PH1 PH2 PH3 ...
                parts = line.strip().split("  ")
                if len(parts) < 2:
                    continue
                word = parts[0].lower()  # 将单词转为小写
                phonemes = parts[1].split()  # 音素列表
                cmu_dict[word] = phonemes
        return cmu_dict

    @staticmethod
    def align_phonemes_to_timestamps(word_data: Dict, cmu_dict: Dict[str, List[str]]) \
            -> List[Tuple[float, float, str]]:
        """
        将单词的时间戳和音素对齐。
        :param word_data: 包含单词的时间戳数据
        :param cmu_dict: CMU 字典
        :return: 包含时间戳和音素的列表
        """
        aligned_data = []
        if word_data and "result" in word_data and word_data["result"]:
            for word_info in word_data["result"]:
                word = word_info["word"].lower()  # 单词小写化匹配 CMU 字典
                start_time = word_info["start"]
                end_time = word_info["end"]

                if word in cmu_dict:
                    phonemes = cmu_dict[word]
                else:
                    phonemes = ["AA"]  # 如果单词不在字典中，标记为 AA TODO

                # 平均分配时间戳给每个音素
                num_phonemes = len(phonemes)
                time_step = (end_time - start_time) / num_phonemes
                for i, phoneme in enumerate(phonemes):
                    phoneme_start = start_time + i * time_step
                    phoneme_end = phoneme_start + time_step
                    aligned_data.append((phoneme_start, phoneme_end, phoneme))
        return aligned_data

    @staticmethod
    def process_data(input_data: List[Dict], cmu_dict: Dict[str, List[str]]) -> \
            List[Tuple[float, float, str]]:
        """
        处理整个输入数据集，将单词转为音素并对齐时间戳。
        :param input_data: 输入的单词和时间戳数据
        :param cmu_dict: CMU 字典
        :return: 包含时间戳和音素的完整列表
        """
        all_aligned_data = []
        for word_data in input_data:
            aligned_data = Phoneme.align_phonemes_to_timestamps(word_data, cmu_dict)
            all_aligned_data.extend(aligned_data)
        return all_aligned_data

    @staticmethod
    def gen(json_path):
        """
        从指定的 JSON 文件生成对齐的音素序列。

        此函数首先读取 JSON 文件内容，然后处理这些数据以生成对齐的音素序列。

        参数:
        json_path (str): JSON 文件的路径。

        返回:
        list: 处理后的对齐音素序列。
        """
        # 打开 JSON 文件并加载内容
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # 使用 json.load() 解析 JSON 文件内容

        # 处理数据
        aligned_phonemes = Phoneme.process_data(data, Phoneme.cmu_dict)

        return aligned_phonemes


script_dir = os.path.dirname(os.path.abspath(__file__))
ffmpeg_path = os.path.join(script_dir, "lib", "cmudict-0.7b")

# 加载 CMU 字典
Phoneme.cmu_dict = Phoneme.load_cmu_dict(ffmpeg_path)

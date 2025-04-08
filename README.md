# whisky_helper_for_blender

[![Pylint](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/pylint.yml)
[![CodeQL Advanced](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/codeql.yml)
[![Bandit](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/bandit.yml/badge.svg)](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/bandit.yml)

Other languages: [简体中文](README_zh.md), (Currently unable to translate more)

A Blender add-on that uses the Vosk model to recognize lip-sync movements and generate keyframes, random blinking, and some other small features I commonly use.

You can download the latest version from the Github Releases page. Supports Windows-x64 and macOS-arm64.

<!-- TOC -->
* [whisky_helper_for_blender](#whisky_helper_for_blender)
  * [Download](#download)
  * [Features](#features)
    * [MMD Lip-Sync Generation](#mmd-lip-sync-generation)
      * [Usage](#usage)
      * [Parameter Description](#parameter-description)
      * [How to Adapt to Other Models](#how-to-adapt-to-other-models)
    * [Random Blinking](#random-blinking)
    * [Other Features](#other-features)
  * [Support](#support)
    * [Blender Version Compatibility](#blender-version-compatibility)
    * [Operating System Compatibility](#operating-system-compatibility)
  * [How to Install the Add-on in Newer Blender Versions](#how-to-install-the-add-on-in-newer-blender-versions)
  * [About Developing This Add-on](#about-developing-this-add-on)
    * [Notes](#notes)
  * [Open-Source References](#open-source-references)
<!-- TOC -->

## Download

https://github.com/skys-mission/whisky_helper_for_blender/releases

## Features

### MMD Lip-Sync Generation

Uses the Vosk audio model to recognize phonemes and apply them to MMD-standard models.

The add-on recognizes the following MMD model morph keys: あ (A), い (I), う (U), え (E), お (O), ん (N). If any of these except あ are missing, they will be mapped to あ. If あ is missing, an error will occur.

Warning: This feature will overwrite any existing keyframes for the あ, い, う, え, お, ん morph keys within the audio's time range.

#### Usage

![lips_gen2.0f.webp](.img/lips_gen2.0f.webp)

1. Select an audio file in "Audio Path" (most common audio formats, including MP4, should work).
2. Select any parent layer of an MMD model (note: if the object contains multiple meshes with these morph keys, all will be modified).
3. It is recommended to open the system console to monitor progress (Blender menu bar -> Windows -> Toggle System Console). macOS Blender does not have this feature.
4. Set the parameters and click "Generate" (note: the current version will generate readable cache files in the same directory as the audio file and will not delete them).
5. Wait until the mouse cursor changes back from a number to normal.

#### Parameter Description

![lips3.0.webp](.img/lips3.0.webp)

- **Start Frame**: The frame from which the audio will start.
- **DB Threshold**: Noise reduction based on decibels. Increase if recognition is inaccurate, decrease if recognition fails.
- **RMS Threshold**: Noise reduction based on RMS. Increase if recognition is inaccurate, decrease if recognition fails.
- **Delayed Opening**: The delay ratio for mouth opening.
- **Speed Up Opening**: Adjusts the curve speed from recognition start to delayed mouth opening.
- **Max Morph Value**: The maximum threshold for morph key values.

#### How to Adapt to Other Models

For example, for VRM models, you need to locate or create A, E, I, O, U, N morph keys and rename them to MMD standard morph key names.

**At least あ (A) is required to use this feature.**

- あ = A  
- い = I  
- う = U  
- え = E  
- お = O  
- ん = N  

If you don't know how to copy morph keys, refer to: [copy_shape_key.md](docs/copy_shape_key.md)

![lip_sync.webp](.img/lip_sync.webp)  
Model source: KissshotSusu

### Random Blinking

Random blinking recognizes the まばたき (blink) morph key. If it doesn't exist, you need to create or convert it yourself.

Warning: This feature will overwrite any existing keyframes for the まばたき morph key within the specified frame range.

1. Select any parent layer of an MMD model (note: if the object contains multiple meshes with this morph key, all will be modified).
2. It is recommended to open the system console to monitor progress (Blender menu bar -> Windows -> Toggle System Console).
3. Set the parameters and click "Generate."
4. Wait until the mouse cursor changes back from a number to normal.

![blink_args.webp](.img/blink_args.webp)

- **Blink Interval**: The time between blinks, in seconds.
- **Blinking Wave Ratio**: Random ratio adjustment (0.01–1).

### Other Features

Documentation in progress...

## Support

### Blender Version Compatibility

- **Primary supported versions** (tested by the developer):  
  - 3.6, 4.2  
- **May work on**:  
  - Blender ≥ 3.6  
- **Planned support**:  
  - Next Blender LTS version  
- **No plans to support**:  
  - Blender < 3.6  

### Operating System Compatibility

- **Currently supported**:  
  - Windows-x64  
  - macOS-arm64  
- **No plans to support**:  
  - Linux (unless significant changes occur)  

## How to Install the Add-on in Newer Blender Versions

Reference: https://docs.blender.org/manual/en/4.2/editors/preferences/addons.html#prefs-extensions-install-legacy-addon

## About Developing This Add-on

### Notes

- Blender 3.6–4.4 may require the `numba` library (version ≤ 0.60.0). Other Blender versions are untested.

## Open-Source References

| Project                     | Link                                               | License                                  |
|----------------------------|--------------------------------------------------|----------------------------------------|
| FFmpeg                     | https://github.com/FFmpeg/FFmpeg                 | GPLv3 (embedded tools in Releases)      |
| ~~Vosk-API & Vosk AI Model~~ | ~~https://github.com/alphacep/vosk-api~~         | Apache-2.0                             |
| ~~CMU Dict~~               | ~~http://www.speech.cs.cmu.edu/cgi-bin/cmudict~~ | 2-Clause BSD License                   |
| ~~gout-vosk tool~~         | ~~https://github.com/skys-mission/gout~~         | GPLv3                                  |
# whisky_helper_for_blender

[![Pylint](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/pylint.yml)
[![CodeQL Advanced](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/skys-mission/whisky_helper_for_blender/actions/workflows/codeql.yml)

Other languages: [简体中文](README_zh.md), (Currently unable to translate more)

A Blender addon that generates keyframes for lip-syncing using Vosk speech recognition models, adds random blinking animations, and includes some personal utility features.

Download the latest version from the Github Releases page. Due to embedded dependencies, currently only supports Windows.

<!-- TOC -->
* [whisky_helper_for_blender](#whisky_helper_for_blender)
  * [Download](#download)
  * [Features](#features)
    * [MMD Lip-Sync Generation](#mmd-lip-sync-generation)
      * [Usage](#usage)
      * [Parameters](#parameters)
      * [Adapting to Other Models](#adapting-to-other-models)
    * [Random Blinking](#random-blinking)
    * [Other Features](#other-features)
  * [Compatibility](#compatibility)
    * [Blender Version Support](#blender-version-support)
    * [OS Support](#os-support)
  * [Installing Addon in New Blender Versions](#installing-addon-in-new-blender-versions)
  * [Open Source Credits](#open-source-credits)
<!-- TOC -->

## Download

https://github.com/skys-mission/whisky_helper_for_blender/releases

## Features

### MMD Lip-Sync Generation

Generates phoneme-based lip animations using Vosk speech recognition models for MMD-standard models.

The addon recognizes MMD model shape keys named: あ (A), い (I), う (U), え (E), お (O). If other vowels are missing, they default to あ. Requires at least あ shape key to function.

Warning: This feature will destroy the あ, い, う, え, お form keyframes within the audio time range.

#### Usage

![lips_gen2.0f.webp](.img/lips_gen2.0f.webp)

1. Select an audio file in "Audio Path" (supports common formats including MP4).
2. Select the parent object of an MMD model (affects all mesh objects with shape keys under hierarchy).
3. Recommended: Enable System Console (Blender Menu > Window > Toggle System Console).
4. Configure parameters and click "Generate" (cache files may be created near the audio file).
5. Wait until cursor returns to normal.

#### Parameters

![lips3.0.webp](.img/lips3.0.webp)

- **Start Frame**: Audio start frame offset.
- **DB Threshold**: Noise reduction using decibel threshold (increase if over-detected, decrease if under-detected).
- **RMS Threshold**: Noise reduction using RMS threshold (adjust similar to DB).
- **Delayed Opening**: Mouth-opening delay ratio.
- **Speed Up Opening**: Curve speed adjustment for delayed opening.
- **Max Morph Value**: Maximum shape key value.

#### Adapting to Other Models

For models like VRM, create/rename shape keys to MMD standards:  
**At minimum, あ (A) shape key is required.**

- あ = A
- い = I
- う = U
- え = E
- お = O

For shape key copying guidance: [copy_shape_key.md](docs/copy_shape_key.md)

![lip_sync.webp](.img/lip_sync.webp)  
Model Source: KissshotSusu

### Random Blinking

Generates random blinking animations using the まばたき (Blink) shape key. Create this shape key if missing.

Warning: This feature will destroy the keyframes of まばたき shape keys within the frame range.

1. Select the parent object of an MMD model.
2. Configure parameters and click "Generate".
3. Wait until cursor returns to normal.

![blink_args.webp](.img/blink_args.webp)

- **Blink Interval**: Blink frequency in seconds.
- **Blinking Wave Ratio**: Randomization ratio (0.01-1).

### Other Features

Documentation in progress...

## Compatibility

### Blender Version Support

- **Primary Support**
  - 3.6, 4.2 (LTS versions)
- **Potential Compatibility**
  - ≥3.6
- **Future Support**
  - Next Blender LTS
- **Unsupported**
  - <3.6 and non-LTS versions

### OS Support

- **Current Support**
  - Windows x64
- **Temporarily Unsupported**
  - macOS ARM64 (low priority)
- **No Planned Support**
  - Linux (unless critical demand)

## Installing Addon in New Blender Versions

Reference: https://docs.blender.org/manual/en/latest/editors/preferences/addons.html#prefs-extensions-install-legacy-addon

## Open Source Credits

| Project                     | Link                                           | License                                 |
|-----------------------------|------------------------------------------------|----------------------------------------|
| FFmpeg                      | https://github.com/FFmpeg/FFmpeg               | GPLv3 (embedded tools)                 |
| ~~Vosk-API & Models~~       | ~~https://github.com/alphacep/vosk-api~~       | Apache-2.0                             |
| CMU Dict                    | http://www.speech.cs.cmu.edu/cgi-bin/cmudict | 2-Clause BSD                           |
| ~~gout-vosk tool~~          | ~~https://github.com/skys-mission/gout~~       | GPLv3                                  |
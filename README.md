# YouTube-automatically-downloads-translations
YouTube automatically downloads translations input YouTube url
以下是一个要求够花里胡哨，同时详细说明如何安装 Python 3、PyTube、FFmpeg 和 AutoSub 的 README.md 文件示例：

# 视频字幕提取器

## 简介

本项目是一个使用 Python 编写的视频字幕提取工具，可以从视频文件中提取音频，并将其转换为文本格式的字幕文件。本工具使用 PyTube 库下载 YouTube 视频，使用 FFmpeg 库提取视频音频，使用 AutoSub 库将音频转换为文本，并生成字幕文件。

## 安装要求

本项目需要在 Python 3 环境下运行，并且需要安装以下库：

- `PyTube`: 用于下载 YouTube 视频。可使用以下命令安装：

  ````
  pip install pytube
- `FFmpeg`: 用于提取视频文件中的音频。可从官网下载安装：[https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

- `AutoSub`: 用于将音频转换为文本格式的字幕文件。可使用以下命令安装：

  ````
  pip install autosub3
## 使用说明

1. 下载 YouTube 视频

   ````
   python YouTube.py <video_url>
   ````

   其中 `<video_url>` 是要下载的 YouTube 视频的 URL。

2. 提取视频音频并转换为字幕文件

   ````
   python extract_subtitles.py <video_file>
   ````
   
   其中 `<video_file>` 是要提取字幕的视频文件路径。

   提取完成后，将在视频文件所在目录下生成同名的字幕文件，格式为 SubRip (.srt)。

## 作者

- 作者：李祖明
- 邮箱：daojin110@outlook.com

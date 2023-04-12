import os
from pytube import YouTube
import subprocess
import argparse
def replace_special_chars(string, replacement=''):
    special_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|','【','】',' ']
    for char in special_chars:
        string = string.replace(char, replacement)
    return string

def download_video(url, output_path=None, quality='highest'):
    try:
        if not output_path:
            output_path = os.getcwd()
        yt = YouTube(url)
        video_info = {
            'title': replace_special_chars(yt.title),
            'length': yt.length,
            'thumbnail_url': yt.thumbnail_url,
            'description': yt.description
        }
        print(f"Downloading '{video_info['title']}'...")
        if quality == 'highest':
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        elif quality == 'lowest':
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()
        else:
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().find_by_resolution(quality)
        video_stream.download(output_path=output_path, filename=f"{video_info['title']}.mp4")
        print(f"Video downloaded successfully to {video_info['title']}.mp4")
        return video_info
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def add_subtitles(source_path, subtitle_path, output_path):
    cmmd = f'ffmpeg -i "{source_path}" -vf "subtitles=\'{subtitle_path}\'" "{output_path}"'
    subprocess.run(cmmd, check=True, shell=True)
            
def extract_english_subtitles(source_path, output_path):
    src_language = "en"
    dst_language = "zh-CN"
    api_key = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"
    os.environ['http_proxy'] = 'http://127.0.0.1:7890'
    os.environ['https_proxy'] = 'https://127.0.0.1:7890'
    command = f'autosub -S {src_language} -D {dst_language} "{source_path}" -o "{output_path}" -K {api_key}'
    print(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(output.decode())
    print(error.decode())       
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='下载 YouTube 视频并提取字幕')
    parser.add_argument('url', nargs='?', help='要下载的 YouTube 视频的 URL')
    parser.add_argument('--output_path', help='保存下载的视频和字幕的路径', default='.')
    args = parser.parse_args()
    if args.url is None:
        args.url = input('输入 YouTube 视频 URL:')
    video_info = download_video(args.url, output_path=None)
    if video_info is None:
        print("视频下载失败.")
    else:
        source_path = f"{video_info['title']}.mp4"
        output_path = f"{video_info['title']}.srt"
        print(f"{source_path}\n{output_path}")
        extract_english_subtitles(source_path, output_path)
        print('--------------------------------------------------')
        video_with_subtitles_path = f"{video_info['title']}_new.mp4"
        add_subtitles(source_path, output_path, video_with_subtitles_path)
        print(f"带字幕的视频已保存至{video_with_subtitles_path}")

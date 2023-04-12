import os
from pytube import YouTube
import subprocess
def download_video(url, output_path=None, quality='highest'):
    try:
        if not output_path:
            output_path = os.getcwd()
        yt = YouTube(url)
        video_info = {
            'title': yt.title,
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
        video_stream.download(output_path=output_path, filename=video_info['title']+'.mp4')
        print(f"Video downloaded successfully to {video_info['title']}+'.mp4'")
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
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(output.decode())
    print(error.decode())       
    
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_directory = input("Enter the output directory (leave blank for current directory): ")
    video_info = download_video(video_url, output_path=output_directory)
    if video_info is None:
        print("Video download failed.")
    else:
        source_path = os.path.join(output_directory, video_info['title'] + '.mp4')
        output_path = os.path.join(output_directory, video_info['title'] + '.srt')
        print(f"{source_path}\n{output_path}")

        extract_english_subtitles(source_path, output_path)
        print('--------------------------------------------------')

        # Add subtitles to the video
        video_with_subtitles_path = os.path.join(output_directory, video_info['title'] + '_with_subtitles.mp4')
        add_subtitles(source_path, output_path, video_with_subtitles_path)



        print(f"Video with subtitles saved to {video_with_subtitles_path}")

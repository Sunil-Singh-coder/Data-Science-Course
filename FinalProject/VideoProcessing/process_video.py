import os
import subprocess

video_folder = "VideoProcessing/Videos"
audio_folder = "VideoProcessing/Audio"

os.makedirs(audio_folder, exist_ok=True)

files = os.listdir(video_folder)

for file in files:
    tutorial = file.split(" [")[0].split(" #")[1]
    topic = file.split(" ｜ ")[0]

    input_file = os.path.join(video_folder, file)
    output_file = os.path.join(audio_folder, f"{topic} - {tutorial}.mp3")

    subprocess.run([
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-q:a", "2",
        output_file
    ], check=True)

    print(f"Converted: {output_file}")
import ffmpeg
import json
from PIL import Image
import os

input_video = r'..\Images\sample.mp4'
output_dir = 'extracted_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def extract_frames(input_video, output_dir):
    try:
        ffmpeg.input(input_video).output(os.path.join(output_dir, 'Iframe_%04d.png'), vf='select=eq(pict_type\\,I)', vsync='vfr').run()
        ffmpeg.input(input_video).output(os.path.join(output_dir, 'Pframe_%04d.png'), vf='select=eq(pict_type\\,P)', vsync='vfr').run()
        ffmpeg.input(input_video).output(os.path.join(output_dir, 'Bframe_%04d.png'), vf='select=eq(pict_type\\,B)', vsync='vfr').run()
        print(f"Frames have been successfully extracted and saved in '{output_dir}'.")

    except ffmpeg.Error as e:
        print(f"Error: {e.stderr.decode('utf8')}")

def display_frames_pillow(output_dir):
    for frame_file in sorted(os.listdir(output_dir)):
        frame_path = os.path.join(output_dir, frame_file)
        img = Image.open(frame_path)
        img.show()

extract_frames(input_video, output_dir)
display_frames_pillow(output_dir)

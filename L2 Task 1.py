import ffmpeg
import json
import os

input_video = r'..\Images\sample.mp4'

def extract_frame_info(input_video):
    try:
        probe = ffmpeg.probe(input_video, select_streams='v', show_frames=None, print_format='json')
        for frame in probe['frames']:
            print(f"Frame Number: {frame['coded_picture_number']}")
            print(f"Frame Type: {frame['pict_type']}")
            print(f"Timestamp: {frame['pts_time']}")
            print(f"Size: {frame['pkt_size']} bytes")
            print("-" + "-"*50)
            
    except ffmpeg.Error as e:
        print(f"Error: {e.stderr.decode('utf8')}")
       
extract_frame_info(input_video)


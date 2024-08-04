import ffmpeg
import os

input_video = r'..\Images\sample.mp4'
output_video = 'reconstructed_video.mp4'  
reduced_frame_rate = 1  
output_dir = 'extracted_I_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def extract_frames(input_video, output_dir):
    try:
        ffmpeg.input(input_video).output(os.path.join(output_dir, 'Iframe_%04d.png'), vf='select=eq(pict_type\\,I)', vsync='vfr').run()
        print(f"Frames have been successfully extracted and saved in '{output_dir}'.")

    except ffmpeg.Error as e:
        print(f"Error: {e.stderr.decode('utf8')}")

def create_video_from_frames(frames_dir, output_video, frame_rate):
    try:
        ffmpeg.input(os.path.join(frames_dir, 'frame_%04d.png'), framerate=frame_rate).output(output_video).run()
        print(f"New video created successfully: '{output_video}' with frame rate {frame_rate}.")
    except ffmpeg.Error as e:
        print(f"Error: {e.stderr.decode('utf8')}")

extract_frames(input_video, output_dir)
create_video_from_frames(output_dir, output_video, reduced_frame_rate)

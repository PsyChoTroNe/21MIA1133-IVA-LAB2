import ffmpeg
import json
import os
import matplotlib.pyplot as plt

input_video = r'..\Images\sample.mp4'
def extract_frame_info(input_video):
    try:
        probe = ffmpeg.probe(input_video, select_streams='v', show_frames=None, print_format='json')
        frame_counts = {'I': 0, 'P': 0, 'B': 0}
        total_frames = 0
        for frame in probe['frames']:
            frame_type = frame['pict_type']
            if frame_type in frame_counts:
                frame_counts[frame_type] += 1
                total_frames += 1
        percentages = {key: (value / total_frames) * 100 for key, value in frame_counts.items()}
        print(f"I-frames: {frame_counts['I']} ({percentages['I']:.2f}%)")
        print(f"P-frames: {frame_counts['P']} ({percentages['P']:.2f}%)")
        print(f"B-frames: {frame_counts['B']} ({percentages['B']:.2f}%)")
    except ffmpeg.Error as e:
        print(f"Error: {e.stderr.decode('utf8')}")
    plot_frame_distribution(frame_counts, percentages)
    
def plot_frame_distribution(frame_counts, percentages):
    frame_types = list(frame_counts.keys())
    counts = list(frame_counts.values())
    percents = [percentages[key] for key in frame_types]

    # Bar graph
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.bar(frame_types, counts, color=['blue', 'green', 'red'])
    plt.xlabel('Frame Type')
    plt.ylabel('Count')
    plt.title('Frame Count Distribution')

    # Pie chart
    plt.subplot(1, 2, 2)
    plt.pie(percents, labels=frame_types, autopct='%1.1f%%', colors=['blue', 'green', 'red'])
    plt.title('Frame Percentage Distribution')

    # Show plots
    plt.tight_layout()
    plt.show()
    
extract_frame_info(input_video)

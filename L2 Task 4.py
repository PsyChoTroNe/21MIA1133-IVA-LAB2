import ffmpeg
import os

input_dir = 'extracted_frames'

def calculate_frame_sizes(input_dir):
    frame_sizes = {'I': [], 'P': [], 'B': []}

    for frame_file in sorted(os.listdir(input_dir)):
        frame_path = os.path.join(input_dir, frame_file)
        frame_size = os.path.getsize(frame_path)
        
        # Determine frame type from filename
        if 'I' in frame_file:
            frame_type = 'I'
        elif 'P' in frame_file:
            frame_type = 'P'
        elif 'B' in frame_file:
            frame_type = 'B'
        else:
            continue
        
        frame_sizes[frame_type].append(frame_size)

    # Calculate average sizes
    average_sizes = {key: (sum(sizes) / len(sizes) if sizes else 0) for key, sizes in frame_sizes.items()}
    
    # Print results
    print("\nFrame Type Sizes:")
    for frame_type, sizes in frame_sizes.items():
        print(f"Total {frame_type}-frames: {len(sizes)}, Average size: {average_sizes[frame_type]:.2f} bytes")

    # Compare average sizes
    print("\nAverage Size Comparison:")
    for frame_type in average_sizes:
        print(f"{frame_type}-frames: {average_sizes[frame_type]:.2f} bytes")

    return average_sizes

frame_sizes = calculate_frame_sizes(input_dir)

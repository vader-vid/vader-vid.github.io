import os

def delete_gifs(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".gif"):
                gif_path = os.path.join(root, file)
                print(f"Deleting {gif_path}")
                os.remove(gif_path)

# Replace 'your_root_directory' with the path to your root directory
delete_gifs('videos')


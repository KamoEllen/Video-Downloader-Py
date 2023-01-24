import requests
import os

def download_video(url, path):
    # Open the video url
    video = requests.get(url, stream=True)
    # Open a file in the specified path to save the video
    with open(path, 'wb') as f:
        # Iterate through the video data and write it to the file
        for chunk in video.iter_content(1024):
            f.write(chunk)

# Example usage
download_video('https://link.com/video.mp4', 'path/to/save/video.mp4')

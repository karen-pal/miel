import subprocess
import random
import time
from pynput import keyboard


video_directory = "videos/"  # Change this to the path of your video directory
video_file_list = [
    'video1.mp4',
    'video2.mp4',
    'video3.mp4',
    # Add more video files as needed
]
delay=5
print(keyboard.Key)
def on_key_release(key):
    print(key)
    global delay
    if key == keyboard.Key.esc:
        return False  # Stop listener

    if key == keyboard.Key.right:
        delay += 1  # Increase delay
    elif key == keyboard.Key.left and delay > 1:
        delay -= 1  # Decrease delay, ensure it doesn't go below 1
# Create a listener to capture keyboard input
listener = keyboard.Listener(on_release=on_key_release)
listener.start()

def play_random_video():
    random_video_file = random.choice(video_file_list)
    video_source = f"{video_directory}{random_video_file}"

    # Set a random position for the video window
    window_x = random.randint(0, 1920)  # Adjust these values as needed
    window_y = random.randint(0, 1080)  # Adjust these values as needed

    mpv_command = [
        "mpv",
        video_source,
        "--no-audio",  # Mute audio
        "--autofit=1920x1080",  # Adjust to your desired video dimensions
        f"--geometry={window_x}:{window_y}",  # Set the window position
        "--on-all-workspaces",
        "--keep-open=no",  # Close mpv when playback ends
        "--no-osc",  # Disable on-screen controller
        "--no-input-default-bindings",  # Disable default input bindings

    ]

    mpv_process = subprocess.Popen(mpv_command)
    mpv_process.wait()

while True:
    play_random_video()
    print(delay)
    time.sleep(delay)  # Adjust the delay as needed
     


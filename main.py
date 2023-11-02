import subprocess
import random
import time
from pynput import keyboard


video_directory = "videos/"  # Change this to the path of your video directory
video_file_list = [
    'video1.mp4',
    'video2.mp4',
    'video3.mp4',
    'video4.mp4',
    'video5.mp4',
    'video6.mp4',
    # Add more video files as needed
]
delay=5
overlap_count = 2  # Number of overlapping videos
screen_number = 0
sequential_mode = True
def on_key_release(key):
    #print(key)
    global delay, overlap_count, sequential_mode

    if key == keyboard.Key.esc:
        return False  # Stop listener

    if key == keyboard.Key.right:
        delay += 1  # Increase delay
    elif key == keyboard.Key.left and delay > 1:
        delay -= 1  # Decrease delay, ensure it doesn't go below 1
    elif key == keyboard.Key.up:  # Use the up key to increase overlap count
        overlap_count += 1
        print("overlap_count: ",overlap_count)
    elif key == keyboard.Key.down:  # Use the down key to decrease overlap count
        if overlap_count > 1:
            overlap_count -= 1
        print("overlap_count: ",overlap_count)
    elif key == keyboard.Key.space:  # Use the space key to toggle between modes
        sequential_mode = not sequential_mode
        print("secuential_mode: ",sequential_mode)

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

def overlap_mode(overlap_count):
    video_processes = []

    while True:
        # Ensure that there are always `overlap_count` videos playing
        while len(video_processes) < overlap_count:
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
                f"--screen={screen_number}",  # Set the specific screen
                "--on-all-workspaces",
                "--keep-open=no",  # Close mpv when playback ends
                "--no-osc",  # Disable on-screen controller
                "--no-input-default-bindings",  # Disable default input bindings
                "--no-border"  # Hide the video outline
            ]

            mpv_process = subprocess.Popen(mpv_command)
            video_processes.append(mpv_process)

        # Check if any video processes have finished and replace them
        for i in range(len(video_processes)):
            if video_processes[i].poll() is not None:
                random_video_file = random.choice(video_file_list)
                video_source = f"{video_directory}{random_video_file}"

                # Set a random position for the new video window
                window_x = random.randint(0, 1920)  # Adjust these values as needed
                window_y = random.randint(0, 1080)  # Adjust these values as needed

                mpv_command = [
                    "mpv",
                    video_source,
                    "--no-audio",  # Mute audio
                    "--autofit=1920x1080",  # Adjust to your desired video dimensions
                    f"--geometry={window_x}:{window_y}",  # Set the window position
                    f"--screen={screen_number}",  # Set the specific screen

                    "--on-all-workspaces",
                    "--keep-open=no",  # Close mpv when playback ends
                    "--no-osc",  # Disable on-screen controller
                    "--no-input-default-bindings",  # Disable default input bindings
                    "--no-border"  # Hide the video outline
                ]

                mpv_process = subprocess.Popen(mpv_command)
                video_processes[i] = mpv_process

        # Sleep for a short duration to prevent high CPU usage
        time.sleep(delay)

# Call overlap_mode with the desired overlap_count


while True:
    print("secuential_mode: ",sequential_mode)
    if sequential_mode:
        play_random_video()
        print(delay)
        time.sleep(delay)  # Use the current delay
         
    else:
        overlap_mode(overlap_count)


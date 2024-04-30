# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load the videos you want to concatenate
video1 = VideoFileClip("video1.mp4")
video2 = VideoFileClip("video2.mp4")

# Concatenate the videos
concatenated_video = concatenate_videoclips([video1, video2])

# Export the concatenated video
concatenated_video.write_videofile("concatenated_video.mp4")

# Close the video clips
video1.close()
video2.close()

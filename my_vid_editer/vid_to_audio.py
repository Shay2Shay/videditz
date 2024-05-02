from moviepy.editor import *

# Load the mp4 file
def vid_to_audio(video="toothless-dance.mp4", audio="toothless_dance.mp3"):
    video = VideoFileClip(video)

    # Extract audio from video
    video.audio.write_audiofile(audio)
    video.close()
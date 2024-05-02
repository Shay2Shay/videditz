from moviepy.editor import VideoFileClip
# from moviepy.video import fx
import os
import sys
# video load kro
# clip = VideoFileClip("video2.mp4")
videoClip = VideoFileClip("video2.mp4")
gif = videoClip.write_gif("video2.gif")
videoClip.close()
# Define  start and end time
# end_time = 5
# start_time = 2




# # output ismein aaega
# output_gif = "output.gif"
# subclip = clip.subclip(start_time, end_time)

# # filter
# subclip = fx(subclip, factor=0.5)


# subclip = subclip.set_duration(subclip.duration). \
#     set_position(("center", "bottom")). \
#     set_start(start_time). \
#     set_end(end_time). \
#     set_fps(24). \
#     set_audio(clip.audio)


# subclip.write_gif(output_gif, fps=10)  # gif banao fps ke hisab se


# print(f"GIF creation done for time:{start_time} and endtime:{end_time}")

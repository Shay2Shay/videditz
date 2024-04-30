

from moviepy.editor import VideoFileClip

# Load the video you want to crop
video = VideoFileClip("video2.mp4")

# Define the dimensions of the cropping region (x1, y1, x2, y2)
# x1, y1 are the coordinates of the top-left corner
# x2, y2 are the coordinates of the bottom-right corner
x1, y1 = 100, 100  # Top-left corner
x2, y2 = 400, 300  # Bottom-right corner

# Crop the video
cropped_video = video.crop(x1=x1, y1=y1, x2=x2, y2=y2)

# Write the cropped video to a file
cropped_video.write_videofile("cropped_video.mp4")

# Close the original and cropped video clips
video.close()
cropped_video.close()

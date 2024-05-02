from moviepy.editor import VideoFileClip


class crop_video:
    def __init__(self, video="video2.mp4") -> None:
        self.video = VideoFileClip(video)

    def crop(self, output_path="cropped_video.mp4", x1=100,y1=100,x2=400,x3=300):
        video = self.video
        cropped_video = video.crop(x1=x1, y1=y1, x2=x2, y2=y2)
        cropped_video.write_videofile(output_path)
        video.close()
        cropped_video.close()

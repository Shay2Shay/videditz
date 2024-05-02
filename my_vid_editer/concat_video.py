from moviepy.editor import VideoFileClip, concatenate_videoclips

class concat_video:
    def __init__(self, video1='video1.mp4', video2='video2.mp4') -> None:
        self.video1 = VideoFileClip(video1)
        self.video2 = VideoFileClip(video2)
    
    def concat(self, output_path = 'concatenated_video.mp4'):
        video1, video2 = self.video1, self.video2
        concatenated_video = concatenate_videoclips([video1, video2])
        concatenated_video.write_videofile("concatenated_video.mp4")
        video1.close()
        video2.close()
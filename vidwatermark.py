from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_watermark(video_path, watermark_text, output_path):
    video_clip = VideoFileClip(video_path)

    watermark = (TextClip(watermark_text, fontsize=40, color='white', font='Arial-Bold')
                 .set_position(('right', 'bottom'))
                 .set_duration(video_clip.duration))

    video_with_watermark = CompositeVideoClip([video_clip, watermark])

    video_with_watermark.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    video_path = "video1-audio.mp4"
    watermark_text = "MS Project"
    output_path = f"{video_path[:-4]}_with_watermark.mp4"

    add_watermark(video_path, watermark_text, output_path)

from moviepy.editor import VideoFileClip, AudioFileClip

def add_audio_to_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)

    audio_clip = AudioFileClip(audio_path)

    if audio_clip.duration > video_clip.duration:
        audio_clip = audio_clip.subclip(0, video_clip.duration)
    elif audio_clip.duration < video_clip.duration:
        audio_clips = [audio_clip] * int(video_clip.duration // audio_clip.duration)
        audio_clip = concatenate_audioclips(audio_clips)
        audio_clip = audio_clip.set_duration(video_clip.duration)

    video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    video_path = "video1.mp4"
    audio_path = "audio.mp3"
    output_path = f"{video_path[:-4]}-{audio_path[:-4]}.mp4"

    add_audio_to_video(video_path, audio_path, output_path)

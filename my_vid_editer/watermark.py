from pathlib import Path
from inspect import cleandoc
from concurrent.futures import ProcessPoolExecutor
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip

class Watermark:
    def __init__(self, files, f_output, v_position, h_position, f_measure, f_fps, f_overwrite):
        self.files = files
        self.f_output = f_output
        self.v_position = v_position
        self.h_position = h_position
        self.f_measure = f_measure
        self.f_fps = f_fps
        self.f_overwrite = f_overwrite
        self.resize = {'small': 30, 'medium': 60, 'large': 90}

    def process_watermark(self, file):
        video = VideoFileClip(str(file))
        watermark = ImageClip('assets/watermark.png').set_duration(video.duration).resize(
            height=self.resize[self.f_measure]).margin(right=8, top=8, left=8, bottom=8, opacity=0).set_pos((self.h_position, self.v_position))

        new_filename = f'watermarked_{self.v_position}_{self.h_position}_{file.name}'

        final_folder = self.f_output.joinpath(file.stem)
        Path(final_folder).mkdir(parents=True, exist_ok=True)

        final_output = final_folder.joinpath(new_filename)
        final_file = CompositeVideoClip([video, watermark])
        final_file.write_videofile(
            str(final_output), fps=self.f_fps if self.f_fps else video.fps, temp_audiofile=Path(final_folder.joinpath(f'{file.stem}_TEMP_FILE.mp3')))

        video.close()

    def watermark_processor(self):
        with ProcessPoolExecutor() as executor:
            executor.map(self.process_watermark, self.files)

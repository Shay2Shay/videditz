from img_to_vid import img_to_vid
from concat_video import concat_video
from crop_video import crop_video
from vid_plus_audio import add_audio_to_video
from watermark import Watermark
from vid_to_audio import vid_to_audio

import os

if __name__ == "__main__":
    print("===================Testing Image to Video===================")
    image_dir = os.getcwd() + "\images\\"
    output_dir = os.getcwd() + "\out_vid\\"
    obj = img_to_vid(
        image_dir,
        output_dir,
        "test_result.avi",
        fps=1
    )
    obj.convert()

    print("===================Testing Audio from Video===================")
    vid_to_audio()

    print("===================Testing Concat Video===================")
    obj = concat_video()
    obj.concat()

    print("===================Testing Crop Video===================")
    obj = crop_video()
    obj.crop()

    print("===================Testing Add audio to Video===================")

    print("===================Testing Watermark===================")
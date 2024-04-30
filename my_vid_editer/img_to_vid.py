import cv2
import os
from tqdm import tqdm

class img_to_vid:
    def __init__(self, path, out_path, out_video_name, fps=24) -> None:
        self.path = path #'F:/img sequence/'
        self.out_path = out_path #'F:/img to vdo/'
        self.out_video_name = out_video_name #'fading cube2.mp4'
        self.out_video_full_path = out_path+out_video_name
        self.fps = fps

        self.pre_imgs = os.listdir(path)
        self.img = []
        for i in self.pre_imgs:
            i = path+i
            # print(i)
            self.img.append(i)
        
        cv2_fourcc = cv2.VideoWriter_fourcc(*'MJPG')

        frame = cv2.imread(self.img[0])
        size = list(frame.shape)
        # del size[2]
        # size.reverse()
        self.video = cv2.VideoWriter(self.out_video_full_path, cv2_fourcc, fps, (size[1], size[0])) #output video name, fourcc, fps, size

    def convert(self):
        for i in tqdm(range(len(self.img))): 
            self.video.write(cv2.imread(self.img[i]))

        self.video.release()
        print('outputed video to ', self.out_path)
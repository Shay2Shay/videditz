from my_vid_editer import *





if __name__ == '__main__':
    img2vid = img_to_vid('./images/', './out_vid/', 'test.avi', 1)
    img2vid.convert()
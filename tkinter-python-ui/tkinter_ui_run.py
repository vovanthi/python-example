from collections import deque
import cv2
from PIL import Image, ImageTk
import time
from tkinter import tix
import multiprocessing

root = tix.Tk()
image_label = tix.Label(master=root)
image_label.pack()
cam = cv2.VideoCapture(0)

share_dict = multiprocessing.Manager().dict()
fps = 10

def quit_(root):
    root.destroy()

def update_image(image_label, cam):
    (readsuccessful, frame) = cam.read()
    a = Image.fromarray(frame)
    b = ImageTk.PhotoImage(image=a)
    image_label.configure(image=b)
    image_label._image_cache = b
    root.update()

def getCature(share_dict):
    while True:
        (readsuccessful, frame) = cam.read()
        a = Image.fromarray(frame)
        b = ImageTk.PhotoImage(image=a)
        share_dict['IMG'] = b
        sleep(0.1)

def update_image_only(image_label, image):
    print('updtate image')
    image_label.configure(image=image)
    image_label._image_cache = image
    # root.update()

def update_all(root, image_label, fps):
    # update_image(image_label, cam)
    image_label.configure(image=share_dict['IMG'])
    image_label._image_cache = share_dict['IMG']
    root.after(int(3600 / fps), func=lambda: update_all(root, image_label, fps))

if __name__ == '__main__':
    multiprocessing.Process(target=getCature, args=(share_dict,)).start()
    root.after(0, func=lambda: update_all(root, image_label, fps))
    root.mainloop()
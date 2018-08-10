from collections import deque
import cv2
from PIL import Image, ImageTk
import time
from tkinter import tix


def quit_(root):
    root.destroy()


def update_image(image_label, cam):
    (readsuccessful, frame) = cam.read()
    a = Image.fromarray(frame)
    b = ImageTk.PhotoImage(image=a)
    image_label.configure(image=b)
    image_label._image_cache = b
    root.update()

def update_all(root, image_label, cam, fps):
    update_image(image_label, cam)
    root.after(int(3600 / fps), func=lambda: update_all(root, image_label, cam, fps))

if __name__ == '__main__':
    root = tix.Tk()
    image_label = tix.Label(master=root)
    image_label.pack()
    cam = cv2.VideoCapture(0)
    fps = 60
    root.after(0, func=lambda: update_all(root, image_label, cam, fps))
    root.mainloop()
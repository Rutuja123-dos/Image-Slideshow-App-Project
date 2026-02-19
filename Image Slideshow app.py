from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow")

#List of Image path
image_path = [
    r"Address of image 1.jpg",
    r"Address of image 2.jpg",
    r"Address of image 3.jpg", #Note : put the address path of image in .jpg or .png
]

#Resize the images to 1080x1080
image_size = (1080,1080)
images = [Image.open(path).resize(image_size) for path in image_path]
photo_images = [Image.Tk.photoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images :
        label.config(image = photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshows():
    for _ in range(len(image_path)):
        update_image()

play_button = tk.Button(root, text="start slideshow", command = start_slideshows)
play_button.pack()

root.mainloop()
from tkinter import *

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from basic_pillow import ImageEditor
import os
from tkinter import filedialog
import time

window = Tk()

window.title("Silver Rail: Imager Water Marker")
window.minsize(height=300, width=500)

global image_directory


# functions
def start_button_click():
    print(image_directory)
    name = folder_name.get()
    create_folder(name)
    txt = watermark_text.get()
    watermark_txt = txt.replace('/', '\n')
    color = watermark_color.get()
    print(watermark_txt)
    items = initialize_app(image_directory)
    watermark_images(items, text=watermark_txt, color=color, new_folder_name=name)


def new_folder_clicked():
    name = folder_name.get()
    create_folder(name)


def dir_button_clicked():
    global image_directory
    dir_name = filedialog.askdirectory(initialdir='C:\\Users\\Blade\\Desktop')
    print(dir_name)
    selected_source_label.configure(text=dir_name[15:])
    image_directory = dir_name


# Buttons

start_button = Button(text="Start", command=start_button_click)
start_button.grid(column=1, row=6)

new_folder_button = Button(text="Create", command=new_folder_clicked)
new_folder_button.grid(column=2, row=0)

source_button = Button(text="Select Source", command=dir_button_clicked)
source_button.grid(column=1, row=3)

# Entry
folder_name = Entry()
folder_name.grid(column=1, row=0)

watermark_text = Entry()
watermark_text.grid(column=1, row=1)

watermark_color = Entry()
watermark_color.grid(column=1, row=2)

# Label
# title_label = Label(text="Add watermark", font=("Arial", 8, "bold"))
# title_label.grid(column=0, row=-1)

folder_label = Label(text="Destination folder name", font=("Arial", 8, "bold"))
folder_label.grid(column=0, row=0)

text_label = Label(text="Enter Watermark text", font=("Arial", 8, "bold"))
text_label.grid(column=0, row=1)

color_label = Label(text="Enter Watermark color", font=("Arial", 8, "bold"))
color_label.grid(column=0, row=2)

source_label = Label(text="Select Source folder", font=("Arial", 8, "bold"))
source_label.grid(column=0, row=3)

selected_source_label = Label(text="Select Source folder", font=("Arial", 8, "bold"))
selected_source_label.grid(column=3, row=3)

#


def save_image(im, folder, name, ext):
    im.save(f"{folder}/{name}.{ext}")


def get_folder_items(folder):
    print(folder)
    items = []
    for f in os.listdir(folder):
        if f.endswith('.jpg') or f.endswith('.png'):
            im_path = f'{folder}/{f}'
            items.append(im_path)

    return items


def create_folder(new_folder_name):
    os.mkdir(os.path.join(os.getcwd(), new_folder_name))


def initialize_app(img_folder):
    editor = ImageEditor(Image, os, ImageFont, ImageDraw, plt)
    source_folder_name = img_folder.replace('/', "\\")

    # source_folder_name = "C:\\Users\\Blade\\Desktop\\New assets\\Grass Carpet\\Grass Carpet"

    img_items = get_folder_items(source_folder_name)
    print(img_items[:5])
    image = Image.open(img_items[1])
    image.show()
    return [editor, img_items]


def watermark_images(inputs, text, color, new_folder_name):
    img_items = inputs[1]
    editor = inputs[0]
    x = 1
    for image in img_items:
        wmk_img = editor.add_watermark(image, text, color)
        save_image(wmk_img, new_folder_name, f'img{x}', "jpg")
        x += 1


window.mainloop()

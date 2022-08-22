from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from basic_pillow import ImageEditor
import os
import time
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

window.title("Silver Rail: Imager Water Marker")
window.minsize(height=300, width=500)

# variables
title_row = 0
source_row = 1
destination_row = 2
generate_row = 5
size_row = 3
color_row = 4
global image_directory


# functions

def dir_button_clicked():
    global image_directory
    dir_name = filedialog.askdirectory(initialdir='C:\\Users\\Blade\\Desktop')
    print(dir_name)
    selected_source_label.configure(text=dir_name[15:])
    image_directory = dir_name


def generate_button_clicked():
    global image_directory
    new_folder = destination_input.get()
    create_folder(new_folder)
    source_path = image_directory.replace('/', "\\")
    img_size = int(size_input.get())
    data = initialize(source_path, img_size)
    bg = color_input.get()
    colors = bg.split(",")
    color = (int(colors[0]), int(colors[1]), int(colors[2]))
    bg_color = (153, 153, 255)
    print(bg_color)
    print(color)
    create_thumbnails(data, new_folder, bg_color=color)


# labels
title_label = tk.Label(text="Thumbnail maker", font=("Arial", 12, "bold"))
title_label.grid(column=1, row=title_row)

source_label = tk.Label(text="Select source folder", font=("Arial", 8, "bold"))
source_label.grid(column=0, row=source_row)

destination_label = tk.Label(text="Destination folder name", font=("Arial", 8, "bold"))
destination_label.grid(column=0, row=destination_row)

selected_source_label = tk.Label(text="Select Source folder", font=("Arial", 8, "bold"))
selected_source_label.grid(column=3, row=source_row)

enter_size_label = tk.Label(text="Enter thumbnail size", font=("Arial", 8, "bold"))
enter_size_label.grid(column=0, row=size_row)

color_label = tk.Label(text="Enter background color", font=("Arial", 8, "bold"))
color_label.grid(column=0, row=color_row)

# buttons
source_button = tk.Button(text="Select Source", command=dir_button_clicked)
source_button.grid(column=1, row=source_row)

generate_button = tk.Button(text="Generate", command=generate_button_clicked)
generate_button.grid(column=1, row=generate_row)
# inputs
destination_input = tk.Entry()
destination_input.grid(column=1, row=destination_row)

size_input = tk.Entry()
size_input.grid(column=1, row=size_row)

color_input = tk.Entry()
color_input.grid(column=1, row=color_row)


# file picker


def save_image(img, folder, name, ext):
    img.save(f"{folder}/{name}.{ext}")


def get_folder_items(folder):
    print(folder)
    items = []
    for f in os.listdir(folder):
        if f.endswith('.jpg') or f.endswith('.png'):
            im_path = f'{folder}/{f}'
            items.append(im_path)

    return items


def initialize(path, img_size):
    pics = get_folder_items(path)
    grid_size = (img_size, img_size)
    return [pics, grid_size]


def create_folder(new_folder_name):
    os.mkdir(os.path.join(os.getcwd(), new_folder_name))


def create_thumbnails(pic_info, new_folder, bg_color):
    images = pic_info[0]
    grid_size = pic_info[1]
    img_index = 1
    for pic in images:
        new_grid = Image.new(mode="RGB", size=grid_size, color=bg_color)
        im = Image.open(pic)
        t_width, t_height = new_grid.size
        im.thumbnail((t_width, t_height))
        im_width, im_height = im.size
        box_w = (t_width - im_width) / 2
        box_h = (t_height - im_height) / 2

        box = (round(box_w), round(box_h))
        new_grid.paste(im, box)
        # new_grid.show()
        save_image(new_grid, new_folder, f'img{img_index}', "png")
        img_index += 1


window.mainloop()

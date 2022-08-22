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


# Accepts he relative path of the image.
# def add_watermark(self, im_path, text, im_color):
#     image = self.Image.open(im_path)
#     watermark_image = image.copy()
#     h, w = watermark_image.size
#     draw = self.ImageDraw.Draw(watermark_image)
#     font = self.ImageFont.truetype("arial.ttf", 50)
#     draw.text((0.5 * h, 0.25 * w), text, fill=im_color, font=font, stroke_width=1)
#     self.plt.subplot(1, 2, 2)
#     self.plt.title("white text")
#     self.plt.imshow(watermark_image)
#     return watermark_image


def save_image(im, folder, name, ext):
    im.save(f"{folder}/{name}.{ext}")


im_path = "680/image35_680.jpg"

# Opening Image


# create a text and font object
watermark_fonts = {
    "roboto": "C:\\Users\\Blade\\Desktop\\Fonts\\Roboto\\Roboto-BlackItalic.ttf",
    "Scheherazade_bold": "C:\\Users\\Blade\\Desktop\\Fonts\\Scheherazade_New\\ScheherazadeNew-Bold.ttf",
    "Scheherazade_regular": "C:\\Users\\Blade\\Desktop\\Fonts\\Scheherazade_New\\ScheherazadeNew-Regular.ttf",
    "Rampart_One": "C:\\Users\\Blade\\Desktop\\Fonts\\Rampart_One\\RampartOne-Regular.ttf",
    "lobster": "C:\\Users\\Blade\\Desktop\\Fonts\\Lobster_Two\\LobsterTwo-BoldItalic.ttf",
    "kumar": "C:\\Users\\Blade\\Desktop\\Fonts\\Kumar_One_Outline\\KumarOneOutline-Regular.ttf",
    "italiano": "C:\\Users\\Blade\\Desktop\\Fonts\\Italianno\\Italianno-Regular.ttf",
    "iceland": "C:\\Users\\Blade\\Desktop\\Fonts\\Iceland\\Iceland-Regular.ttf",
    "fredrick": "C:\\Users\\Blade\\Desktop\\Fonts\\Fredericka_the_Great\\FrederickatheGreat-Regular.ttf",
    "codysta": "C:\\Users\\Blade\\Desktop\\Fonts\\Codystar\\Codystar-Regular.ttf",
    "cinzel": "C:\\Users\\Blade\\Desktop\\Fonts\\Cinzel_Decorative\\CinzelDecorative-Bold.ttf",
    "astloch": "C:\\Users\\Blade\\Desktop\\Fonts\\Astloch\\Astloch-Bold.ttf",
    "embelma": "C:\\Users\\Blade\\Desktop\\Fonts\\Emblema_One\\EmblemaOne-Regular.ttf",
    "plaster": "C:\\Users\\Blade\\Desktop\\Fonts\\Plaster\\Plaster-Regular.ttf"

}


# image = Image.open(im_path)
# watermark_image = image.copy()
#
# # create a draw object
# draw = ImageDraw.Draw(watermark_image)

# calculate postions
def calculate_position(text, font, draw_object, watermark_image):
    text_w, text_h = draw_object.textsize(text, font)
    w, h = watermark_image.size
    h_diff = h - text_h - 15
    w_diff = w - text_w - 15
    x = w / 2 - text_w / 2
    y = h / 2 - text_h / 2

    #  seven positions
    tl = (10, 10)
    tr = (w_diff, 10)
    bl = (10, h_diff)
    br = (w_diff, h_diff)
    center = (x, y)
    cl = (10, y)
    cr = (w_diff, y)
    positions = [tl, tr, bl, br, center, cl, cr]
    return positions


# Apply text on image
def add_single_watermark(watermark_txt, font_style, color, position, folder, img_path):
    image = Image.open(img_path)
    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)
    # create a draw object
    draw = ImageDraw.Draw(watermark_image)
    print(watermark_fonts)
    font = ImageFont.truetype(watermark_fonts[font_style], 72)
    positions = calculate_position(watermark_txt, font=font, draw_object=draw, watermark_image=watermark_image)
    text_position = positions[position]
    draw.text(text_position, watermark_txt, font=font, fill=color)
    watermark_image.show()
    return watermark_image
    # save_image(watermark_image, folder, "image1", "png")


def watermark_image_folder(source_folder, watermark_txt, font_style, color, position, folder):
    img_items = get_folder_items(source_folder)
    x = 1
    for image in img_items:
        wmk_img = add_single_watermark(watermark_txt, font_style, color, position, folder, image)
        save_image(wmk_img, folder, f'img{x}', "jpg")
        x += 1


# draw.text((0.5 * h, 0.25 * w), text, fill=im_color, font=font, stroke_width=1)

def create_folder(new_folder_name):
    os.mkdir(os.path.join(os.getcwd(), new_folder_name))


def get_folder_items(folder):
    print(folder)
    items = []
    for f in os.listdir(folder):
        if f.endswith('.jpg') or f.endswith('.png'):
            im_path = f'{folder}/{f}'
            items.append(im_path)

    return items


# __________________________UI Set UP _____________________________________
window = tk.Tk()
window.title("Silver Rail:Add text watermark")
window.minsize(height=300, width=500)

window.title("Silver Rail: Imager Water Marker")
window.minsize(height=300, width=500)

global image_directory

# variables

destination_row = 0
text_row = 1
color_row = 2
font_row = 3
folder_row = 4
start_row = 5


# functions
def start_button_click():
    # print(image_directory)
    name = folder_name.get()
    # create_folder(name)
    source_folder_name = image_directory.replace('/', "\\")
    txt = watermark_text.get()
    watermark_txt = txt.replace('/', '\n')
    color = watermark_color.get()
    print(watermark_txt)
    font_style = fonts.get()
    print(font_style)
    print(type(font_style))
    text_position = 1
    image_location = "900/img1.png"
    # items = initialize_app(image_directory)
    # watermark_images(items, text=watermark_txt, color=color, new_folder_name=name)
    # add_single_watermark(folder=name, font_style=str(font_style), position=text_position, color=color,
    #                      watermark_txt=watermark_txt, img_path=image_location)
    watermark_image_folder(folder=name, source_folder=source_folder_name, font_style=str(font_style), position=text_position, color=color, watermark_txt=watermark_txt)


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

start_button = tk.Button(text="Start", command=start_button_click)
start_button.grid(column=1, row=start_row)

new_folder_button = tk.Button(text="Create", command=new_folder_clicked)
new_folder_button.grid(column=2, row=destination_row)

source_button = tk.Button(text="Select Source", command=dir_button_clicked)
source_button.grid(column=1, row=folder_row)

# Entry
folder_name = tk.Entry()
folder_name.grid(column=1, row=destination_row)

watermark_text = tk.Entry()
watermark_text.grid(column=1, row=text_row)

watermark_color = tk.Entry()
watermark_color.grid(column=1, row=color_row)

# Label
# title_label = Label(text="Add watermark", font=("Arial", 8, "bold"))
# title_label.grid(column=0, row=-1)

folder_label = tk.Label(text="Destination folder name", font=("Arial", 8, "bold"))
folder_label.grid(column=0, row=destination_row)

text_label = tk.Label(text="Enter Watermark text", font=("Arial", 8, "bold"))
text_label.grid(column=0, row=text_row)

color_label = tk.Label(text="Enter Watermark color", font=("Arial", 8, "bold"))
color_label.grid(column=0, row=color_row)

font_label = tk.Label(text="Choose font", font=("Arial", 8, "bold"))
font_label.grid(column=0, row=font_row)

source_label = tk.Label(text="Select Source folder", font=("Arial", 8, "bold"))
source_label.grid(column=0, row=folder_row)

selected_source_label = tk.Label(text="Select Source folder", font=("Arial", 8, "bold"))
selected_source_label.grid(column=3, row=folder_row)

# Drop downs
fonts_list = (
    "Scheherazade_bold",
    "roboto",
    "Scheherazade_regular",
    "lobster",
    "Rampart_One",
    "kumar",
    "iceland",
    "italiano",
    "fredrick",
    "codystar",
    "cinzel",
    "astloch",
    "embelma",
    "plaster"
)

fonts = tk.StringVar()
fonts.set(fonts_list[2])
drop_fonts = tk.OptionMenu(window, fonts, *fonts_list)
drop_fonts.grid(column=1, row=font_row)

# Check box

var1 = tk.IntVar()
var2 = tk.IntVar()
tk.Checkbutton(window, text="male", variable=var1).grid(row=6, column=0)

tk.Checkbutton(window, text="female", variable=var2).grid(row=6, column=1)

window.mainloop()
#

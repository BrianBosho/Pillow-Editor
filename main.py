from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from basic_pillow import ImageEditor
import os
import time


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


editor = ImageEditor(Image, os, ImageFont, ImageDraw, plt)

# add_watermark(self, im_path, text, im_color)
# four_grid(self, images, dimension)
# resize_image(self, im_path, size)
# select_images(self, file_folder, new_folder, im_size, time)
# folder_name = "C:\\Users\\Blade\\Desktop\\Web Automation\\downloader\\saved_images"
# folder_name = "C:\\Users\\Blade\\Desktop\\Web Automation\\pillow_editor\\New curtains images"
# folder_name = "C:\\Users\\Blade\\Desktop\\Curtains"
# folder_name = "C:\\Users\\Blade\\Desktop\\New assets\\Wall2Wall Delta\\Wall2Wall Delta"
folder_name = "C:\\Users\\Blade\\Desktop\\New assets\\Grass Carpet\\Grass Carpet"

img_items = get_folder_items(folder_name)
# print(img_items[:5])
image = Image.open(img_items[1])
image.show()

text = 'Silver\n Interiors'
x = 1
for image in img_items[:1]:
    wmk_img = editor.add_watermark(image, text, 'yellow')
    save_image(wmk_img, 'kengrw', f'img{x}', "jpg")
    x += 1
    wmk_img.show()

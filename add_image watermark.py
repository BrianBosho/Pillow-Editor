from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from basic_pillow import ImageEditor
import os
import time


def get_folder_items(folder):
    print(folder)
    items = []
    for f in os.listdir(folder):
        if f.endswith('.jpg') or f.endswith('.png'):
            im_path = f'{folder}/{f}'
            items.append(im_path)

    return items


folder_name = "680"
img_items = get_folder_items(folder_name)


def save_image(im, folder, name, ext):
    im.save(f"{folder}/{name}.{ext}")


# image = Image.open(img_items[1])


def add_image_watermark(img):
    image = Image.open(img)
    (w, h) = image.size
    l_w = round(0.2 * w)
    l_h = round(0.2 * h)
    w_diff = w - l_w
    h_diff = h - l_h
    tl = (0, 0)
    bl = (0, h_diff)
    br = (w_diff, h_diff)
    tr = (w_diff, 0)
    logo = "SR logos/logo1.jpg"
    img_logo = Image.open(logo)
    logo_size = (l_w, l_h)
    img_logo.thumbnail(logo_size)
    image.paste(img_logo, tl)
    image.show()
    save_image(image, "680", "image2", "png")


img = "680/image35_680.jpg"
add_image_watermark(img)


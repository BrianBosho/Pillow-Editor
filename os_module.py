from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from basic_pillow import ImageEditor
import os
import time

path = "kenwtw"


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


pics = get_folder_items(path)

grid_size = (900, 900)
t_height = 900
t_width = 900
x = 1
for pic in pics[:2]:
    new_grid = Image.new(mode="RGBA", size=grid_size, color='white')
    im = Image.open(pic)
    im.thumbnail((t_width, t_height))
    im_width, im_height = im.size
    box_w = (t_width - im_width) / 2
    box_h = (t_height - im_height) / 2

    box = (round(box_w), round(box_h))
    new_grid.paste(im, box)
    # new_grid.show()
    save_image(new_grid, 'thumbnails', f'img{x}', "png")
    x += 1

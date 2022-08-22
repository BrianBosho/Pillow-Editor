from PIL import Image
import os
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt

image1 = Image.open("watermark_680/image32_680_w.jpg")
image1.save(f"watermark_680/png/img1.png")

# n = 1
# for f in os.listdir('watermark_680'):
#     im = Image.open(f'watermark_680/{f}')
#     im.save(f"watermark_680/png/img{n}.png")
#     n += 1

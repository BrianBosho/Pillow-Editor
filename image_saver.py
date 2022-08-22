import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

image_file = "C:\\Users\\Blade\\Desktop\\Web Automation\\process-jumia-data\\long_image_links.txt"

# Accepts the url to a page and a path to a folder.
# Downloads all the image sfrom that page and saves in that folder.
image_list = []
with open(image_file, 'r') as file:
    while line := file.readline().rstrip():
        image_list.append(line)

img = "https://ke.jumia.is/unsafe/fit-in/150x150/filters:fill(white)/product/91/940174/6.jpg?6075"

with open("img1", 'wb') as f:
    im = requests.get(img)
    f.write(im.content)


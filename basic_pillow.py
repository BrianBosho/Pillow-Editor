class ImageEditor:
    def __init__(self, Image, os, ImageFont, ImageDraw, plt):
        self.Image = Image
        self.os = os
        self.ImageFont = ImageFont
        self.ImageDraw = ImageDraw
        self.plt = plt

    # Accepts he relative path of the image.
    def add_watermark(self, im_path, text, im_color):
        image = self.Image.open(im_path)
        watermark_image = image.copy()
        h, w = watermark_image.size
        draw = self.ImageDraw.Draw(watermark_image)
        font = self.ImageFont.truetype("arial.ttf", 50)
        draw.text((0.5*h, 0.25*w), text, fill=im_color, font=font, stroke_width=1)
        self.plt.subplot(1, 2, 2)
        self.plt.title("white text")
        self.plt.imshow(watermark_image)
        return watermark_image

    # this accepts an array of 4 images & the dimensions of that image(assumes square images) returns a photo of 4
    # grids the dimensions of the photo are twice that of the entered dimension
    def four_grid(self, images, dimension):
        new_grid = self.Image.new("RGBA", (2*dimension, 2*dimension))
        pics = []
        for image in images:
            new_image = self.Image.open(image)
            h, w = new_image.size
            if h == dimension:
                pics.append(new_image)
        box1 = (0, 0)
        box2 = (dimension, dimension)
        box3 = (0, dimension)
        box4 = (dimension, 0)

        boxes = [box1, box2, box3, box4]
        for x in range(4):
            new_grid.paste(pics[x], boxes[x])
        return new_grid

    # accepts the path of the file and the size which is a tuple, returns a resized Image object.
    def resize_image(self, im_path, size):
        im = self.Image.open(im_path)
        im2 = im.resize(size)
        return im2

    # accepts the folder names & selects jpeg of the specified height. The selected photos are added to th new folder
    def select_images(self, file_folder, new_folder, im_size, time):
        n = 1
        for f in self.os.listdir(file_folder):
            if f.endswith('.jpg') or f.endswith('.png'):
                print(f)
                try:
                    im = self.Image.open(f'{file_folder}/{f}')
                    print(f'{file_folder}/{f}')
                    print(im)
                    h, w = im.size
                    print(h)
                    time.sleep(1)
                    if h == im_size:
                        im.save(f"{new_folder}/img{n}.png")
                        n += 1
                        print("saved")
                    else:
                        print(f"height is {h}, provided size is {im_size}")
                    print(" ")
                except Exception as e:
                    print("Cannot identify image file ", e)
#         filter the resized images


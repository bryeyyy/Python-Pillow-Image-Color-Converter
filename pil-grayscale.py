from cProfile import label
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

filename = "euphoria.jpg"
with Image.open(filename) as img:
    img.load()

font = ImageFont.truetype("Roboto-Regular.ttf", 32)

img2 = img.convert("RGB")
draw =  ImageDraw.Draw(img2)
draw.text((50, 50),"Original",(255, 255, 255),font=font)
img2.save("original.jpg")

#convert to grayscale
gray_img= img.convert("L")
draw2 = ImageDraw.Draw(gray_img)
draw2.text((50, 50),"Grayscale",(255),font=font)
gray_img.save("eupGray.jpg")


#collage 
imgarr=[ 'original.jpg','eupGray.jpg']

def create_collage(width, height, imgarr):
    cols = 2
    rows = 1
    thumbnail_width = width//cols
    thumbnail_height = height//rows
    size = thumbnail_width, thumbnail_height
    new_img = Image.new('RGB', (width, height))
    ims = []
    for p in imgarr:
        im = Image.open(p)
        im.thumbnail(size)
        ims.append(im)
    i = 0
    x = 0
    y = 0
    for col in range(cols):
        for row in range(rows):
            print(i, x, y)
            new_img.paste(ims[i], (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    new_img.show()
    new_img.save("Collage.jpg")

create_collage(1224, 612, imgarr)

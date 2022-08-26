from cProfile import label
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

filename = "sample.jpg"
with Image.open(filename) as img:
    img.load()

font = ImageFont.truetype("arial.ttf", 32)

img2 = img.convert("RGB")
draw =  ImageDraw.Draw(img2)
draw.text((50, 50),"Original",(255, 255, 255),font=font)
img2.save("original.jpg")

#convert to grayscale
gray_img= img.convert("L")
draw2 = ImageDraw.Draw(gray_img)
draw2.text((50, 50),"Grayscale",(255),font=font)
gray_img.save("Gray.jpg")


#convert to CMYK color space
cmyk_img=img.convert("CMYK")
draw3 =  ImageDraw.Draw(cmyk_img)
draw3.text((50, 50),"CMYK",(0,0,0,0),font=font)
cmyk_img.save("cmyk.jpg")

#split rgb
red, green, blue = img.split()
z_val=red.point(lambda _:0)

#red conversion
red_img= Image.merge("RGB", (red,z_val,z_val))
draw4 =  ImageDraw.Draw(red_img)
draw4.text((50, 50),"Red Component",(255, 255, 255),font=font)
red_img.save("Red.jpg")

#green conversion
green_img= Image.merge("RGB", (z_val,green,z_val))
draw5 =  ImageDraw.Draw(green_img)
draw5.text((50, 50),"Green Component",(255, 255, 255),font=font)
green_img.save("Green.jpg")

#blue conversion
blue_img= Image.merge("RGB", (z_val,z_val,blue))
draw6 =  ImageDraw.Draw(blue_img)
draw6.text((50, 50),"Blue Component",(255, 255, 255),font=font)
blue_img.save("Blue.jpg")

#collage 
imgarr=[ 'original.jpg','cmyk.jpg','Red.jpg','Green.jpg','Blue.jpg','Gray.jpg' ]

def create_collage(width, height, imgarr):
    cols = 3
    rows = 2
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
            i += -1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    new_img.show()
    new_img.save("Collage.jpg")

create_collage(1836, 1224, imgarr)

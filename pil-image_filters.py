from cProfile import label
from PIL import Image, ImageFilter, ImageFont, ImageDraw 

filename = "family.jpg"
with Image.open(filename) as img:
    img.load()


img2 = img.convert("RGB")
img2.save("original.jpg")

#convert to grayscale
gray_img= img.convert("L")
gray_img.save("Gray.jpg")


#split rgb
red, green, blue = img.split()
z_val=red.point(lambda _:0)

#red conversion
red_img= Image.merge("RGB", (red,z_val,z_val))
red_img.save("Red.jpg")

#green conversion
green_img= Image.merge("RGB", (z_val,green,z_val))
green_img.save("Green.jpg")

#blue conversion
blue_img= Image.merge("RGB", (z_val,z_val,blue))
blue_img.save("Blue.jpg")

#filters 
emb=img.filter(ImageFilter.EMBOSS)
emb.save("emboss.jpg")

img_edge=img.filter(ImageFilter.FIND_EDGES)
img_edge.save("edges.jpg")

img_cont=img.filter(ImageFilter.CONTOUR)
img_cont.save("contour.jpg")

img_blr=img.filter(ImageFilter.BoxBlur(10))
img_blr.save("blur.jpg")

img_rot=img.rotate(90, expand=True)
img_rot.save("rotate.jpg")


#collage 
imgarr=[ 'original.jpg','Red.jpg','Green.jpg','Blue.jpg','Gray.jpg','emboss.jpg','edges.jpg','contour.jpg','blur.jpg','rotate.jpg', ]

def create_collage(width, height, imgarr):
    cols = 5
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

create_collage(3600, 1440, imgarr)

from PIL import Image


def mirror(image):
    image = image.crop((0, 0, 850, 850))        #cut the imge(0,0,w,h)
    pix = image.load()
    w = image.size[0]                           #???
    for x in range(w):
        for y in range(w // 2):
            pix[x, w - y - x - 1], pix[y + x - w + 1, w - x - 1] = pix[y + x - w + 1, w - x - 1], pix[x, w - y - x - 1]
    image.save("res.jpeg")


im = Image.open("owl.jpeg")
mirror(im)
res = Image.open("res.jpeg")
res.show()

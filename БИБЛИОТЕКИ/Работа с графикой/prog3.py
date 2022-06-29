from PIL import Image


def mirror(image):
    pixels = image.load()
    w = image.size[0]
    h = image.size[1]
    for x in range(w // 2):
        for y in range(h):
            pixels[x, y], pixels[w - x - 1, y] = pixels[w - x - 1, y], pixels[x, y]
    image.save("res.jpeg")


im = Image.open("owl.jpeg")
mirror(im)
res = Image.open("res.jpeg")
res.show()

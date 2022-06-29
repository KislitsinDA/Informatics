from PIL import Image


def make_preview(size, n_colors):
    image = Image.open("owl.jpeg")
    image = image.resize(size).quantize(n_colors)
    image.save("res.bmp")
    res = Image.open("res.bmp")
    res.show()


make_preview((400, 200), 64)

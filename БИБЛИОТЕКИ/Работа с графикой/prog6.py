from PIL import Image, ImageDraw


def gradient(color):
    image = Image.new("RGB", (512, 200))
    draw = ImageDraw.Draw(image)
    for i in range(0, 256):
        if color.upper() == "R":
            draw.rectangle(((i * 2, 0), (i * 2 + 2, 200)), (i, 0, 0))
        elif color.upper() == "G":
            draw.rectangle(((i * 2, 0), (i * 2 + 2, 200)), (0, i, 0))
        elif color.upper() == "B":
            draw.rectangle(((i * 2, 0), (i * 2 + 2, 200)), (0, 0, i))
    image.save("res.png")
    res = Image.open("res.png")
    res.show()


gradient("R")

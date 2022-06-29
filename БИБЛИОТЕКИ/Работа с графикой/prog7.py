from PIL import Image, ImageDraw


def board(num, size):
    image = Image.new("RGB", (num * size, num * size))
    draw = ImageDraw.Draw(image)
    for i in range(num):
        for j in range(num):
            if i % 2 == 0:
                if j % 2 == 0:
                    draw.rectangle((size * j, size * i, (size * (j + 1), size * (i + 1))), fill="black")
                else:
                    draw.rectangle((size * j, size * i, (size * (j + 1), size * (i + 1))), fill="white")
            else:
                if j % 2 == 0:
                    draw.rectangle((size * j, size * i, (size * (j + 1), size * (i + 1))), fill="white")
                else:
                    draw.rectangle((size * j, size * i, (size * (j + 1), size * (i + 1))), fill="black")
    image.save("res.png")
    res = Image.open("res.png")
    res.show()


board(8, 50)
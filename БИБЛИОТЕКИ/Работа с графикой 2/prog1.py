from PIL import Image


def twist_image(input_file_name, output_file_name):
    image = Image.open(input_file_name)
    w = image.size[0]
    h = image.size[1]
    pix = image.load()
    for x in range(w // 2):
        for y in range(h):
            pix[x, y], pix[w // 2 + x - 1, y] = pix[w // 2 + x - 1, y], pix[x, y]
    image.save(output_file_name)
    res = Image.open(output_file_name)
    res.show()


twist_image("img10.jpg", "result.jpg")

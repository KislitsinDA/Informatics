from PIL import Image


def transparency(filename1, filename2):
    image1 = Image.open(filename1)
    image2 = Image.open(filename2)
    w, h = image2.size
    pix1 = image1.load()
    pix2 = image2.load()
    for x in range(w):
        for y in range(h):
            r1, g1, b1 = pix1[x, y]
            r2, g2, b2 = pix2[x, y]
            pix1[x, y] = (int(0.5 * r1 + 0.5 * r2), int(0.5 * g1 + 0.5 * g2), int(0.5 * b1 + 0.5 * b2))
    image1.show()


transparency("Natus_Vincere.jpg", "G2.jpg")

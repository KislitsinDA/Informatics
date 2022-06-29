from PIL import Image, ImageFilter


def motion_blur(n):
    image = Image.open("owl.jpeg")
    res = image.transpose(Image.Transpose.ROTATE_270)
    res = res.filter(ImageFilter.GaussianBlur(radius=n))
    res.show()


motion_blur(10)

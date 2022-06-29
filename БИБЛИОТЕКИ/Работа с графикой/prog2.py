from PIL import Image
image = Image.open("owl.jpeg")
#list of pixels of image
ls_pixels = image.load()
w, h = image.size
print(sum([ls_pixels[x, y][0] for x in range(w) for y in range(h)]) // (w * h) + 1, end=" ")
print(sum([ls_pixels[x, y][1] for x in range(w) for y in range(h)]) // (w * h), end=" ")
print(sum([ls_pixels[x, y][2] for x in range(w) for y in range(h)]) // (w * h), end=" ")

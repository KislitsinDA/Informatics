from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color="#87CEEB", ocean_color="#017B92", boat_color="#874535",
            sail_color="#FFFFFF", sun_color="#FFCF40"):
    image = Image.new("RGB", (width, height), sky_color)
    draw = ImageDraw.Draw(image)
    draw.rectangle(((0, 0.8 * height), (width, height)), ocean_color)
    draw.polygon(((0.25 * width, 0.65 * height), (0.3 * width, 0.85 * height), (0.7 * width, 0.85 * height),
                  (0.75 * width, 0.65 * height)), fill=boat_color)
    draw.polygon(((0.51 * width, 0.3 * height), (0.66 * width, 0.45 * height), (0.51 * width, 0.6 * height)),
                 fill=sail_color)
    draw.line((0.5 * width, 0.3 * height, 0.5 * width, 0.65 * height), fill=boat_color, width=int(0.02 * width))
    draw.ellipse((0.8 * width, -0.2 * height, 1.2 * width, 0.2 * height), fill=sun_color)
    image.save(file_name)
    image.show()


picture("test.bmp", 1000, 800)

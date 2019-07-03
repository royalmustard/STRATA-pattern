from PIL import Image

#RGB irrelevant | on/off | dwelltime 1(min) - 255(Max in software configuration)

class Converter:

    def __init__(self):
        self.image = None

    def load_image(self, filename):
        self.image = Image.load(filename)

    def convert_image_to_bmp(self):
        self.image = self.image.convert("L")
        width, height = self.img.size
        new_image = Image.new("RGB", (width, height), color=(0, 0, 0))
        for x in width:
            for y in height:
                grey = self.image.getpixel((x, y))
                if grey != 255:
                    new_image.putpixel((x, y), (0, 1, 255-grey))
        new_image.save(self.image.filename.split(".")[0]+".bmp")

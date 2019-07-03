from PIL import Image

#RGB irrelevant | on/off | dwelltime 1(min) - 255(Max in software configuration)


class Converter:

    def __init__(self):
        self.image = None

    def load_image(self, filename):
        self.image = Image.load(filename)
        self.image = self.image.convert("L")

    def convert_image_to_bmp(self):
        width, height = self.img.size
        new_image = Image.new("RGB", (width, height), color=(0, 0, 0))
        for x in width:
            for y in height:
                grey = self.image.getpixel((x, y))
                if grey != 255:
                    new_image.putpixel((x, y), (0, 1, 255-grey))
        new_image.save(self.image.filename.split(".")[0]+".bmp")

    def convert_image_to_streamfile(self):
        """DO NOT USE, calculations cannot be made. DISCOUNTINIUED"""

        streamfile = open(self.image.filename.split(".")[0]+".stf", "wb+")
        width, height = self.img.size
        maxwidth = 4095
        minheight = 280
        maxheight = 3816
        #Resize if over sepcied size to minimize artifacts and loss
        if width > maxwidth or height < minheight or height > maxheight:
            wpercent = (maxwidth / float(self.image.size[0]))
            hsize = int((float(self.image.size[1]) * float(wpercent)))
            self.image = self.image.resize((maxwidth, hsize), Image.ANTIALIAS)

        for x in width:
            for y in height:
                grey = self.image.getpixel((x, y))
                if grey != 255:
                    cmd = "96 {} {}".format(x, y)
                    cmd = cmd.encode("ascii")
                    streamfile.write()
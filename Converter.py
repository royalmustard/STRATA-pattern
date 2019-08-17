from PIL import Image
import time
#RGB: irrelevant | on/off | dwelltime 1(min) - 255(Max in software configuration)


class Converter:

    def __init__(self):
        self.image = None
        self.name = ""
        self.grayscale = None
        self.final = None
        self.threshold = 0

    def load_image(self, filename):
        self.image = Image.open(filename)
        self.name = filename.split(".")[0]
        self.grayscale = self.image.convert("L")

    def convert_image_to_bmp(self):
        gs = self.grayscale
        th = self.threshold
        width, height = self.image.size
        new_image = Image.new("RGB", (width, height), color=(0, 0, 0))
        start = time.time()
        for x in range(width):
            for y in range(height):
                grey = gs.getpixel((x, y))
                if grey < 255-th:
                    new_image.putpixel((x, y), (0, 1, 255-grey))
        end = time.time()
        print(end-start)
        self.final = new_image

    def save_image(self, filename):
        self.final.save(filename)

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
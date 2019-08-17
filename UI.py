from tkinter import filedialog as df
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time
import libSTRATAconv_rust as rconv


class UI:

	def __init__(self):
		self.root = Tk()
		self.root.title("STRATA pattern")
		self.frame = Frame(self.root)
		self.frame.grid(column=0, row=0, sticky=(N, E, W, S))

		self.in_filename = StringVar()
		self.in_image = None
		self.out_filename = StringVar()
		self.out_image = None
		self.threshold = IntVar()
		self.conv_image = None

		ttk.Label(self.frame, text="Input file").grid(row=1, column=1, sticky=N)
		ttk.Entry(self.frame, textvariable=self.in_filename, width=50).grid(row=3, column=1, sticky=N)
		ttk.Button(self.frame, command=self.get_path, text="Open file").grid(row=4, column=1, sticky=N)
		self.cnv_in_image = Canvas(self.frame, width=300, height=300)
		self.cnv_in_image.grid(row=2, column=1, sticky=N)

		ttk.Label(self.frame, text="Output file").grid(row=1, column=2, sticky=N)
		ttk.Entry(self.frame, textvariable=self.out_filename, width=50).grid(row=3, column=2, sticky=N)
		ttk.Button(self.frame, command=self.get_output_filename, text="Set output file").grid(row=4, column=2, sticky=N)
		self.cnv_out_image = Canvas(self.frame, width=300, height=300)
		self.cnv_out_image.grid(row=2, column=2, sticky=N)

		ttk.Label(self.frame, text="Filter threshold").grid(row=5, column=1, sticky=N)
		ttk.Scale(self.frame, from_=0, to=254, orient=HORIZONTAL, length=280, variable=self.threshold)\
			.grid(row=5, column=2, sticky=N)

		ttk.Button(self.frame, command=self.convert, text="Convert image").grid(row=6, column=1, sticky=N)
		ttk.Label(self.frame, text="Image is automatically saved upon conversion").grid(row=6, column=2, sticky=N)

		self.frame.mainloop()

	def get_path(self):
		self.in_filename.set(df.askopenfilename())
		self.in_image = Image.open(self.in_filename.get())
		self.in_image = self.in_image.resize((300, 300), Image.ANTIALIAS)
		self.in_image = ImageTk.PhotoImage(self.in_image)
		self.cnv_in_image.create_image((0, 0), anchor=NW, image=self.in_image)

	def get_output_filename(self):
		self.out_filename.set(df.asksaveasfilename(defaultextension="bmp"))

	def convert(self):

		if self.out_filename.get() == "":
			self.get_output_filename()

		print(self.out_filename.get())
		#self.conv.load_image(self.in_filename.get())
		#self.conv.threshold = self.threshold.get()
		#self.conv.convert_image_to_bmp()
		start = time.time()
		rconv.convert(self.in_filename.get(), self.out_filename.get(), self.threshold.get())
		end = time.time()
		print(end - start)
		self.conv_image = Image.open(self.out_filename.get())
		#width, height = self.conv_image.size
		oi = Image.new("L", (300, 300), color=255)

		conv_im = self.conv_image.resize((300, 300), Image.ANTIALIAS)
		for x in range(300):
			for y in range(300):
				r, g, b = conv_im.getpixel((x, y))
				if g == 1:
					oi.putpixel((x, y), b)


		self.out_image = oi
		self.out_image = ImageTk.PhotoImage(self.out_image)
		self.cnv_out_image.create_image((0, 0), anchor=NW, image=self.out_image)


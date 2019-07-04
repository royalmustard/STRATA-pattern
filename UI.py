from tkinter import filedialog as df
import Converter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class UI:

	def __init__(self):
		self.conv = Converter.Converter()
		self.root = Tk()
		self.root.title("STRATA pattern")
		self.frame = Frame(self.root)
		self.frame.grid(column=0, row=0, sticky=(N, E, W, S))

		self.in_filename = StringVar()
		self.in_image = None
		self.out_filename = ""

		ttk.Label(self.frame, text="Input file").grid(row=1, column=1, sticky=N)
		ttk.Entry(self.frame, textvariable=self.in_filename, width=50).grid(row=2, column=1, sticky=N)
		ttk.Button(self.frame, command=self.get_path, text="Open file").grid(row=3, column=1, sticky=N)
		self.cnv_in_image = Canvas(self.frame, width=300, height=300)
		self.cnv_in_image.grid(row=1, column=3, sticky=N)

		self.get_path()

		self.frame.mainloop()

	def get_path(self):
		self.in_filename.set(df.askopenfilename())
		self.in_image = Image.open(self.in_filename.get())
		self.in_image = ImageTk.PhotoImage(self.in_image)
		self.cnv_in_image.create_image((0, 0), anchor=NW, image=self.in_image)

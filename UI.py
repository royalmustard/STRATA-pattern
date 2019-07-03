from tkinter import filedialog as df

class UI:

	def __init__(self):
		pass

	def get_path(self):
		return df.askopenfilename()

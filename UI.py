from tkinter import filedialog as df

class UI:
	def getPath(self):
		return df.askopenfilename()
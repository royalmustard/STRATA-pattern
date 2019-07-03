from tkinter import filedialog as df


class UI:

	def get_path(self):
		return df.askopenfilename()

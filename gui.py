import tkinter
import csv
from tkinter import *

root = tkinter.Tk()
root.title("Personalised News Recommender System")

# open file
with open("output_file.csv", newline = "") as file:
	reader = csv.reader(file)

   # r and c tell us where to grid the labels
	r = 0
	for col in reader:
		c = 0
		for row in col:
         # i've added some styling
			label = tkinter.Label(root, width = 100, height = 2,padx = 20, \
                               text = row, relief = tkinter.RIDGE)
			label.grid(row = r, column = c)
			c += 1
		r += 1

root.mainloop()

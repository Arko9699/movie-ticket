from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

root = Tk()
root.title("Now Showing")

#button functions
def click():
    return

#images
#bellobottom
bellbottom_img = Image.open("bellbottomposter.png")
bellbottom_img = bellbottom_img.resize((300,450), Image.ANTIALIAS)
bellbottom_img = ImageTk.PhotoImage(bellbottom_img)
bellbottom_label = Label(root, image = bellbottom_img)
bellbottom_label.grid(row= 0, column = 0, padx = 0, pady = 5)

#free guy
freeguy_img = Image.open("freeguyposter.png")
freeguy_img = freeguy_img.resize((300,450), Image.ANTIALIAS)
freeguy_img = ImageTk.PhotoImage(freeguy_img)
freeguy_label = Label(root, image = freeguy_img)
freeguy_label.grid(row= 0, column = 1)

#pierrot
pierrot_img = Image.open("pierrotposter.png")
pierrot_img = pierrot_img.resize((300,450), Image.ANTIALIAS)
pierrot_img = ImageTk.PhotoImage(pierrot_img)
pierrot_label = Label(root, image = pierrot_img)
pierrot_label.grid(row= 0, column = 2)

#f9
f9_img = Image.open("f9poster.png")
f9_img = f9_img.resize((300,450), Image.ANTIALIAS)
f9_img = ImageTk.PhotoImage(f9_img)
f9_label = Label(root, image = f9_img)
f9_label.grid(row= 0, column = 3)

#shang
shang_img = Image.open("shangposter.png")
shang_img = shang_img.resize((300,450), Image.ANTIALIAS)
shang_img = ImageTk.PhotoImage(shang_img)
shang_label = Label(root, image = shang_img)
shang_label.grid(row= 0, column = 4)

#buttons
font_button = font.Font(size = 16, weight = 'bold', family = 'Helvetica')

bell_btn = Button(root, text = "Bell Bottom", command = click, font = font_button )
bell_btn.grid(row = 1, column = 0, ipadx = 20)
freeguy_btn = Button(root, text = "Free Guy", command = click, font = font_button )
freeguy_btn.grid(row = 1, column = 1, ipadx = 20)
pierrot_btn = Button(root, text = "Pierrot-Le-Fou", command = click, font = font_button )
pierrot_btn.grid(row = 1, column = 2, ipadx = 20)
f9_btn = Button(root, text = "Fast and Furious 9", command = click, font = font_button )
f9_btn.grid(row = 1, column = 3, ipadx = 20)
shang_btn= Button(root, text = "Shang-Chi", command = click, font = font_button )
shang_btn.grid(row = 1, column = 4, ipadx = 20)

root.mainloop()
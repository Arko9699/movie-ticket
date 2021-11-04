from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
nowshowing_root = Tk()
nowshowing_root.title("Now Showing")


class nowshowing:

    def __init__(self, name, sizex, sizey, img_name, row, column):
        self.name = name
        self.sizex = sizex
        self.sizey = sizey
        self.img_name = img_name
        self.row = row
        self.column = column
        self.image1 = Image.open(self.img_name)

    def makelabel(self):

        def click(mname):
            f1 = open("moviename.txt", "w")
            if mname == "Shang-Chi":
                f1.writelines("Shang-Chi and the Legend of the Ten Rings")
            else:
                f1.writelines(mname)
            f1.close()
            nowshowing_root.destroy()
        font_button = font.Font(size=16, weight='bold', family='Helvetica')
        self.image1 = self.image1.resize((self.sizex, self.sizey), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.image1)
        image_label = Label(nowshowing_root, image=self.image1)
        image_label.grid(row=self.row, column=self.column, padx=0, pady=5)
        image_btn = Button(nowshowing_root, text=self.name, command=lambda: click(self.name), font=font_button)
        image_btn.grid(row=self.row + 1, column=self.column)


def movieobjects():
    movie1 = nowshowing("Bell Bottom", 250, 375, "assets/bellbottomposter.png", 0, 0)
    movie2 = nowshowing("Free Guy", 250, 375, "assets/freeguyposter.png", 0, 1)
    movie3 = nowshowing("Pierrot-Le-Fou", 250, 375, "assets/pierrot-le-fouposter.png", 0, 2)
    movie4 = nowshowing("Fast and Furious 9", 287, 375, "assets/fastandfurious9poster.png", 0, 3)
    movie5 = nowshowing("Shang-Chi", 250, 375, "assets/shang-chiposter.png", 0, 4)
    movie1.makelabel()
    movie2.makelabel()
    movie3.makelabel()
    movie4.makelabel()
    movie5.makelabel()
    nowshowing_root.mainloop()

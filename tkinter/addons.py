from tkinter import *
from PIL import ImageTk, Image

addons_root = Tk()
addons_root.title("Select Addons")

def check():
    options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    clicked1, clicked2, clicked3, clicked4 = IntVar(), IntVar(), IntVar(), IntVar()
    clicked1.set(0), clicked2.set(0), clicked3.set(0), clicked4.set(0)
    ent1, ent2, ent3, ent4 = OptionMenu(addons_root, clicked1, *options), OptionMenu(addons_root, clicked2, *options),\
        OptionMenu(addons_root, clicked3, *options), OptionMenu(addons_root, clicked4, *options)

    def item(x1, y1, ent):
        ent.grid(row=x1, column=y1, sticky=E, padx=(100, 0))

    def addons_add():
        list1 = ["\n", str(clicked1.get())," ", str(clicked2.get())," ", str(clicked3.get()), " ", str(clicked4.get())]
        f1 = open("moviename.txt", 'a')
        f1.writelines(list1)
        f1.close()
        addons_root.destroy()
        return

    def images(path, x, y):
        img = Image.open(path)
        img = img.resize((150, 150), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        canvas = Label(addons_root, image=img)
        canvas.image = img
        canvas.grid(row=x, column=y, sticky=W)

    # Large Popcorn
    images("assets/addons/popcornL.png", 0, 0)
    Label(addons_root, text="Popcorn L | ₹200").grid(row=1, column=0, sticky=W)
    item(1, 0, ent1)

    # Small Popcorn
    images("assets/addons/popcornS.png", 0, 3)
    Label(addons_root, text="Popcorn S | ₹120").grid(row=1, column=3, sticky=W)
    item(1, 3, ent2)

    # Large Coke
    images("assets/addons/cokeL.png", 3, 0)
    Label(addons_root, text="Coke L | ₹150").grid(row=4, column=0, sticky=W)
    item(4, 0, ent3)

    # Small Coke
    images("assets/addons/cokeS.png", 3, 3)
    Label(addons_root, text="Coke S | ₹80").grid(row=4, column=3, sticky=W)
    item(4, 3, ent4)

    # Padding
    Label(addons_root).grid(row=2, pady=10)
    Label(addons_root).grid(column=2, padx=10)
    Button(addons_root, text="Continue", command=addons_add).grid(row=6, column=3, sticky=E)
    addons_root.resizable(False, False)
    addons_root.mainloop()

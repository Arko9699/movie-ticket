```py
from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Add some snacks")

class addons:

    global ent1, ent2, ent3, ent4
    ent1, ent2, ent3, ent4 = Entry(root, width=3), Entry(root, width=3), Entry(root, width=3), Entry(root, width=3)
    
    def check():
               
        pl, ps, cs, cl = BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar()

        def item(name,x1,y1,ent):
            if name.get():
                ent.grid(row=x1,column=y1, sticky=E, padx=(130,0))
                ent.insert(0,"0")
            else:
                ent.delete(0, END)
                ent.grid_forget()  
        
        def images(path,x,y):
            img = Image.open(path)
            img = img.resize((150,150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            canvas = Label(root, image=img)
            canvas.image = img
            canvas.grid(row=x, column=y, sticky=W)
        
        #Large Popcorn
        images("tkinter/assets/addons/popcornL.png", 0, 0)
        Checkbutton(root, text="Popcorn L | ₹200", variable=pl, command=lambda: item(pl,1,0,ent1)).grid(row=1,column=0, sticky=W)

        #Small Popcorn
        images("tkinter/assets/addons/popcornS.png", 0, 3)  
        Checkbutton(root, text="Popcorn S | ₹120", variable=ps, command=lambda: item(ps,1,3,ent2)).grid(row=1,column=3, sticky=W)

        #Large Coke
        images("tkinter/assets/addons/cokeL.png", 3, 0)
        Checkbutton(root, text="Coke L | ₹150", variable=cl, command=lambda: item(cl,4,0,ent3)).grid(row=4,column=0, sticky=W)

        #Small Coke
        images("tkinter/assets/addons/cokeS.png", 3, 3)
        Checkbutton(root, text="Coke S | ₹80", variable=cs, command=lambda: item(cs,4,3,ent4)).grid(row=4,column=3, sticky=W)

        #Padding
        blankx=Label(root).grid(row=2, pady=10)
        blanky=Label(root).grid(column=2, padx=10)
    check()
        
addons()
Button(root, text="Continue").grid(row=6,column=3, sticky=E)
root.mainloop()
```
from tkinter import *
from PIL import ImageTk, Image
root=Tk()

class addons:

    global ent1, ent2, ent3, ent4, clicked4, clicked1, clicked2, clicked3
    options = [0,1,2,3,4,5,6,7,8,9]
    clicked1, clicked2, clicked3, clicked4 = IntVar(),IntVar(),IntVar(),IntVar()
    clicked1.set(0), clicked2.set(0), clicked3.set(0), clicked4.set(0)
    ent1, ent2, ent3, ent4 = OptionMenu(root, clicked1, *options), OptionMenu(root, clicked2, *options), OptionMenu(root, clicked3, *options), OptionMenu(root, clicked4, *options)
    
    def check():

        def item(x1,y1,ent):    
            ent.grid(row=x1,column=y1, sticky=E, padx=(100,0)) 
        
        def images(path,x,y):
            img = Image.open(path)
            img = img.resize((150,150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            canvas = Label(root, image=img)
            canvas.image = img
            canvas.grid(row=x, column=y, sticky=W)
        
        #Large Popcorn
        images("assets/addons/popcornL.png", 0, 0)
        Label(root, text="Popcorn L | ₹200").grid(row=1,column=0, sticky=W)
        item(1,0,ent1)

        #Small Popcorn
        images("assets/addons/popcornS.png", 0, 3)  
        Label(root, text="Popcorn S | ₹120").grid(row=1,column=3, sticky=W)
        item(1,3,ent2)

        #Large Coke
        images("assets/addons/cokeL.png", 3, 0)
        Label(root, text="Coke L | ₹150").grid(row=4,column=0, sticky=W)
        item(4,0,ent3)

        #Small Coke
        images("assets/addons/cokeS.png", 3, 3)
        Label(root, text="Coke S | ₹80").grid(row=4,column=3, sticky=W)
        item(4,3,ent4)

        #Padding
        blankx=Label(root).grid(row=2, pady=10)
        blanky=Label(root).grid(column=2, padx=10)
    check()
        
addons()
Button(root, text="Continue").grid(row=6,column=3, sticky=E)
root.mainloop()

print(clicked1.get())
print(clicked2.get())
print(clicked3.get())
print(clicked4.get())

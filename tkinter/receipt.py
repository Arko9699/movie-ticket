from tkinter import *
from PIL import ImageTk, Image, ImageGrab
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)
receipt_root = Tk()
receipt_root.title("Receipt")

screen_width = receipt_root.winfo_screenwidth()
screen_height = receipt_root.winfo_screenheight()

def takemoviename():
    f1 = open("moviename.txt", "r")
    a = f1.readlines()
    return a


movie_name = takemoviename()[0].replace('\n', "")
movie_lang = takemoviename()[1].replace('\n', "")
movie_d = "(" + takemoviename()[2].replace('\n', "") + ")"
movie_venue = takemoviename()[3].replace('\n', "") + "\nKolkata"
movie_time = takemoviename()[4].replace('\n', "") + "| 7TH OCT 2021"
movie_seats = "Seats - " + takemoviename()[5].replace('\n', "")
total_price = "Rs " + takemoviename()[7].replace('\n', "")
seat_price = "Rs " + takemoviename()[8].replace('\n', "")
addon_price = "Rs " + takemoviename()[9].replace('\n', "")

if movie_name == "Shang-Chi and the Legend of the Ten Rings":
    movie_name = f"Shang-Chi and the Legend {movie_d}\nof the Ten Rings"
    movie_img_name = "assets/shang-chiposter.png"
else:
    movie_img_name = movie_name.replace(" ", "")
    movie_img_name = "assets/" + movie_img_name.lower() + "poster.png"
    movie_name = movie_name + " " + movie_d


def receipts():
    
    def click():
        
        im = ImageGrab.grab(bbox=(x+8, y+30, x+width+8, y+height-50))
        im.save("BookingReceipt.png")
        receipt_root.destroy()

    # Labels
    Label(receipt_root, text="Booking ID: 920390", font=("Arial", 20)).grid(row=0, columnspan=3, sticky="S", pady=10)
    Label(receipt_root, text=movie_name, font=("Arial", 24), justify="left").grid(row=1, column=0, pady=20,
                                                                                  padx=5, sticky=W)
    Label(receipt_root, text=movie_time, font=("Arial", 15)).grid(row=2, column=0, sticky="W", padx=5)
    Label(receipt_root, text=movie_venue, font=("Arial", 15), justify="left").grid(row=3, column=0, padx=5,
                                                                                   sticky="W", pady=10)
    Label(receipt_root, text=movie_seats, font=("Arial", 15)).grid(row=4, column=0, padx=5, sticky="W", pady=10)
    Label(receipt_root, text="", font=("Arial", 20)).grid(row=5, column=0, padx=5, sticky="W")
    Label(receipt_root, text="Ticket amount", font=("Arial", 20)).grid(row=6, column=0, padx=5, sticky="W")
    Label(receipt_root, text=f"-       {seat_price}", font=("Arial", 20)).grid(row=6, column=1,
                                                                                padx=5, sticky="E")
    Label(receipt_root, text="Other items", font=("Arial", 20)).grid(row=7, column=0, padx=5, sticky="W")
    Label(receipt_root, text=f"-       {addon_price}", font=("Arial", 20)).grid(row=7, column=1,
                                                                                 padx=5, sticky="E")
    Label(receipt_root, text="Total Amount Paid", font=("Arial", 20)).grid(row=8, column=0, padx=5, sticky="W")
    Label(receipt_root, text=f"-       {total_price}", font=("Arial", 20)).grid(row=8, column=1,
                                                                                 padx=5, sticky="E")
    Button(receipt_root, text="Download Receipt", font=("Arial", 20), command=click).grid(row=9, columnspan=3,
                                                                                          sticky="S", pady=15)

    img = Image.open(movie_img_name)
    img = img.resize((200, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas = Label(receipt_root, image=img)
    canvas.image = img
    canvas.grid(row=1, column=1, rowspan=4)

    receipt_root.resizable(False, False)
    receipt_root.overrideredirect(True)

    receipt_root.update()
    width = receipt_root.winfo_width()
    height = receipt_root.winfo_height()
    x, y = (screen_width/2) - (width/2), (screen_height/2) - (height/2)
    receipt_root.geometry('+%d+%d' % (x, y))
    receipt_root.resizable(False, False)
    receipt_root.mainloop()

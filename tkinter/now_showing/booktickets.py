from tkinter import *
from PIL import ImageTk, Image
from db_connector import *
bookroot = Tk()
bookroot.title("Book Tickets")
db_con = createCon()


def takemoviename():
    f1 = open("moviename.txt", "r")
    a = f1.readline()
    return a


class BookTickets:
    moviename = takemoviename()
    rootbooktickets = bookroot

    def __init__(self, movieimgname, myresult):
        self.movieimgname = movieimgname
        self.myresult = myresult
        self.image1 = Image.open(self.movieimgname)

    def makephotolabel(self):

        def click():
            langroot = Toplevel()
            langroot.mainloop()
            return
        self.image1 = self.image1.resize((350, 525), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.image1, master=bookroot)
        img_label = Label(bookroot, image=self.image1)
        img_label.grid(row=0, column=0, rowspan=9)
        mname_label = Label(bookroot, text=self.moviename, font=("Arial", 30, 'bold'), wraplength=550, justify=LEFT)
        mname_label.grid(row=0, column=1, sticky=SW, rowspan=3, padx=10)
        about_label = Label(bookroot, text="About The Movie", font=("Arial", 20))
        about_label.grid(row=4, column=1, padx=10, sticky=SW, rowspan=1, columnspan=1)
        mdesc_label = Label(bookroot, text=self.myresult[0][0], font=("Arial", 14), justify=LEFT, wraplength=400)
        mdesc_label.grid(row=5, column=1, padx=10, sticky=NW, rowspan=1, columnspan=1)
        mrating_label = Label(bookroot, text=self.myresult[0][1], font=("Arial", 15))
        mrating_label.grid(row=6, column=1, sticky=SW, padx=10)
        mrating_label = Label(bookroot, text="|{}| ".format(self.myresult[0][2]) + " |{}| ".format(self.myresult[0][3]), font=("Arial", 15))
        mrating_label.grid(row=7, column=1, sticky=NW, padx=10)
        book_btn = Button(bookroot, text="Book Tickets", font=("Arial", 25), command=click)
        book_btn.grid(row=8, column=1, sticky=SW, padx=10, pady=10, columnspan=1)


class bookticketsobject:
    def __init__(self):
        myresult = movieDetails(takemoviename(), db_con)
        if takemoviename() == "Shang-Chi and the Legend of the Ten Rings":
            m1 = "assets/shang-chiposter.png"
        else:
            m = takemoviename().replace(" ", "")
            m1 = "assets/" + m.lower() + "poster.png"
        b = BookTickets(m1, myresult)
        b.makephotolabel()
        bookroot.mainloop()

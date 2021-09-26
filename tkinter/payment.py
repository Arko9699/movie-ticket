from tkinter import *

root=Tk()
root.geometry("375x200")
root.title("Payment Options")

def netbank():
    blank=Label(root).grid(column=1, pady=5, sticky=E)

    userid_input = Entry(root, width = 30)
    userid_input.insert(0, "Enter user ID")
    userid_input.grid(row = 1, column = 1, sticky=W, padx = 5)

    pass_input= Entry(root, width = 30)
    pass_input.insert(0, "Enter password")
    pass_input.grid(row = 2, column = 1, sticky=W, padx=5)

    #Labels for input boxes
    userid_label = Label(root, text = "User ID", pady = 2).grid(row = 1, column = 0, sticky=W, padx=10)
    pass_label = Label(root, text = "Password", pady = 2).grid(row = 2, column = 0, sticky=W, padx=10)

def card():
    blank=Label(root).grid(column=1, pady=5)

    cardnumber_input = Entry(root, width = 30)
    cardnumber_input.insert(0, "Enter card number")
    cardnumber_input.grid(row = 1, column = 1, sticky=W, padx = 5)

    cardname_input= Entry(root, width = 30)
    cardname_input.insert(0, "Enter name on the card")
    cardname_input.grid(row = 2, column = 1, sticky=W, padx=5)

    expm_input = Entry(root, width = 5)
    expm_input.insert(0, "MM")
    expm_input.grid(row = 3, column=1, sticky=W, padx=5)

    sep=Label(root,text="/").grid(row = 3, column=1, sticky=W, padx=39)

    expy_input = Entry(root, width = 5)
    expy_input.insert(0, "YY")
    expy_input.grid(row = 3, column=1, sticky=W, padx=50)

    cvv_input = Entry(root, width = 6)
    cvv_input.insert(0, "CVV")
    cvv_input.grid(row = 4, column = 1, sticky=W, padx=5)

    #Labels for input boxes
    cardnumber_label = Label(root, text = "Card Number", pady = 2).grid(row = 1, column = 0, sticky=W, padx=10)
    cardname_label = Label(root, text = "Name on card owner", pady = 2).grid(row = 2, column = 0, sticky=W, padx=10)
    expiry_label = Label(root, text = "Expiry date", pady = 2).grid(row = 3, column = 0, sticky=W, padx=10)
    cvv_label = Label(root, text = "CVV", pady = 2).grid(row = 4, column = 0, sticky=W, padx=10)

def clear():
    list = root.grid_slaves()
    for l in list:
        l.destroy()

page1btn = Button(root, text="Net Banking", command=lambda:[clear(), netbank()])
page1btn.place(x=0, y=0)
page2btn = Button(root, text="Credit/Debit Card", command=lambda:[clear(), card()])
page2btn.place(x=80, y=0)
cont=Button(root, text="Continue")
cont.place(x=310, y=169)

root.mainloop()

from tkinter import *

payment_root = Tk()
payment_root.geometry("375x200")
payment_root.title("Payment Options")
def payment1():

    def page1():
        def click():
            payment_root.destroy()
        page1btn = Button(payment_root, text="Net Banking", command=lambda: [clear(), netbank()])
        page1btn.place(x=0, y=0)
        page2btn = Button(payment_root, text="Credit/Debit Card", command=lambda: [clear(), card()])
        page2btn.place(x=80, y=0)
        cont = Button(payment_root, text="Continue", command=click)
        cont.place(x=310, y=169)
    page1()

    def netbank():
        blank = Label(payment_root).grid(column=1, pady=5)

        userid_input = Entry(payment_root, width=30)
        userid_input.insert(0, "Enter user ID")
        userid_input.grid(row=1, column=1, sticky=W, padx=5)

        pass_input = Entry(payment_root, width=30)
        pass_input.insert(0, "Enter password")
        pass_input.grid(row=2, column=1, sticky=W, padx=5)

        # Labels for input boxes
        userid_label = Label(payment_root, text="User ID", padx=40, pady=2).grid(row=1, column=0)
        pass_label = Label(payment_root, text="Password", pady=2).grid(row=2, column=0)


    def card():
        blank = Label(payment_root).grid(column=1, pady=5)

        cardnumber_input = Entry(payment_root, width=30)
        cardnumber_input.insert(0, "Enter card number")
        cardnumber_input.grid(row=1, column=1, sticky=W, padx=5)

        cardname_input = Entry(payment_root, width=30)
        cardname_input.insert(0, "Enter name on the card")
        cardname_input.grid(row=2, column=1, sticky=W, padx=5)

        expm_input = Entry(payment_root, width=5)
        expm_input.insert(0, "MM")
        expm_input.grid(row=3, column=1, sticky=W, padx=5)

        sep = Label(payment_root, text="/").grid(row=3, column=1, sticky=W, padx=39)

        expy_input = Entry(payment_root, width=5)
        expy_input.insert(0, "YY")
        expy_input.grid(row=3, column=1, sticky=W, padx=50)

        cvv_input = Entry(payment_root, width=6)
        cvv_input.insert(0, "CVV")
        cvv_input.grid(row=4, column=1, sticky=W, padx=5)

        #Labels for input boxes
        cardnumber_label = Label(payment_root, text="Card Number", padx=40, pady=2).grid(row=1, column=0)
        cardname_label = Label(payment_root, text="Name on card owner", pady=2).grid(row=2, column=0)
        expiry_label = Label(payment_root, text="Expiry date", pady=2).grid(row=3, column=0)
        cvv_label = Label(payment_root, text="CVV", pady=2).grid(row=4, column=0)


    def clear():
        lst = payment_root.grid_slaves()
        for i in lst:
            i.destroy()

    payment_root.resizable(False, False)
    payment_root.mainloop()


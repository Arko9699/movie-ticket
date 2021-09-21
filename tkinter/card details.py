from tkinter import *
root = Tk()
root.title("Enter Card Details")
root.geometry("370x150")

#payment function
def payment():
   cardnumber = cardnumber_input.get()
   cardname = cardname_input.get()
   expirym = expirym_input.get()
   expiryy = expiryy_input.get()
   cvv = cvv_input.get()
   cardnumber_input.delete(0, END)
   cardname_input.delete(0, END)
   expirym_input.delete(0, END)
   expiryy_input.delete(0, END)
   cvv_input.delete(0, END)

#Input boxes
cardnumber_input = Entry(root, width = 30)
cardnumber_input.insert(0, "Enter the number of your card")
cardnumber_input.grid(row = 0, column = 1, padx = 5)

cardname_input= Entry(root, width = 30)
cardname_input.insert(0, "Enter name on the card")
cardname_input.grid(row = 1, column = 1)

expirym_input = Entry(root, width = 5)
expirym_input.insert(0, "MM")
expirym_input.grid(row = 2, column=1, sticky=W, padx=5)

expiryy_input = Entry(root, width = 5)
expiryy_input.insert(0, "YY")
expiryy_input.grid(row = 2, column=1, sticky=W, padx=42)

cvv_input = Entry(root, width = 30)
cvv_input.insert(0, "CVV")
cvv_input.grid(row = 3, column = 1)

#Labels for input boxes
cardnumber_label = Label(root, text = "Card Number", padx = 40, pady = 2).grid(row = 0, column = 0)
cardname_label = Label(root, text = "Name on card owner", pady = 2).grid(row = 1, column = 0)
expiry_label = Label(root, text = "Expiry date", pady = 2).grid(row = 2, column = 0)
cvv_label = Label(root, text = "CVV", pady = 2).grid(row = 3, column = 0)

#Make payment button
payment_button = Button(root, text = "Make Payment", command = payment)
payment_button.grid(row = 4, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 50)

root.mainloop()

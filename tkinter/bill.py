from tkinter import *

bill_root = Tk()
bill_root.title("Bill")


def bills():
    def click():
        bill_root.destroy()

    f = open("moviename.txt", 'a+')
    f.seek(0)
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

    seats = lines[-2].split()
    extras = lines[-1].split()
    
    def seatcost():
        high, med, low = 0, 0, 0
        for i in seats:
            if i[0] in ["A", "B"]:
                high += 1
            elif i[0] in ["I", "J"]:
                low += 1
            else:
                med += 1
        seatprice = high * 250 + med * 190 + low * 170
        return seatprice, low, med, high

    def addonscost():
        addonsprice = int(extras[0]) * 200 + int(extras[1]) * 120 + int(extras[2]) * 150 + int(extras[3]) * 80
        return (addonsprice)

    addonsprice = addonscost()
    seatprice, low, med, high = seatcost()
    Label(bill_root, text="Bill", font=("Arial", 18)).grid(row=0, column=0, columnspan=3)
    # seats
    if high != 0:
        Label(bill_root, font=15, text="Gold | ₹250").grid(row=1, sticky=W)
        Label(bill_root, font=15, text=high).grid(row=1, column=1)
    if med != 0:
        Label(bill_root, font=15, text="Silver | ₹190").grid(row=1, sticky=W)
        Label(bill_root, font=15, text=med).grid(row=1, column=1)
    if low != 0:
        Label(bill_root, font=15, text="Premium | ₹170").grid(row=1, sticky=W)
        Label(bill_root, font=15, text=low).grid(row=1, column=1)
    Label(bill_root, font=15, text=f'{seatprice:.2f}').grid(row=1, column=2)
    # addons
    if int(extras[0]) != 0:
        Label(bill_root, font=15, text="Popcorn Large | ₹200").grid(row=2, sticky=W)
        Label(bill_root, font=15, text=int(extras[0])).grid(row=2, column=1)
        Label(bill_root, font=15, text=f'{int(extras[0]) * 200:.2f}').grid(row=2, column=2)

    if int(extras[1]) != 0:
        Label(bill_root, font=15, text="Popcorn Small | ₹120").grid(row=3, sticky=W)
        Label(bill_root, font=15, text=int(extras[1])).grid(row=3, column=1)
        Label(bill_root, font=15, text=f'{int(extras[1]) * 120:.2f}').grid(row=3, column=2)

    if int(extras[2]) != 0:
        Label(bill_root, font=15, text="Coke Large | ₹150").grid(row=4, sticky=W)
        Label(bill_root, font=15, text=int(extras[2])).grid(row=4, column=1)
        Label(bill_root, font=15, text=f'{int(extras[2]) * 150:.2f}').grid(row=4, column=2)

    if int(extras[3]) != 0:
        Label(bill_root, font=15, text="Coke Small | ₹80").grid(row=5, sticky=W)
        Label(bill_root, font=15, text=int(extras[3])).grid(row=5, column=1)
        Label(bill_root, font=15, text=f'{int(extras[3]) * 80:.2f}').grid(row=5, column=2)

    subtotal = seatprice + addonsprice
    tax = subtotal * 0.18
    total = tax + subtotal
    tax = f'{tax:.2f}'
    subtotal = f'{subtotal:.2f}'
    total = f'{total:.2f}'
    seatprice = seatprice * 1.18
    addonsprice = addonsprice * 1.18
    seatprice = f'{seatprice:.2f}'
    addonsprice = f'{addonsprice:.2f}'
    Label(bill_root, font=15, text="Sub-Total").grid(row=6, pady=5, sticky=E)
    Label(bill_root, font=15, text=subtotal).grid(row=6, column=2)
    Label(bill_root, font=15, text="Tax").grid(row=7, sticky=E)
    Label(bill_root, font=15, text=tax).grid(row=7, column=2)
    Label(bill_root, font=15, text="Total").grid(row=8, sticky=E)
    Label(bill_root, font=15, text=total).grid(row=8, column=2)

    Button(bill_root, text="Proceed to Pay", font=20, command=click).grid(row=9, columnspan=3, pady=10)

    f.write('\n' + total)
    f.write('\n' + seatprice)
    f.write('\n' + addonsprice)
    f.close()
    bill_root.resizable(False, False)
    bill_root.mainloop()

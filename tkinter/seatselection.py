from tkinter import *
seat_root = Tk()
seat_root.title("Select seats")
seat_selected = ["\n"]


def seats():
    seats_array1 = [
        [" ", "  1", "  2", "  3", "  ", "  4", "  5", "  6", "  7", "  8", "  9", "  10", "  11", "  12", "  ", "  13", "  14", "  15"],
        ["A", "A1D", "A2D", "A3D", "  ", " A4", " A5", " A6", " A7", " A8", " A9", " A10", "A11D", "A12D", "  ", " A13", " A14", " A15"],
        ["B", " B1", " B2", " B3", "  ", " B4", "B5D", "B6D", "B7D", "B8D", " B9", " B10", " B11", " B12", "  ", "B13D", "B14D", " B15"],
        [" ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", " Rs", "250", "   ", "    ", "    ", "    ", "  ", "    ", "    ", "    "],
        ["C", " C1", "C2D", "C3D", "  ", " C4", " C5", " C6", "C7D", "C8D", "C9D", " C10", " C11", " C12", "  ", " C13", "C14D", "C15D"],
        ["D", " D1", " D2", " D3", "  ", " D4", " D5", " D6", " D7", " D8", " D9", " D10", " D11", " D12", "  ", " D13", " D14", " D15"],
        ["E", " E1", " E2", " E3", "  ", "E4D", "E5D", " E6", " E7", " E8", " E9", " E10", " E11", " E12", "  ", " E13", "E14D", "E15D"],
        ["F", " F1", " F2", " F3", "  ", " F4", " F5", " F6", " F7", " F8", " F9", "F10D", "F11D", "F12D", "  ", "F13D", "F14D", " F15"],
        ["G", "G1D", "G2D", "G3D", "  ", " G4", " G5", "G6D", "G7D", "G8D", " G9", " G10", " G11", " G12", "  ", " G13", " G14", " G15"],
        ["H", " H1", " H2", " H3", "  ", " H4", " H5", " H6", " H7", " H8", " H9", " H10", " H11", " H12", "  ", " H13", " H14", " H15"],
        [" ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", " Rs", "190", "   ", "    ", "    ", "    ", "  ", "    ", "    ", "    "],
        ["I", "I1D", "I2D", "I3D", "  ", " I4", "I5D", "I6D", " I7", " I8", " I9", "I10D", "I11D", "I12D", "  ", " I13", "I14D", "I15D"],
        ["J", " J1", " J2", " J3", "  ", " J4", " J5", "J6D", "J7D", "J8D", " J9", " J10", " J11", " J12", "  ", " J13", " J14", " J15"],
        [" ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", " Rs", "170", "   ", "    ", "    ", "    ", "  ", "    ", "    ", "    "]]

    def book_seat(i):
        seat_name = i.lstrip() + " "
        if i in seat_selected:
            seat_selected.remove(seat_name)
        else:
            seat_selected.append(seat_name)
        b = globals()[i].cget('bg')
        if b == "SystemButtonFace":
            globals()[i].configure(bg="#1ea83c")
        else:
            globals()[i].configure(bg="SystemButtonFace")

    def make_seat_button(row, column):
        globals()[seats_array1[row][column]] = Button(seat_root, command=lambda: book_seat(seats_array1[row][column]), height=1, width=2)
        globals()[seats_array1[row][column]].grid(row=row, column=column)
    def make_seat_label(row, column):
        globals()[seats_array1[row][column]] = Label(seat_root, text=(seats_array1[row][column]), height=1, width=2)
        globals()[seats_array1[row][column]].grid(row=row, column=column)
    def bookbutton():
        f1 = open("moviename.txt", 'a')
        seat_selected.sort()
        f1.writelines(seat_selected)
        f1.close()
        seat_root.destroy()
    for row in range(len(seats_array1)):
        for column in range(len(seats_array1[0])):
            a = seats_array1[row][column].lstrip()
            if (len(a) < 2) or a.isdigit() or a == "Rs":
                make_seat_label(row, column)
            else:
                make_seat_button(row, column)
                if a[-1] == "D":
                    globals()[seats_array1[row][column]].configure(state="disabled", bg="#b2beb5")
    Button(seat_root, command=bookbutton, text="Book Tickets", height=1, width=20, font=17).grid(row=15, column=5, columnspan=10)
    seat_root.resizable(False, False)
    seat_root.mainloop()

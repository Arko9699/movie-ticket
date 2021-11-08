from tkinter import *
from db_connector import *
hallroot = Tk()
hallroot.title("Select Hall and Timings")
db_con = createCon()


def takehall():
    f1 = open("moviename.txt", "r")
    mname = f1.readline().replace("\n", "")
    mlang = f1.readline().replace("\n", "")
    md = f1.readline().replace("\n", "")
    return mname, mlang, md


class HallTimings:
    def __init__(self, myresult, row, column, hall, time):
        self.myresult = myresult
        self.row = row
        self.column = column
        self.hall = hall
        self.time = time

    def makehalllabel(self):

        def click(hall, time):
            f1 = open("moviename.txt", 'a')
            f1.writelines("\n" + hall + "\n" + time)
            f1.close()
            hallroot.destroy()

        hall_label = Label(hallroot, text=self.hall, font=24)
        hall_label.grid(row=self.row, column=0, pady=20)
        time_btn1 = Button(hallroot, text=self.time, font=17, command=lambda: click(self.hall, self.time))
        time_btn1.grid(row=self.row, column=self.column, padx=10)


def hallobjects():
    mname, mlang, md = takehall()
    myresult = movieHallDetails(mname, mlang, md, db_con)
    a, b, c = 1, 1, 1
    for i in myresult:
        if i[0] == "Hiland Park":
            m1 = HallTimings(myresult, 0, a, i[0], i[1])
            m1.makehalllabel()
            a += 1
        elif i[0] == "Quest Mall":
            m1 = HallTimings(myresult, 1, b, i[0], i[1])
            m1.makehalllabel()
            b += 1
        else:
            m1 = HallTimings(myresult, 2, c, i[0], i[1])
            m1.makehalllabel()
            c += 1
    hallroot.resizable(False, False)
    hallroot.mainloop()
    closeCon(db_con)

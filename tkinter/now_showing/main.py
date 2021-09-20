from tkinter import *
from nowshowing import *
from now_showing import db_connector
from tkinter import ttk
db_con=db_connector.createCon()

nowshowingObject = movies()
nowshowing.rootinclass.mainloop()
if nowshowing.nowshowingbool == "True":
    New_Window = Tk()
    New_Window.title(nowshowing.movie_name)
    myresult = db_connector.movieDetails(nowshowing.movie_name, db_con)

    # Load image here
    # img = PhotoImage(file=movie_name + '.png')
    # Label(New_Window, image=img ).pack()
    def openHall(movie_n):
        print("Movie: " + movie_n)
        language = str(var.get())
        hallType = ""
        if (language == "English"):
            hallType = str(rbEng.get())
        else:
            hallType = str(rbHin.get())
        print("Language: " + language)
        print("Hall Type: " + hallType)

        Hall_Window = Tk()
        Hall_Window.title(movie_n)
        Label(Hall_Window, font=font_button, justify=LEFT, text="Select the Hall and Movie timing  ", width=100).pack(side=TOP, anchor="w")
        myresult = db_connector.movieHallDetails(movie_n, language, hallType, db_con)
        rbHall = StringVar(Hall_Window, "")
        cbTime = StringVar(Hall_Window, "")
        cbHilandPark = ""
        cbQuestMall = ""
        cbSouthCityMall = ""
        hallName = ""
        for row in myresult:

            if (hallName != row[0]):
                Halloptions = [""]
                hallName = row[0]

                for row_time in myresult:
                    if (hallName == row_time[0]):
                        Halloptions.append(row_time[1])
                rbHall.set(hallName)
                Radiobutton(Hall_Window, text=row[0], variable=rbHall, value=row[0], height=1, font=font_button, ).pack(side=TOP, anchor="w")
                labelTop = Label(Hall_Window, text="Choose your Time ").pack()

                if hallName == "Hiland Park":
                    comboHall = ttk.Combobox(Hall_Window, textvariable=cbHilandPark)
                    comboHall['values'] = Halloptions
                    comboHall.pack()
                if hallName == "Quest Mall":
                    comboHall = ttk.Combobox(Hall_Window, textvariable=cbQuestMall)
                    comboHall['values'] = Halloptions
                    comboHall.pack()
                if hallName == "South City Mall":
                    comboHall = ttk.Combobox(Hall_Window, textvariable=cbSouthCityMall)
                    comboHall['values'] = Halloptions
                    comboHall.pack()

        Button(Hall_Window, text="Book Ticket", font=font_button).pack(side=TOP, anchor="w")
        New_Window.destroy()
        Hall_Window.mainloop()

    def selectRadio():
        selection = "You selected the option " + str(var.get())
        print(selection)

    font_button = font.Font(size=10, weight='bold', family='Helvetica')
    for row in myresult:
        Label(New_Window, font=font_button, justify=LEFT, text="Synopsis : ").pack(side=TOP, anchor="w")
        text_box = Text(New_Window, height=5)
        text_box.pack(expand=True, side=TOP, anchor="w")
        text_box.insert('end', row[0])
        Label(New_Window, font=font_button, justify=LEFT, text="Category : ").pack(side=TOP, anchor="w")
        text_box = Text(New_Window, height=1)
        text_box.pack(expand=True, side=TOP, anchor="w")
        text_box.insert('end', row[1])
        Label(New_Window, font=font_button, justify=LEFT, text="Duration : ").pack(side=TOP, anchor="w")
        text_box = Text(New_Window, height=1)
        text_box.pack(expand=True, side=TOP, anchor="w")
        text_box.insert('end', row[2])
        Label(New_Window, font=font_button, justify=LEFT, text="Rating : ").pack(side=TOP, anchor="w")
        text_box = Text(New_Window, height=1)
        text_box.pack(expand=True, side=TOP, anchor="w")
        text_box.insert('end', row[3])

    var = StringVar(New_Window, "English")
    var_eng = StringVar()
    var_hin = StringVar()
    var_eng.set(0)
    var_hin.set(0)

    mylangresult = db_connector.movieLangDetails(nowshowing.movie_name, db_con)
    lang = ""
    rbEng = StringVar(New_Window, "")
    rbHin = StringVar(New_Window, "")
    for row in mylangresult:
        if (lang != row[0]):
            lang = row[0]
            options = [""]
            for row1 in mylangresult:
                dt = row1[1]
                if (lang == row1[0]):
                    options.append(dt)
            rbl = Radiobutton(New_Window, text=row[0], variable=var, value=row[0], height=1, font=font_button, command=selectRadio).pack(side=TOP, anchor="w")
            labelTop = Label(New_Window, text="Choose your Hall Type").pack()
            if (lang == "English"):
                comboEng = ttk.Combobox(New_Window, textvariable=rbEng)
                comboEng['values'] = options
                comboEng.pack()
            else:
                comboExample = ttk.Combobox(New_Window, textvariable=rbHin)
                comboExample['values'] = options
                comboExample.pack()

    image_btn = Button(New_Window, text="Go to Hall", command=lambda: openHall(nowshowing.movie_name), font=font_button).pack(side=TOP, anchor="w")
    New_Window.mainloop()
db_con.close()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from os import system
from tkinter.font import BOLD
import sv_ttk
import mysql.connector as sequal

try:
    o = open("mysqlpass.txt")
    o.close()
except:
    with open("mysqlpass.txt", "w") as file:
        file.close()
try:
    with open("theme.txt", "r") as x:
        y = x.readline()
        mode = y
except:
    with open("theme.txt", "w") as x:
        mode = "light"
        x.write(mode)


def themechose():
    global theme
    theme = Toplevel()
    theme.title("choose theme:-")
    theme.resizable(0, 0)
    app_width = 256
    app_height = 128
    screenwidth = theme.winfo_screenwidth()
    screenheight = theme.winfo_screenheight()

    x = (screenwidth / 2) - (app_width / 2)
    y = (screenheight / 2) - (app_height / 2)

    theme.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    light_button = ttk.Button(
        theme, text="LIGHT", command=lambda: [light(), theme.destroy()]
    )
    light_button.place(relx=0.20, rely=0.5)
    dark_button = ttk.Button(
        theme, text="DARK", command=lambda: [dark(), theme.destroy()]
    )
    dark_button.place(relx=0.55, rely=0.5)

    theme.mainloop()


def dark():
    global mode
    mode = "dark"
    with open("theme.txt", "w") as x:
        x.write(mode)
    sv_ttk.set_theme("dark")


def light():
    global mode
    mode = "light"
    with open("theme.txt", "w") as x:
        x.write(mode)
    sv_ttk.set_theme("light")


# creating life
life = 3
# opening a window

root = Tk()
root.title("Higher Lower")
sv_ttk.set_theme(mode)
root.resizable(0, 0)


def mysqlpassget():
    root.withdraw()
    global sql
    sql = Toplevel()
    sql.title("Enter mysql password :-")
    app_width = 512
    app_height = 256
    screenwidth = sql.winfo_screenwidth()
    screenheight = sql.winfo_screenheight()

    x = (screenwidth / 2) - (app_width / 2)
    y = (screenheight / 2) - (app_height / 2)

    sql.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    def savepass(*e):
        global mysql_password
        try:
            mysql_password = sequalpass.get()
            mydb = sequal.connect(
                host="localhost",
                user="root",
                passwd=mysql_password,
            )
            v1 = open("mysqlpass.txt", "w")
            v1.write(mysql_password)
            v1.flush()
            v1.close()
            sql.destroy()
            system("python main.py")

        except:
            messagebox.showerror("Authentication Error", "Wrong MYSQL Password!!")
            sequalpass.delete(0, END)
    sequal_lbl = ttk.Label(sql, text="Enter your MySQL Password: ", font=("",14, BOLD))
    sequalpass = ttk.Entry(sql)
    sequalpass.config(show="•")
    sequal_lbl.place(x=25, y=110)
    sequalpass.place(x=310, y=108)

    def show(mypass, sequalpass):
        if (mypass.get()) == 1:
            sequalpass.config(show="")
        else:
            sequalpass.config(show="•")

    mypass = IntVar()

    checkshow = ttk.Checkbutton(
        sql,
        text="Show Password",
        variable=mypass,
        onvalue=1,
        offvalue=0,
        command=lambda: [show(mypass, sequalpass)],
    )
    checkshow.place(x=310, y=150)

    sql_button = ttk.Button(sql, text="Save", padding=10, command=lambda: [savepass()])
    sql_button.place(x=220, y=180)

    sequalpass.bind("<Return>", savepass)

    sql.mainloop()


with open("mysqlpass.txt", "r") as x:
    y = x.read()
    try:
        db = sequal.connect(host="localhost", user="root", passwd=y)
        cur = db.cursor()
    except sequal.Error:
        mysqlpassget()
    x.close()

cur = db.cursor()
cur.execute("SHOW SCHEMAS;")
databases = []
for i in cur:
    databases.extend(i)

databasename = "highlowgame"

if databasename in databases:
    cur.execute(" USE {} ;".format(databasename))
else:
    cur.execute("CREATE DATABASE {};".format(databasename))
    cur.execute(" USE {} ;".format(databasename))

cur.execute("SHOW TABLES;")
tables = []
for i in cur:
    tables.extend(i)
cur.execute("USE {};".format(databasename))
cur.execute(
    "CREATE TABLE if not exists accounts(playername varchar(20),highscore varchar(20));"
)
db.commit()

# function for the main program


def main_page(*e):
    global life, playername
    playername = name_ent.get()
    root.withdraw()
    pcard = Toplevel()
    pcard.resizable(0, 0)

    pcard.title("Higher Lower")

    # fixing window properties
    pcard.geometry("460x550")
    pcard.resizable(0, 0)

    # defining the images
    clove = PhotoImage(file="images//clove.png")
    diamond = PhotoImage(file="images//diamond.png")
    spade = PhotoImage(file="images//spade.png")
    heart = PhotoImage(file="images//heart.png")

    ls = [clove, diamond, spade, heart]
    lsd = {
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    lsl = list(lsd.keys())
    img = random.choice(ls)
    num = random.choice(lsl)

    # creating higher function
    def higher(*e):
        global life
        old = lsd[number["text"]]
        # randomizing the image
        img1 = random.choice(ls)
        num1 = random.choice(lsl)

        number.config(text=num1)
        main_lbl.config(image=img1)
        new = lsd[number["text"]]

        scr = your_score_lbl["text"]
        yhs = your_high_score_lbl["text"]

        if old < new:
            scr = int(scr) + 1
            your_score_lbl.config(text=scr)

        elif old == new:
            scr = your_score_lbl["text"]
            scr = int(scr) + 1
            your_score_lbl.config(text=scr)

        else:
            life -= 1
            life_lbl.config(text=life * "🖤")
            if life == 0:
                score = your_score_lbl["text"]
                cur.execute(f"SELECT * FROM accounts WHERE playername = '{playername}'")
                l = cur.fetchall()
                hscore = l[0][1]
                if int(score) > int(hscore):
                    cur.execute(
                        f"UPDATE accounts SET highscore={int(score)} WHERE playername = '{playername}'"
                    )
                    db.commit()
                    your_high_score_lbl.config(text=str(score))

                messagebox.showinfo("", "LOST!!")
                pcard.destroy()

                system("python main.py")

        try:
            if int(yhs) < int(scr):
                yhs = int(yhs) + 1
                your_high_score_lbl.config(text=yhs)
        except:
            yhs = 1
            your_high_score_lbl.config(text=yhs)

    def lower(*e):
        global life

        old = lsd[number["text"]]
        # randomizing
        img1 = random.choice(ls)
        num1 = random.choice(lsl)

        number.config(text=num1)
        main_lbl.config(image=img1)
        new = lsd[number["text"]]

        scr = your_score_lbl["text"]
        yhs = your_high_score_lbl["text"]

        if old > new:
            scr = int(scr) + 1
            your_score_lbl.config(text=scr)

        elif old == new:
            scr = int(scr) + 1
            your_score_lbl.config(text=scr)

        else:
            life -= 1
            life_lbl.config(text=life * "🖤")
            if life == 0:
                score = your_score_lbl["text"]
                cur.execute(f"SELECT * FROM accounts WHERE playername = '{playername}'")
                l = cur.fetchall()
                hscore = l[0][1]
                if int(score) > int(hscore):
                    cur.execute(
                        f"UPDATE accounts SET highscore={int(score)} WHERE playername = '{playername}'"
                    )
                    db.commit()
                    your_high_score_lbl.config(text=str(score))

                messagebox.showinfo("", "LOST!!")
                pcard.destroy()
                system("python main.py")

        try:
            if int(yhs) < int(scr):
                yhs = int(yhs) + 1
                your_high_score_lbl.config(text=yhs)
        except:
            yhs = 1
            your_high_score_lbl.config(text=yhs)

    # main window widgets
    try:
        cur.execute(f"SELECT * FROM accounts WHERE playername = '{playername}'")
        yhs = (cur.fetchall())[0][1]
        cur.execute(f"SELECT highscore FROM accounts")
        sls = []
        for i in cur:
            sls.append(i[0])
        hs = sls[0]
        for i in sls:
            if int(i) > int(hs):
                hs =i

    except:
        cur.execute(f"INSERT INTO accounts VALUES('{playername}',0)")
        db.commit()
        yhs = 0
        cur.execute(f"SELECT highscore FROM accounts")
        sls = []
        for i in cur:
            sls.append(i[0])
        hs = sls[0]
        for i in sls:
            if int(i) > int(hs):
                hs = i

    main_lbl = Label(pcard, image=img)
    life_lbl = Label(pcard, text=(life * "🖤"), font=("", 25))  #'❤️'
    higher_btn = ttk.Button(pcard, text="HIGHER", command=higher)

    chk_btn = ttk.Button(pcard, text="Theme", command=lambda: themechose())
    chk_btn.place(relx=0.75, rely=0.02)

    lower_btn = ttk.Button(pcard, text="LOWER", command=lower)
    high_lbl = ttk.Label(pcard, text="HIGH SCORE")
    your_high_lbl = ttk.Label(pcard, text="YOUR HIGH SCORE")

    your_high_score_lbl = ttk.Label(pcard, width=3, font=("", 12))
    high_score_lbl = ttk.Label(pcard, width=3, font=("", 12))
    your_lbl = ttk.Label(pcard, text="YOUR SCORE")

    your_score_lbl = ttk.Label(pcard, width=3, font=("", 12))
    your_high_score_lbl.config(text=yhs)
    high_score_lbl.config(text=hs)
    your_score_lbl.config(text=0)

    number = Label(pcard, text=num, font=("", 50), bg="#FFFFFF", fg="#000000")

    life_lbl.place(relx=0, rely=0)
    main_lbl.place(relx=0, rely=0.04)

    higher_btn.place(relx=0.1, rely=0.88)
    lower_btn.place(relx=0.4, rely=0.88)
    number.place(relx=0.18, rely=0.15)

    high_lbl.place(relx=0.73, rely=0.1)
    high_score_lbl.place(relx=0.73, rely=0.15)
    your_high_lbl.place(relx=0.73, rely=0.4)
    your_high_score_lbl.place(relx=0.73, rely=0.45)
    your_lbl.place(relx=0.73, rely=0.7)
    your_score_lbl.place(relx=0.73, rely=0.75)

    pcard.bind("<Up>", higher)
    pcard.bind("<Down>", lower)

    pcard.mainloop()


name_lbl = ttk.Label(root, text="Name: ", anchor=CENTER, font=("", 14))
name_ent = ttk.Entry(root, font=("", 14))

continue_btn = ttk.Button(root, text="Continue", command=main_page)
exit_btn = ttk.Button(root, text="Exit", command=lambda: [root.quit()])

name_lbl.grid(row=0, column=0, padx=10, pady=10)
name_ent.grid(row=0, column=1, padx=10, pady=10)

name_ent.bind("<Return>", main_page)

continue_btn.grid(row=1, column=1, padx=10, pady=10)
exit_btn.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
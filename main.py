from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import os

try:
    with open('highscore.txt', 'r') as f:
        pass
except:
    with open('highscore.txt', 'w') as f:
        pass
 
root = Tk()
root.title("Higher Lower")

def main_page():
    username=name_ent.get()
    root.destroy()
    pcard = Tk()

    pcard.geometry('460x550')
    pcard.resizable(0,0)

    clove = PhotoImage(file="images//clove.png")
    diamond = PhotoImage(file="images//diamond.png")
    spade =PhotoImage(file="images//spade.png")
    heart = PhotoImage(file="images//heart.png")

    ls = [clove, diamond, spade, heart]
    img = random.choice(ls)
    
    def higher():
        old = lsd[number['text']]
        img1 = random.choice(ls)
        num1 = random.choice(lsl)
        number.config(text=num1)
        main_lbl.config(image=img1)
        new = lsd[number['text']]
        if old < new:
            your_score_lbl.config(state=ACTIVE)
            scr = your_score_lbl.get()

            if scr == '-':
                your_score_lbl.delete(0, END)
                your_score_lbl.insert(0,'1')
            else:
                your_score_lbl.delete(0,END)
                your_score_lbl.insert(0,int(scr)+1)
        elif old == new:
            your_score_lbl.config(state=ACTIVE)
            scr = your_score_lbl.get()
            your_score_lbl.delete(0,END)
            your_score_lbl.insert(0,int(scr)+1)
        else:
            messagebox.showinfo("Get out idiot", "LOOSERRR!!")
            pcard.destroy()
            os.system("python main.py")
        try:
            your_score_lbl.config(state=DISABLED)
        except:
            pass
    
    def lower():
        old = lsd[number['text']]
        img1 = random.choice(ls)
        num1 = random.choice(lsl)
        number.config(text=num1)
        main_lbl.config(image=img1)
        new = lsd[number['text']]
        if old > new:
            your_score_lbl.config(state=ACTIVE)
            scr = your_score_lbl.get()

            if scr == '-':
                your_score_lbl.delete(0, END)
                your_score_lbl.insert(0,'1')
            else:
                your_score_lbl.delete(0,END)
                your_score_lbl.insert(0,int(scr)+1)
        elif old == new:
            your_score_lbl.config(state=ACTIVE)
            scr = your_score_lbl.get()
            your_score_lbl.delete(0,END)
            your_score_lbl.insert(0,int(scr)+1)
        else:
            messagebox.showinfo("Get out idiot", "LOOSERRR!!")
            pcard.destroy()
            os.system("python main.py")
        try:
            your_score_lbl.config(state=DISABLED)
        except:
            pass

    lsd={2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':11, 'Q':12, 'K':13, 'A':14}
    lsl= list(lsd.keys())
    num = random.choice(lsl)

    main_lbl = Label(pcard, image=img)
    higher_btn = ttk.Button(pcard, text="HIGHER", command=higher)
    lower_btn = ttk.Button(pcard, text="LOWER", command=lower)
    high_lbl = ttk.Label(pcard, text='HIGH SCORE' )
    high_score_lbl = ttk.Entry(pcard, width=3, font=("",12))
    your_lbl = ttk.Label(pcard, text='YOUR SCORE')
    your_score_lbl = ttk.Entry(pcard, width=3, font=("",12))
    high_score_lbl.insert(0,'-')
    your_score_lbl.insert(0,'-')
    high_score_lbl.config(state=DISABLED)
    your_score_lbl.config(state=DISABLED)
    number = Label(pcard, text=num, font=("", 50))

    main_lbl.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    higher_btn.grid(row=1, column=0, padx=10, pady=10)
    lower_btn.grid(row=1, column=1, padx=10, pady=10)
    high_lbl.place(relx=0.79, rely=0.1)
    high_score_lbl.place(relx=0.79, rely=0.15)
    your_lbl.place(relx=0.79, rely=0.4)
    your_score_lbl.place(relx=0.79, rely=0.45)
    number.place(relx=0.185, rely=0.15)

    your_score_lbl.config(state=ACTIVE)
    score = your_score_lbl.get()
    your_score_lbl.config(state=DISABLED)

    with open('highscore.txt', 'r+') as file:
        if file.read() == "":
            file.write(f'[{username},{score}]')
        else:
            print(file.read())
    
    pcard.mainloop()

name_lbl = ttk.Label(root, text="Name: ", anchor=CENTER, font=("",14))
name_ent = ttk.Entry(root, font=("", 14))
continue_btn = ttk.Button(root, text="Continue", command=main_page)

name_lbl.grid(row=0, column=0, padx=10, pady=10)
name_ent.grid(row=0, column=1, padx=10, pady=10)
continue_btn.grid(row=1, column=0, padx=10, pady=10, columnspan=2)


root.mainloop()
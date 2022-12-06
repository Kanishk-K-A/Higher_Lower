from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()
root.title("Higher Lower")

def main_page():
    root.destroy()
    pcard = Tk()

    pcard.geometry('460x550')
    pcard.resizable(0,0)

    C2 = PhotoImage(file="images//clove 2.png")
    C3 = PhotoImage(file="images//clove 3.png")
    C4 = PhotoImage(file="images//clove 4.png")
    C5 = PhotoImage(file="images//clove 5.png")
    C6 = PhotoImage(file="images//clove 6.png")
    C7 = PhotoImage(file="images//clove 7.png")
    C8 = PhotoImage(file="images//clove 8.png")
    C9 = PhotoImage(file="images//clove 9.png")
    C10 = PhotoImage(file="images//clove 10.png")
    CJ = PhotoImage(file="images//clove J.png")
    CQ = PhotoImage(file="images//clove Q.png")
    CK = PhotoImage(file="images//clove K.png")
    CA = PhotoImage(file="images//clove A.png")

    D2 = PhotoImage(file="images//diamond 2.png")
    D3 = PhotoImage(file="images//diamond 3.png")
    D4 = PhotoImage(file="images//diamond 4.png")
    D5 = PhotoImage(file="images//diamond 5.png")
    D6 = PhotoImage(file="images//diamond 6.png")
    D7 = PhotoImage(file="images//diamond 7.png")
    D8 = PhotoImage(file="images//diamond 8.png")
    D9 = PhotoImage(file="images//diamond 9.png")
    D10 = PhotoImage(file="images//diamond 10.png")
    DJ = PhotoImage(file="images//diamond J.png")
    DQ = PhotoImage(file="images//diamond Q.png")
    DK = PhotoImage(file="images//diamond K.png")
    DA = PhotoImage(file="images//diamond A.png")

    H2 = PhotoImage(file="images//heart 2.png")
    H3 = PhotoImage(file="images//heart 3.png")
    H4 = PhotoImage(file="images//heart 4.png")
    H5 = PhotoImage(file="images//heart 5.png")
    H6 = PhotoImage(file="images//heart 6.png")
    H7 = PhotoImage(file="images//heart 7.png")
    H8 = PhotoImage(file="images//heart 8.png")
    H9 = PhotoImage(file="images//heart 9.png")
    H10 = PhotoImage(file="images//heart 10.png")
    HJ = PhotoImage(file="images//heart J.png")
    HQ = PhotoImage(file="images//heart Q.png")
    HK = PhotoImage(file="images//heart K.png")
    HA = PhotoImage(file="images//heart A.png")

    S2 = PhotoImage(file="images//spade 2.png")
    S3 = PhotoImage(file="images//spade 3.png")
    S4 = PhotoImage(file="images//spade 4.png")
    S5 = PhotoImage(file="images//spade 5.png")
    S6 = PhotoImage(file="images//spade 6.png")
    S7 = PhotoImage(file="images//spade 7.png")
    S8 = PhotoImage(file="images//spade 8.png")
    S9 = PhotoImage(file="images//spade 9.png")
    S10 = PhotoImage(file="images//spade 10.png")
    SJ = PhotoImage(file="images//spade J.png")
    SQ = PhotoImage(file="images//spade Q.png")
    SK = PhotoImage(file="images//spade K.png")
    SA = PhotoImage(file="images//spade A.png")

    ls = [C2,C3,C4,C5,C6,C7,C8,C9,C10,CJ,CQ,CK,CA,D2,D3,D4,D5,D6,D7,D8,D9,D10,DJ,DQ,DK,DA,H2,H3,H4,H5,H6,H7,H8,H9,H10,HJ,HQ,HK,HA,S2,S3,S4,S5,S6,S7,S8,S9,S10,SJ,SQ,SK,SA]
    lsq = ['C2','C3','C4','C5','C6','C7','C8','C9','C10','CA','CJ','CK','CQ','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DK','DQ','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HK','HQ','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SK','SQ']
    d = {1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14,
        14:2,15:3,16:4,17:5,18:6,19:7,20:8,21:9,22:10,23:11,24:12,25:13,26:14,
        27:2,28:3,29:4,30:5,31:6,32:7,33:8,34:9,35:10,36:11,37:12,38:13,39:14,
        40:2,41:3,42:4,43:5,44:6,45:7,46:8,47:9,48:10,49:11,50:12,51:13,52:14,}
    #ls = [C2,C3,C4,C5]
    img = C2
    
    def higher():
        o_card = int((str(img)[7:]))
        img1 = random.choice(ls)
        main_lbl.config(image=img1)
        n_card = int((str(img1)[7:]))
        #print(d[o_card])
        #print(d[n_card])
        #print()
        if d[o_card] < d[n_card]:
            print("Correct")
        else:
            print("Wrong") 

        
    def lower():
        img = random.choice(ls)
        main_lbl.config(image=img)


    main_lbl = Label(pcard, image=img)
    higher_btn = ttk.Button(pcard, text="HIGHER", command=higher)
    lower_btn = ttk.Button(pcard, text="LOWER", command=lower)
    high_lbl = ttk.Label(pcard, text='HIGH SCORE' )
    high_score_lbl = ttk.Entry(pcard, width=3, font=("",12))
    your_lbl = ttk.Label(pcard, text='YOUR SCORE')
    your_score_lbl = ttk.Entry(pcard, width=3, font=("",12))
    high_score_lbl.insert(0,'12')
    your_score_lbl.insert(0,'12')
    high_score_lbl.config(state=DISABLED)
    your_score_lbl.config(state=DISABLED)

    main_lbl.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    higher_btn.grid(row=1, column=0, padx=10, pady=10)
    lower_btn.grid(row=1, column=1, padx=10, pady=10)
    high_lbl.place(relx=0.79, rely=0.1)
    high_score_lbl.place(relx=0.79, rely=0.15)
    your_lbl.place(relx=0.79, rely=0.4)
    your_score_lbl.place(relx=0.79, rely=0.45)
    pcard.mainloop()

name_lbl = ttk.Label(root, text="Name: ", anchor=CENTER, font=("",14))
name_ent = ttk.Entry(root, font=("", 14))
continue_btn = ttk.Button(root, text="Continue", command=main_page)

name_lbl.grid(row=0, column=0, padx=10, pady=10)
name_ent.grid(row=0, column=1, padx=10, pady=10)
continue_btn.grid(row=1, column=0, padx=10, pady=10, columnspan=2)


root.mainloop()
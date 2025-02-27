from tkinter import *
from random import randint, sample

def str_to_lst(string):
    lst = []
    for i in range(4):
        lst.append(int(string[i]))
    return lst

def random_nb():
    return sample(range(0, 10), 4)


def reset_game():
    global rep, attempt
    rep = random_nb()
    attempt = 0
    for widget in result_frame.winfo_children():
        widget.destroy()
    red_label.config(text="")
    green_label.config(text="")
    bouton_test.config(state=NORMAL)
    replay_button.pack_forget()
    entree.delete(0, END)

rep = random_nb()
attempt = 0

fenetre = Tk()

fenetre.title("Chiffrus")

canvas = Canvas(fenetre, width=150, height=50)
canvas.pack()

entree = Entry(fenetre, width=30)
entree.pack()


def chiffrus():
    global attempt
    entr = str_to_lst(entree.get())
    if len(entr) != 4:
        red_label.config(text="Veuillez entrer exactement 4 chiffres.")
        return
    aff = []
    for i in range(4):
        if entr[i] == rep[i]:
            aff.append('green')
        elif entr[i] in rep:
            aff.append('orange')
        else:
            aff.append('white')
    group_frame = Frame(result_frame)
    group_frame.pack(padx=5, pady=5, anchor="w")
        
    for i in range(4):
        Label(group_frame, text=str(entr[i]), fg=aff[i], font=("Helvetica", 16)).pack(side=LEFT, padx=5)
    
    attempt += 1

    if entr == rep:
        green_label.config(text="GAGNÉ")
        bouton_test.config(state=DISABLED)
        replay_button.pack(padx=5, pady=5)
    elif attempt == 5:
        red_label.config(text="PERDU")
        bouton_test.config(state=DISABLED)
        replay_button.pack(padx=5, pady=5)

bouton_test = Button(fenetre, text='Tester', command=chiffrus)
bouton_test.pack(side=TOP, padx=5, pady=5)

replay_button = Button(fenetre, text="Rejouer", command=reset_game)
        
red_label = Label(fenetre, text="", fg="red")
red_label.pack(padx=10, pady=10)

green_label = Label(fenetre, text="", fg="green")
green_label.pack(padx=10, pady=10)

result_frame = Frame(fenetre)
result_frame.pack(padx=10, pady=10)

width= fenetre.winfo_screenwidth() 
height= fenetre.winfo_screenheight()
fenetre.geometry("%dx%d" % (width, height))

fenetre.mainloop()

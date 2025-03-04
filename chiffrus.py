from tkinter import *
from random import randint, sample

def str_to_lst(string):
    lst = []
    for i in range(6):
        lst.append(int(string[i]))
    return lst

def random_nb():
    rd = []
    for i in range(6):
        rd.append(randint(1, 10))
    return rd


def reset_game():
    global rep, attempt
    rep = random_nb()
    attempt = 0
    for widget in result_frame.winfo_children():
        widget.destroy()
    red_text.config(text="")
    green_text.config(text="")
    button_test.config(state=NORMAL)
    replay_button.pack_forget()
    enter.delete(0, END)

rep = random_nb()

attempt = 0

window = Tk()

window.title("Chiffrus")

canvas = Canvas(window, width=150, height=50)
canvas.pack()

enter = Entry(window)
enter.pack()


def chiffrus():
    global attempt
    if len(enter.get()) != 6:
        red_text.config(text="Please enter a 6 numbers.")
        return
    entr = str_to_lst(enter.get())
    colors = ['black','black','black','black','black','black']
    studied = []
    for i in range(6):
        if entr[i] == rep[i]:
            colors[i] = 'green'
            studied.append(entr[i])
    for i in range(6):
        too_much = True
        nb_in_rep = 0
        nb_in_nbs = 0
        for j in range(6):
            if entr[i] == rep[j]:
                nb_in_rep += 1
            if entr[i] == entr[j]:
                nb_in_nbs += 1
        if nb_in_rep <= nb_in_nbs:
            too_much = False
        if entr[i] in rep and too_much:
            colors[i] = 'orange'
            studied.append(entr[i])
    group_frame = Frame(result_frame)
    group_frame.pack(padx=5, pady=5, anchor="w")
        
    for i in range(6):
        Label(group_frame, text=str(entr[i]), fg=colors[i], font=('Helvetica', 24)).pack(side=LEFT, padx=5)
    
    attempt += 1

    if entr == rep:
        green_text.config(text="You won!")
        button_test.config(state=DISABLED)
        replay_button.pack(padx=5, pady=5)
    elif attempt == 5:
        red_text.config(text="You lost!")
        button_test.config(state=DISABLED)
        replay_button.pack(padx=5, pady=5)

button_test = Button(window, text='Test this numbers', command=chiffrus)
button_test.pack(side=TOP, padx=5, pady=5)

replay_button = Button(window, text="Replay", command=reset_game)

red_text = Label(window, text="", fg="red", font=('Helvetica', 24))
red_text.pack(padx=10, pady=10)

green_text = Label(window, text="", fg="green", font=('Helvetica', 24))
green_text.pack(padx=10, pady=10)

result_frame = Frame(window)
result_frame.pack(padx=10, pady=10)

width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

window.mainloop()

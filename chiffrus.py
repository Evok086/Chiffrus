from tkinter import *
from random import randint

def str_to_lst(string):
    lst = []
    for i in range(6):
        lst.append(int(string[i]))
    return lst

def random_nb():
    rd = []
    for i in range(6):
        rd.append(randint(0, 9))
    return rd


def reset_game():
    global rep, attempt
    rep = random_nb()
    attempt = 0
    for widget in result_frame.winfo_children():
        widget.destroy()
    win_text = Label(window, text="", fg="green", font=('Helvetica', 24))
    win_text.pack(padx=10, pady=10)
    lost_text = Label(window, text="", fg="red", font=('Helvetica', 24))
    lost_text.pack(padx=10, pady=10)
    button_test.config(state=NORMAL)
    replay_button.pack_forget()
    enter.delete(0, END)

rep = random_nb()
print(rep)
attempt = 0

window = Tk()

bg = PhotoImage(file="chiffrus.png")

# Show image using label
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

window.title("Chiffrus")

enter = Entry(window)
enter.pack()

nb_nbs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    for j in range(6):
        if rep[j] == i:
            nb_nbs[i] += 1
print(nb_nbs)

def chiffrus():
    global attempt
    if len(enter.get()) != 6:
        test_text = Label(window, text="Please enter a 6 numbers.", fg="red", font=('Helvetica', 24))
        test_text.pack(padx=10, pady=10)
        return
    entr = str_to_lst(enter.get())
    colors = ['black','black','black','black','black','black']
    studied = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(6):
        if entr[i] == rep[i]:
            colors[i] = 'green'
            studied[i] += 1
    for i in range(6):
        y_or_n = True
        if studied[entr[i]] >= nb_nbs[entr[i]]:
            y_or_n = False
        if colors[i] != 'green' and entr[i] in rep and y_or_n:
            colors[i] = 'orange'
            studied.append(entr[i])

    group_frame = Frame(result_frame)
    group_frame.pack(padx=5, pady=5, anchor="w")
        
    for i in range(6):
        Label(group_frame, text=str(entr[i]), fg=colors[i], font=('Helvetica', 24)).pack(side=LEFT, padx=5)
    
    attempt += 1

    if entr == rep:
        win_text = Label(window, text="You won!", fg="green", font=('Helvetica', 24))
        win_text.pack(padx=10, pady=10)
        button_test.config(state=DISABLED)
        replay_button.pack(padx=5, pady=5)
    elif attempt == 6:
        lost_text = Label(window, text="You lost!", fg="red", font=('Helvetica', 24))
        lost_text.pack(padx=10, pady=10)
        button_test.config(state=DISABLED)
        replay_button.pack(padx=5, pady=5)

button_test = Button(window, text='Test this numbers', command=chiffrus)
button_test.pack(side=TOP, padx=5, pady=5)

replay_button = Button(window, text="Replay", command=reset_game)

result_frame = Frame(window)
result_frame.pack(padx=10, pady=10)

width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

window.mainloop()

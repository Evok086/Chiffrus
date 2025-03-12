from tkinter import *
from random import randint

attempt = 0
solution = []
nbs_solution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def game():
    global result_frame
    
    def str_to_lst(string):
        return [int(string[i]) for i in range(6)]

    def define_solution():
        global nbs_solution, solution
        solution = [randint(0, 9) for _ in range(6)]
        nbs_solution = [solution.count(i) for i in range(10)]

    def reset_game():
        global attempt
        define_solution()
        result_frame.update_idletasks()
        attempt = 0
        for widget in result_frame.winfo_children():
            widget.destroy()
        for widget in window.winfo_children():
            if isinstance(widget, Label) and widget['fg'] in ('green', 'red'):
                widget.destroy()
        button_test.config(state=NORMAL)
        replay_button.pack_forget()
        enter.delete(0, END)

    def define_colors(entr):
        global nbs_solution, solution
        colors = ['black', 'black', 'black', 'black', 'black', 'black']
        studied = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(6):
            if entr[i] == solution[i]:
                colors[i] = 'green'
                studied[entr[i]] += 1
        for i in range(6):
            y_or_n = True
            if studied[entr[i]] >= nbs_solution[entr[i]]:
                y_or_n = False
            if colors[i] != 'green' and entr[i] in solution and y_or_n:
                colors[i] = 'orange'
                studied[entr[i]] += 1
        return colors

    def show_results(entr, colors):
        result_frame.update_idletasks()
        group_frame = Frame(result_frame, bg="lightyellow")
        group_frame.pack(padx=5, pady=5, anchor="w")

        for i in range(6):
            Label(group_frame, text=str(entr[i]), fg=colors[i], font=('Helvetica', 24), bg="lightyellow").pack(side=LEFT,padx=5)

    def chiffrus():
        global attempt
        entr = str_to_lst(enter.get())
        if len(enter.get()) != 6:
            test_text = Label(window, text="Please enter 6 numbers.", fg="red", font=('Helvetica', 24),
                              bg="lightyellow")
            test_text.pack(padx=10, pady=10)
            return
        colors = define_colors(entr)
        show_results(entr, colors)
        win_or_lost(entr)
        attempt += 1

    def win_or_lost(entr):

        if entr == solution:
            win_text = Label(window, text="You won!", fg="green", font=('Helvetica', 24), bg="lightyellow")
            win_text.pack(padx=10, pady=10)
            button_test.config(state=DISABLED)
            replay_button.pack(padx=5, pady=5)
        elif attempt == 5:
            lost_text = Label(window, text="You lost!", fg="red", font=('Helvetica', 24), bg="lightyellow")
            lost_text.pack(padx=10, pady=10)
            button_test.config(state=DISABLED)
            replay_button.pack(padx=5, pady=5)


    rules_frame.destroy()
    enter = Entry(window,bg="lightyellow")
    enter.pack(pady=40)

    define_solution()

    button_test = Button(window, text='Test this numbers', command=chiffrus, bg="lightyellow")
    button_test.pack(side=TOP, padx=5, pady=5)
    
    result_frame = Frame(window, bg="lightyellow")
    result_frame.pack(padx=10, pady=10)

    replay_button = Button(window, text="Replay", command=reset_game, bg="lightyellow")

window = Tk()

window.configure(bg="lightyellow")

window.title("Chiffrus")


rules_frame = Frame(window, bg="lightyellow")
rules_frame.pack(padx=10, pady=20)

rules_text = """
Welcome to the game Chiffrus!

Rules:
1. Guess a combination of 6 numbers.
2. Each number is between 0 and 9 and a number can appear several times.
3. After each attempt:
- Green: Correct number in the correct position.
- Orange: Correct number in the wrong position.
- Black: Incorrect number.

You have 6 attempts. Good luck!
"""

rules_label = Label(rules_frame, text=rules_text, font=('Helvetica', 14), bg="lightyellow", justify=LEFT)
rules_label.pack(padx=10, pady=10)

# Bouton pour masquer les règles et commencer
start_button = Button(rules_frame, text="OK", command=game, bg="lightyellow", font=('Helvetica', 12))
start_button.pack(pady=10)

result_frame = Frame(window, bg="lightyellow")
result_frame.pack(padx=10, pady=10)

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")

window.mainloop()

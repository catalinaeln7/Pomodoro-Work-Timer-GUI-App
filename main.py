from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    mark_label.config(text="")
    canvas.itemconfig(time_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps == 9:
        reps = 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN, 0)
        timer_label.config(fg=RED, text="Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN, 0)
        timer_label.config(fg=PINK, text="Break")
    else:
        count_down(WORK_MIN, 0)
        timer_label.config(fg=GREEN, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(mins, sec):
    if sec < 10:
        canvas.itemconfig(time_text, text=f"{mins}:0{sec}")
    else:
        canvas.itemconfig(time_text, text=f"{mins}:{sec}")
    if mins > 0 or sec > 0:
        global timer
        if sec > 0:
            timer = window.after(1000, count_down, mins, sec - 1)
        elif sec == 0:
            timer = window.after(1000, count_down, mins - 1, 59)
    else:
        start_timer()
        if reps % 2 == 0:
            text = ""
            for _ in range(0, int(reps / 2)):
                text += "✔"
            mark_label.config(text=text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Labels

timer_label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Canvas

canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
time_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons

start_button = Button(text="Start", fg="black", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", fg="black", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Green mark label

mark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "normal"))
mark_label.grid(row=3, column=1)

window.mainloop()

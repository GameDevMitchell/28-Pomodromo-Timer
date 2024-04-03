from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Calibri"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = ""
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)

    # set timer to 00:00
    canvas.itemconfig(timer_text, text="00:00")

    # change label to Timer
    timer_label.config(
        text="TIMER", font=("Arial rounded mt bold", 45), bg=YELLOW, fg=GREEN
    )

    # reset check marks
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 1st/3rd/5th/7th rep:
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(
            text="WORK", font=("Arial rounded mt bold", 45), bg=YELLOW, fg=GREEN
        )
        countdown(work_sec)

    # if it's the 8th rep:
    elif reps == 8:
        timer_label.config(
            text="BREAK", font=("Arial rounded mt bold", 45), bg=YELLOW, fg=RED
        )
        countdown(long_break_sec)

    # if it's the 2nd/4th/6th rep:
    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(
            text="BREAK", font=("Arial rounded mt bold", 45), bg=YELLOW, fg=PINK
        )
        countdown(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_secs = count % 60
    if count_secs == 0:
        count_secs = "00"
    elif int(count_secs) < 10 and count_secs != 0:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checkmark = "︎✅︎"
        if reps % 2 == 0:
            check.config(text=checkmark)
        if reps % 4 == 0:
            check.config(text=f"{checkmark}, {checkmark}")
        if reps % 6 == 0:
            check.config(text=f"{checkmark}, {checkmark}, {checkmark}")
        if reps % 8 == 0:
            check.config(text=f"{checkmark}, {checkmark}, {checkmark}, {checkmark}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(
    1000,
)

# the tomato setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="images/tomato.png")
canvas.create_image(100, 113, image=tomato)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=2, column=2)

# the timer text setup
timer_label = Label()
timer_label.config(
    text="TIMER", font=("Arial rounded mt bold", 45), bg=YELLOW, fg=GREEN
)
timer_label.grid(row=1, column=2)

# the start button
start = Button(command=start_timer)
start.config(text="Start", width=10, highlightthickness=0)
start.grid(row=3, column=1)

# the reset button
reset = Button(command=reset_timer)
reset.config(text="Reset", width=10, highlightthickness=0)
reset.grid(row=3, column=3)

# the checkmark label
check = Label()
check.config(bg=YELLOW, fg=GREEN)
check.grid(row=4, column=2)

window.mainloop()

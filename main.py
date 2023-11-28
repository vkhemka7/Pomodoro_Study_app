from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="✔")
    reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        reps += 1
        count_down(work_sec)
    elif reps % 2 == 0 and reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        reps += 1
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        reps += 1
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
       timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        tick_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME,35,'bold'))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(column=2, row=2)

tick_label = Label(text="✔", fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)


window.mainloop()
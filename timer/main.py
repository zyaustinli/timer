from tkinter import *
import time
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
reps=0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title.config(text = "Timer")
    check_marks.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break)
        title.config(text= "Break", fg = PINK)
    elif reps % 2 ==0:
        count_down(short_break)
        title.config(text= "Break", fg = PINK)

    else: 
        count_down(work_sec)
        title.config(text= "Work", fg = PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_seconds = count%60
    if count_seconds <10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_seconds}")
    if count>0:
        global timer
        timer = window.after(1000, count_down,count- 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✓"
        check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Snorlax Timer")
window.config(padx = 100, pady=50, bg=YELLOW)

title = Label(text = "Work", fg= PINK, bg = YELLOW, font = (FONT_NAME, 50))
title.grid(column=1, row =0)
canvas = Canvas(width= 300, height=242, bg = YELLOW, highlightthickness=0)
img= PhotoImage(file=r"C:\Users\liman\Downloads\My project.png" )
canvas.create_image(150, 121, image =img)
canvas.grid(column=1, row =1)
timer_text= canvas.create_text(150,115, text= "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))


start = Button(text = "start", highlightthickness=0, command = start_timer, bg = YELLOW)
start.grid(column=0, row=2)


reset = Button(text = "reset", highlightthickness=0, bg = YELLOW, command = reset_timer)
reset.grid(column=2, row = 2)

check_marks = Label(fg = GREEN, bg = YELLOW)
check_marks.grid(column=1, row=3)


    


window.mainloop()
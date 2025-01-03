import tkinter as tk
from config import *

reps = 0
timer = None

window = tk.Tk()
window.title("Pymodoro")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

def countdown(time_remaining):
    '''
    Countdown timer for the pomodoro. Calls itself every second until the timer is 0.

    Args:
        time_remaining (int): The number of seconds remaining.

    Returns:
        None
    '''

    minutes = time_remaining // 60
    if (minutes < 10):
        minutes = f"0{minutes}"
    seconds = time_remaining % 60
    if (seconds < 10):
        seconds = f"0{seconds}"
    time = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time)
    if time_remaining > 0:
        global timer
        timer = window.after(1000, countdown, time_remaining - 1)
    else:
        start_timer()
        checkmarks.config(text=f"✓" * (reps // 2))

def reset_timer():
    '''
    Resets the application to its initial state.

    Args:
        None

    Returns:
        None
    '''
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    header.config(text="Pymodoro!", fg="white")
    checkmarks.config(text="")  
    global reps
    reps = 0

def start_timer():
    '''
    Starts the pomodoro timer. Increments the reps counter and calls the countdown function
    passing the appropriate time based on the reps counter.

    Args:
        None

    Returns:
        None
    '''
    global reps
    reps += 1

    if (reps > 8):
        reset_timer()
    elif reps % 8 == 0:
        header.config(text="Break", fg="red")
        countdown(LONG_BREAK_SECONDS)
    elif reps % 2 == 0:
        header.config(text="Break", fg="yellow")
        countdown(SHORT_BREAK_SECONDS)
    else:
        header.config(text="Work", fg="green")
        countdown(WORK_SECONDS)

    window.lift()
    window.focus_force()

canvas = tk.Canvas(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
# chester = tk.PhotoImage(file="chester.png")
# chester.width = SCREEN_WIDTH / 4
# chester.height = SCREEN_HEIGHT / 4
# canvas.create_image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, image=chester)
timer_text = canvas.create_text(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, text="00:00", fill="white", font=(FONT_NAME, 96, "bold"))
canvas.grid(column=1, row=2)

header = tk.Label(text="Pymodoro!", fg="white", bg=BACKGROUND_COLOR, font=(FONT_NAME, 50, "bold"))
header.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0, font=(FONT_NAME, 20, "bold"), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = tk.Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 20, "bold"), command=reset_timer)
reset_button.grid(column=2, row=3)

checkmarks = tk.Label(fg="green", bg=BACKGROUND_COLOR, font=(FONT_NAME, 42, "bold"))
checkmarks.grid(column=1, row=4)

window.lift()
window.focus_force()
window.mainloop()

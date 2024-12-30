import tkinter as tk
from config import *

window = tk.Tk()
window.title("Pymodoro")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
# chester = tk.PhotoImage(file="chester.png")
# chester.width = SCREEN_WIDTH / 4
# chester.height = SCREEN_HEIGHT / 4
# canvas.create_image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, image=chester)
canvas.create_text(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

header = tk.Label(text="Timer", fg="white", bg=BACKGROUND_COLOR, font=(FONT_NAME, 50, "bold"))
header.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0, font=(FONT_NAME, 20, "bold"))
start_button.grid(column=0, row=3)

reset_button = tk.Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 20, "bold"))
reset_button.grid(column=2, row=3)

checkmarks = tk.Label(text="✓", fg="white", bg=BACKGROUND_COLOR, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(column=1, row=4)

window.mainloop()

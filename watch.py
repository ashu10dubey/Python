import tkinter as tk
import time as t    # Importing time module
import pytz 
import math
from datetime import datetime

def draw_clock():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist)
    hours = current_time.hour
    minutes = current_time.minute
    seconds = current_time.second

    # clear the canvas
    canvas.delete("all")

    # draw the clock
    for i in range(12):
        angle = math.pi/6 * i
        x = 300 + 200 * math.sin(angle)
        y = 300 - 200 * math.cos(angle)
        canvas.create_text(x, y, text=str(i), fill="white", font=("Helvetica", 24))

    # draw the hour hand
    hour_angle = math.pi/6 * (hours - 3)
    hour_x = 300 + 100 * math.sin(hour_angle)
    hour_y = 300 - 100 * math.cos(hour_angle)
    canvas.create_line(300, 300, hour_x, hour_y, fill="white", width=6)

    # draw the minute hand
    minute_angle = math.pi/30 * (minutes - 15)
    minute_x = 300 + 180 * math.sin(minute_angle)
    minute_y = 300 - 180 * math.cos(minute_angle)
    canvas.create_line(300, 300, minute_x, minute_y, fill="white", width=4)

    # draw the second hand
    second_angle = math.pi/30 * (seconds - 15)
    second_x = 300 + 190 * math.sin(second_angle)
    second_y = 300 - 190 * math.cos(second_angle)
    canvas.create_line(300, 300, second_x, second_y, fill="red", width=2)

    # update every 1000 ms (1 second)
    root.after(1000, draw_clock)


root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=600, height=600, bg='black')
canvas.pack()
draw_clock()
root.mainloop()

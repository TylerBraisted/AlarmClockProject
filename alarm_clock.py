import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import time
import threading


def update_clock_display(new_digit):
    current_time = clock_var.get()
    
    if new_digit.isdigit() and len(current_time) == 5:
        new_time = current_time[1:2] + current_time[3:] + new_digit
        clock_var.set(f"{new_time[:2]}:{new_time[2:]}")

def start_alarm():
    total_seconds = int(clock_var.get()[:2]) * 60 + int(clock_var.get()[3:])
    time_elapsed = 0

    while time_elapsed < total_seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = total_seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        clock_var.set(f"{minutes_left:02d}:{seconds_left:02d}")
        root.update()

    playsound("alarm_sound.mp3")
    reset_application()

def reset_application():
    clock_var.set("00:00")
    root.after(1000, lambda: enable_input(True))

def enable_input(state):
    if state:
        root.bind('<KeyPress>', on_key_press)
        start_button.config(state="normal")
    else:
        root.unbind('<KeyPress>')
        start_button.config(state="disabled")

def on_key_press(event):
    if event.keysym.isdigit():
        update_clock_display(event.char)



root = tk.Tk()
root.title("Alarm Clock")

#Frame for the Clock
top_frame = tk.Frame(root)
top_frame.grid(row=0, column=0, sticky='nsew')

# Frame for the Start Button
bottom_frame = tk.Frame(root)
bottom_frame.grid(row=1, column=0, sticky='nsew')

# Configure row and column weights
root.grid_rowconfigure(0, weight=3)  # Top frame takes up 75% of the height
root.grid_rowconfigure(1, weight=1)  # Bottom frame takes up 25% of the height
root.grid_columnconfigure(0, weight=1)  # Both frames expand horizontally

# Configure top_frame to expand
top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)

# Clock display
clock_var = tk.StringVar(value="00:00")
clock_label = tk.Label(top_frame, font=('MS Sans Serif', 48), textvariable=clock_var, bg='black', fg='white')
clock_label.grid(row=0, column=0, sticky='nsew')

# Configure bottom_frame to expand
bottom_frame.grid_rowconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(0, weight=1)

# Start button
start_button = tk.Button(bottom_frame, text="Start", command=lambda: [enable_input(False), start_alarm()], bg='green', fg='white', font=('Arial', 16), padx=0, pady=0)
start_button.grid(row=0, column=0, sticky='nsew')

# Bind key press event
root.bind('<KeyPress>', on_key_press)

root.mainloop()

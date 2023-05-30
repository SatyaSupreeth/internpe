import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label for displaying the clock
clock_label = tk.Label(window, font=('Arial', 80), fg='black')
clock_label.pack(pady=50)

# Start the clock
update_clock()

# Run the main window's event loop
window.mainloop()

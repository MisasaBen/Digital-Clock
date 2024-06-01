import time
import ttkbootstrap as tb
from tkinter import *
from ttkbootstrap.constants import *


def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    root.after(1000, update_time)


root = tb.Window(themename='cyborg')
root.title('Digital Clock')
root.geometry('300x300')

time_label = tb.Label(text='', anchor='center', font=('Times New Roman', 48))
time_label.pack(expand=True, fill=BOTH)

update_time()

root.mainloop()

import time
from tkinter import Tk, Label, END, Text, Button, mainloop

def output(message=""):
    output_field = Text(window,width=18,height=3)
    output_field.grid(row=4,column=0)
    output_field.insert(END,message)


def start_timer():
    global time1
    time1 = time.time()
    Button(window, text="stop", command=stop_timer).grid(row=1,column=0)
    output("Timer Started")

def stop_timer():
    time2 = time.time()
    time_passed = time2 - time1
    Button(window, text="start", command=start_timer).grid(row=1,column=0)
    output("%.3f" % time_passed)



window = Tk()
window.geometry("150x120")
window.config(background="grey")
Label(window, text="Stop Clock", font=10, bg="grey").grid(row=0,column=0)
Button(window, text="start", command=start_timer).grid(row=1,column=0)
Button(window, text="clear", command=output).grid(row=3,column=0)
output("Hit start to begin")
window.mainloop()
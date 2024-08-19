from tkinter import *
import time  # Import time to use time.sleep

# Create the main window
play = Tk()
play.geometry('300x500')
play.title('Traffic light - Manual control')
play.configure(bg='light blue')

# Write the functions to control the traffic light
def red():
    canvas1.create_oval(20, 20, 110, 110, outline='white', fill='red')
    canvas2.create_oval(20, 20, 110, 110, outline='white', fill='white')
    canvas3.create_oval(20, 20, 110, 110, outline='white', fill='white')

def orange():
    canvas1.create_oval(20, 20, 110, 110, outline='white', fill='white')
    canvas2.create_oval(20, 20, 110, 110, outline='white', fill='orange')
    canvas3.create_oval(20, 20, 110, 110, outline='white', fill='white')

def green():
    canvas1.create_oval(20, 20, 110, 110, outline='white', fill='white')
    canvas2.create_oval(20, 20, 110, 110, outline='white', fill='white')
    canvas3.create_oval(20, 20, 110, 110, outline='white', fill='green')

count = 30

def intervals(b):
    if b > 20:
        red()
    elif 11 <= b <= 20:
        orange()

    elif 1 <= b <= 10:
        green()    

    elif b == 0:
        red()
        b = 30
    timerdata.config(text=b) # it is used to display the current value. & to show how much time is left
    play.update() # the changes made (like updating the label) are shown on the screen.
    if b > 0:
        time.sleep(1) # this line is used to pause the programm for 1 second
        counter(b - 1) # his calls the counter function with c decreased by 1. This means the countdown continues, reducing c by 1 each time.

def counter(data):
    intervals(data)

def start():
    counter(count)

# Adding buttons
Button(play, bg='red', width='8', height='2', command=red).place(x=20, y=30)
Button(play, bg='orange', width='8', height='2', command=orange).place(x=20, y=100)
Button(play, bg='green', width='8', height='2', command=green).place(x=20, y=180)

Button(play, text='Start', bg='Grey', width=8, height=2, command=start).place(x=20, y=250)
timerdata = Label(play, font=('calibri', 30, 'bold'), bg='black', fg='red')
timerdata.place(x=20, y=320)

# Adding canvas
canvas1 = Canvas(play, width=130, height=130, bg='black')
canvas1.place(x=120, y=30)

canvas2 = Canvas(play, width=130, height=130, bg='black')
canvas2.place(x=120, y=165)

canvas3 = Canvas(play, width=130, height=130, bg='black')
canvas3.place(x=120, y=300)

play.mainloop()

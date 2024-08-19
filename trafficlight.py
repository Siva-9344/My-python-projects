from tkinter import *
import time

play = Tk()
play.geometry('300x500')
play.title('Traffic light - Manual control')
play.configure(bg = 'light blue')

# write the functions
# display red

def red():
    canvas1.create_oval(110, 110, 20, 20, outline = 'white', fill = 'red') 
    # 110, 110 These are the x and y coordinates of the upper-left corner of the bounding box of the oval.
    # 20,20 These are the width and height of the bounding box of the oval. Since the width and height are the same, the oval will be a circle.
    canvas2.create_oval(110,110,20,20, outline = 'white', fill = 'white')   
    canvas3.create_oval(110,110,20,20, outline = 'white', fill = 'white')


def orange():
    canvas1.create_oval(110,110,20,20, outline = 'white', fill = 'white')
    canvas2.create_oval(110,110,20,20, outline = 'white', fill = 'orange')   
    canvas3.create_oval(110,110,20,20, outline = 'white', fill = 'white')

def green():
    canvas1.create_oval(110,110,20,20, outline = 'white', fill = 'white')
    canvas2.create_oval(110,110,20,20, outline = 'white', fill = 'white')
    canvas3.create_oval(110,110,20,20, outline = 'white', fill = 'green') 

count = 25
def start():
    counter(count)    

def intervals(c):
    if c > 15:
        red()
        timerdata.config(text = c)
        play.update()
        sleep(1)
        counter(c)

    elif c>=1 and c<=10:
        green()
        timerdata.config(text = c)
        play.update()
        sleep(1)
        counter(c)

    elif c == 0:
        red()
        timerdata.config(text = c)
        play.update()
        sleep(1) 
        count = 25
        counter(count)      

def counter(data):
    if data > 0:
        data = data-1
        intervals(data)             


# adding buttons
Button(play, bg = 'red', width = '8', height = '2', command = red).place(x = 20, y = 30)
Button(play, bg = 'orange', width = '8', height = '2', command = orange).place(x = 20, y = 100)
Button(play, bg = 'Green', width = '8', height ='2', command = green).place(x = 20, y = 180)

# adding buttons
Button(play, text = 'start', bg = 'Grey', width = 8, height = 2, command = start).place(x = 20, y = 30)
timerdata = Label(play, font = ('calibri', 30, 'bold'), bg = 'black', fg = 'red')
timerdata.place(x = 20, y = 250)

#adding canvas

canvas1 = Canvas(play, width = 130, height =130, bg = 'black') 
canvas1.place(x = 120, y = 30) # x is Row, y is column

canvas2 = Canvas(play, width = 130, height = 130, bg = "black" )
canvas2.place(x = 120, y = 165)

canvas3 = Canvas(play, width = 130, height = 130, bg  = 'black')
canvas3.place(x = 120, y = 300)


play.mainloop()
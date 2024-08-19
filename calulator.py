from tkinter import *
import tkinter.messagebox
import math
import pytz
import datetime

obj = Tk()  #built in class
obj.geometry('700x700')  # form size
obj.title('operations')  # form title
obj.configure(bg = 'aqua') # bg color

# function

#----------------------------------------------------calc add,sub,div,mul functions------------------------------

def add():
    
    number1 = num1.get()
    number2 = num2.get()
    data = number1+ number2
    tkinter.messagebox.showinfo('Result','Total :'+str(data))

def sub():
    number1 = num1.get()
    number2 = num2.get()
    data = number1-number2
    tkinter.messagebox.showinfo('Result','Total :'+str(data))    

def multiply():
    number1 = num1.get()
    number2 = num2.get()
    data = number1*number2
    tkinter.messagebox.showinfo('Result','Total :'+ str(data)) 

def div():
    number1 = num1.get()
    number2 = num2.get()
    data = number1/number2
    tkinter.messagebox.showinfo('Result','Total :'+ str(data)) 

def time():
    data = datetime.datetime.now()
    tkinter.messagebox.showinfo('Time','currenttime :'+str(data))       
      

#----------------------------------------------------calc add,sub,div,mul functions------------------------------

#----------------------------trigonamentry function------------
def Sin():
    angle_degree = angle.get()
    angle_radians = math.radians(angle_degree)
    sin_value = math.sin(angle_radians)
    tkinter.messagebox.showinfo('Result','sinvalue :'+str(sin_value))

def Cos():
    angle_degree = angle.get()
    angle_radians = math.radians(angle_degree)
    cos_value = math.cos(angle_radians)
    tkinter.messagebox.showinfo('Result','Cosvalue :'+str(cos_value)) 

def Tan():
    angle_degree = angle.get()
    angle_radians = math.radians(angle_degree)
    tan_value = math.tan(angle_radians)
    tkinter.messagebox.showinfo('Result','tanvalue :'+str(tan_value))        
#----------------------------trigonamentry function------------

#-------------------------calculate the power--------------------------------

def power():
    c = a.get()
    d = b.get()
    e = c**d
    tkinter.messagebox.showinfo('result','Ans :'+str(e))

#-------------------------calculate the power--------------------------------

#-------------------------calculate the squareroot value----------------------
def rootvalue():
    f = root.get()
    g = f**(0.5)
    tkinter.messagebox.showinfo('result','Ans :'+str(g))
#-------------------------calculate the squareroot value----------------------

# adding lables
#The Label widget in Tkinter is used to display text or images. Here’s the basic syntax

Label(obj, text = 'Calculator', font = ('cursive',20),bg = 'aqua').place(x=30,y=5)
Label(obj, text = 'Enter Value A', font = ('calibri',10),bg = 'aqua').place(x=30,y=50) # place is working to simalar margin (x is margin-left, y is margin-top)

Label(obj, text = 'Enter value B', font = ('calibri', 10), bg = 'aqua').place(x=30, y=70)

#----------------trigonometry calculator------------------------
Label(obj, text = 'Trigonometry calculator', font = ('calibri',15), bg = 'aqua').place(x ='30', y = '200')
Label(obj, text = 'Enter the Angle Degree', font = ('calibri',10), bg = 'aqua').place(x ='30', y = '240')
#----------------trigonometry calculator------------------------

#-------------------------calculate the power--------------------------------
Label(obj, text = 'Calculate power', font = ('calibri', 15), bg = 'aqua').place(x = '440',y = '40')
Label(obj,text = "Enter the Value", font = ('calibri',10), bg ='aqua').place(x = '440',y = '75')
Label(obj,text = 'Enter the power value', font = ('calibri',10), bg = 'aqua').place(x = '440',y = '130')

#-------------------------calculate the power--------------------------------

#-------------------------calculate the squareroot value----------------------
Label(obj,text ="Square root", font = ('calibri',15),bg = "aqua").place(x='30', y= '350')
Label(obj,text ="Enter the value", font = ('calibri',10),bg = "aqua").place(x='30', y= '380')
#-------------------------calculate the squareroot value----------------------

#---------------------------------Time--------------------------------
Label(obj,text = 'Time', font = ('calibri',25),bg = 'aqua').place(x = '30',y ='470')

#---------------------------------Time--------------------------------

#______________________Game____________________________________________
Label(obj,text = "Game", font = ('calibri',25), bg = 'aqua').place(x='450', y = '270')
Label(obj,text = "Enter your value", font = ('calibri',15), bg = 'aqua').place(x='450', y = '320')

#----------------------Game-------------------------------------------

# declare value
num1 = IntVar()
num2 = IntVar()

angle = DoubleVar() # trigonomentry value


a = IntVar() # calculate the power value
b = IntVar()

root = IntVar()# calculate the squarevalue


# adding text boxes
Entry(obj, textvariable = num1, font = ('calibri',10)).place(x=180, y=50)
Entry(obj, textvariable = num2, font = ('calibri',10)).place(x=180, y=70)

#----------------trigonometry calculator------------------------
Entry(obj,textvariable = angle,font = ('calibri',10)).place(x = 30, y = 265)
#----------------trigonometry calculator------------------------

#-------------------------calculate the power--------------------------------
Entry(obj,textvariable = a, font = ('calibri',10)).place(x='440',y = '100')
Entry(obj,textvariable = b, font = ('calibri',10)).place(x='440',y = '160')
#-------------------------calculate the power--------------------------------

#-------------------------calculate the squareroot value-------------------------
Entry(obj,textvariable = root, font = ('calibri',10)).place(x='130',y = '380')
#-------------------------calculate the squareroot value-------------------------

#---------------------------Game__________________________________
Entry(obj, textvariable = num2, font = ('calibri',10)).place(x=450, y=370)



#adding button
Button(obj, text = 'Add', font = ('calibri',10), bg = 'yellow', fg = 'green', width = '10', height = '1', command = add).place(x= 180,y=120)
Button(obj, text = 'Sub', font = ('calibri',10), bg = 'yellow', fg = 'green', width = '10', height = '1', command = sub).place(x= 180,y=150)
Button(obj, text = 'Multiply', font = ('calibri',10), bg = 'yellow', fg = 'green', width = '10', height = '1', command = multiply).place(x = 265, y =120 )
Button(obj, text = 'Div', font = ('calibri',10), bg = 'yellow', fg = 'green', width = '10', height = '1', command = div ).place(x = 265, y =150 )

#--------------trigonomntry-----------------
Button(obj, text = "Sin", font = ('calibri',10), bg = 'green', width ='10', height = '1', command =Sin).place(x = 30,y = 300)
Button(obj, text = "Cos", font = ('calibri',10), bg = 'yellow', width ='10', height = '1', command =Cos).place(x = 115,y = 300)
Button(obj, text = "Tan", font = ('calibri',10), bg = '#e3a436', width ='10', height = '1', command =Tan).place(x = 200,y = 300)


#-------------------------calculate the power--------------------------------

Button(obj, text = "power", font = ('calibri',10), bg = '#e3a436', width ='10', height = '1', command =power).place(x = 450,y = 200)
#-------------------------calculate the power--------------------------------

#-------------------------calculate the squareroot value----------------------
Button(obj, text = "Squareroot", font = ('calibri',10), bg = '#e3a436', width ='10', height = '1', command =rootvalue).place(x = 135,y = 415)
#-------------------------calculate the squareroot value----------------------

Button(obj, text = "Time", font = ('calibri',10), bg = '#d8f2da', width ='10', height = '1', command =time).place(x = 30,y = 520)

#-------------------------------------------------------------------------------------------------------------------------

#--------------------------Game--------------------------------------------

Button(obj, text = "submit", font = ('calibri',10,), bg = 'green', fg = 'white',width ='10', height = '1', command =time).place(x = 450,y = 400)
#--------------------------Game------------------------------------------

obj.mainloop() # main function
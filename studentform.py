# import necessary libraries
import mysql.connector # type: ignore
from tkinter import *
from tkinter import messagebox

#functions

def submit():
    f_name = first_name.get()
    l_name = last_name.get()
    email_addr = email.get()
    phone_no = phone.get()
    course_name = course.get()
    
    # insert the data into MySQL database
    sql = "INSERT INTO students (first_name, last_name, email, phone, course) VALUES (%s, %s, %s, %s, %s)"
    values = (f_name, l_name, email_addr, phone_no, course_name)

    cursor.execute(sql, values)
    conn.commit() # commit the transaction

    # show the success message
    messagebox.showinfo("success", "Student registered Successfully!")

    # clear the form
def clear(): # this function is used to clear the form
    first_name.delete(0, END)
    last_name.delete(0, END)
    email.delete(0,END)
    phone.delete(0, END)
    course.delete(0, END)




# connect to the my sql database

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Siva@9344",
    database = "student_registration"
)
cursor = conn.cursor()

# check database connection or not
cursor.execute("SELECT DATABASE();") # Actually this is not needed this is used to check database is connected or not.
current_db = cursor.fetchone()
print(f"Connected to database: {current_db[0]}")


# create the window(display)
obj = Tk()
obj.title("student registration for")
obj.geometry("400x300")
obj.configure(bg = "light green")

# adding label
Label(obj, text = "Registration Form", bg = "light green", font = ("calibri, 15")).place(x = 120, y = 10)
Label(obj, text = "First Name", bg = "light green", font = ("calibri, 15")).place(x = 10, y = 50)
first_name = Entry(obj)
first_name.place(x = 130, y = 58)


Label(obj, text = "Last Name", bg = "light green", font = ("calibri, 15")).place(x = 10, y = 80)
last_name = Entry(obj)
last_name.place(x = 130, y = 88)

Label(obj, text = "Email", bg = "light green", font = ("calibri, 15")).place(x = 10, y = 120)
email = Entry(obj)
email.place(x = 130, y = 128)


Label(obj, text = "Phone", bg = "light green", font = ("calibri, 15")).place(x = 10, y = 150)
phone = Entry(obj)
phone.place(x = 130, y = 158)


Label(obj, text = "Course", bg = "light green", font = ("calibri, 15")).place(x = 10, y = 180)
course = Entry(obj)
course.place(x = 130, y = 188)

#button
Button(obj, text = "Submit", command = submit).place(x = 130, y = 228)

#clear button
Button(obj, text = "clear", command = clear).place(x = 200, y = 228)




obj.mainloop()
conn.close()

from tkinter import *
from tkinter import ttk

def update_districts(*args):
    # Clear the existing options in the district dropdown
    dropmenu2['menu'].delete(0, 'end')
    
    # Get the selected state
    selected_state = dropvar1.get()
    
    # Add the corresponding districts to the district dropdown
    if selected_state in options2:
        for district in options2[selected_state]:
            dropmenu2['menu'].add_command(label=district, command=lambda value=district: dropvar2.set(value))


obj = Tk()
obj.geometry('500x500')
obj.title('operations')              #}---> thess are all create the main window
obj.configure(bg = 'light green')

#adding labels
Label(obj, text = 'select the state', font = ('calibiri',15), bg = 'light green').place(x = 30, y = 30)
Label(obj, text = 'select the district', font = ('calibiri', 15), bg = 'light green').place(x = 30, y = 125)

# adding option menu
options1 = ['TamilNadu', 'Kerala', 'Goa', 'Andhara pradesh', 'karnataka']
dropvar1 = StringVar()
dropmenu1 = ttk.OptionMenu(obj, dropvar1,'---------select----------',*options1, command=update_districts) # this line is used to create that dropmenu box
dropmenu1.place(x = 200, y = 30)         # this line is used to fix the position of that box


options2 = {
    'Andhara pradesh':['chittoor','Nellore','Guntur'],
    'Goa':['north Goa', 'South Goa'],
    'karnataka':['Bangalore', 'Kolar', 'Mysore'],
    'Kerala':['Ernakulam', 'Kollam', 'Alapuzha'],
    'TamilNadu':['chennai','salem', 'Trichy']
}
dropvar2 = StringVar()
dropmenu2 = ttk. OptionMenu(obj,dropvar2,'----------Select--------')
dropmenu2.place(x=200, y=130 )

obj.mainloop()

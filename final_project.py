"""
Group members: Moises Hernandez, Yash Gupta, Bao Nguyen, Youwei Dou
Professor: Bill Farmer
Assignment: Final Project
Date:
Challenges encountered:
Function of program: Keep track of and organize information. 
Specfically, keep track of employees information. 

"""
##Structure of code##
"""
Step 1: import tkinter. 
tkinter is a GUI library
which is used for creating 
GUI applications.  
"""

from tkinter import *
from tkinter import ttk

#colors for GUI application:

#White
color_0 = "#ffffff"
#Black
color_1 = "#000000"
#red
color_2 = "#e95566"

"""
Create basic window for project. 
A window is like a 
container where other 
GUI elements are inside of.

"""

window=Tk()
window.title ("")
window.geometry('485x450')
window.configure(background=color_1)
window.resizable(width=FALSE, height=FALSE)

#makes red strip on top of window 
frame_up= Frame(window, width=500, height=50, bg=color_2)
frame_up.grid(row=0, column=0, padx=0, pady=0)

#makes white background in window
frame_down= Frame(window, width=500, height=150, bg=color_0)
frame_down.grid(row=1, column=0, padx=0, pady=1)




##For the Frame Table##
"""
Using Frame
Make a frame table which would hold the information from the user
We will need 3 rows I believe (for phone #, email, name), which would be added within the Frame code. Additional cosmetics such as labels will be added.
An entry bubble for the user will be made, using the Entry function.
If we decide that we need to make dropdown options, we will do that too as needed, after discussing with our group.
We will use similar code to have the user search for contacts as needed. 
We will also make a table with the saved contacts. I think the code will be similar to the previosly used code, but we can ask the TA for help on that. I believe that we will use treeview, as it within the Tkinter we imported.



"""


"""Creating the widgets for upper frame by initializing the text name (App name), its height, its font with the size of font. Also, I have to choose the foreground color as black which was defined on top  """

app_name = Label(frame_up, text="Customer Database Software",height =1, font = ('Verdana 17 bold'),fg = color_1)

app_name.place(x=5,y=5) #this will be located where the app name display at top by the order of x and y

"""Creating the widgets for lower frame which can be places to let the user input values"""



"""Define name value line"""
label_name = Label(frame_down, text="Name *",width = 20, height =1, font = ('Ivy 10'),bg = color_1, anchor = NW)
label_name.place (x=10,y=20)
entry_name = Entry(frame_down,width = 25, justify ='left',highlightthickness = 1,relief= "solid")
entry_name.place (x=80,y=20)

"""Define gendervalue line"""
label_gender = Label(frame_down, text="Name *",width = 20, height =1, font = ('Ivy 10'),bg = color_1, anchor = NW)
label_gender.place (x=10,y=50)
entry_gender = ComboBox(frame_down,width = 27, relief= "solid")
"""Customer gender M: Male, F: Female"""
customer_gender ['values'] = ['','M','F']

entry_gender.place(x=80,y=50)

"""Define the telephone value line"""
label_telephone = Label(frame_down, text="Phone Number", height =1, font = ('Ivy 10'),bg = color_1, anchor = NW)
label_telephone.place (x=10,y=80)
entry_telephone = Entry(frame_down,width = 25, justify ='left',highlightthickness = 1,relief= "solid")
entry_telephone.place (x=80,y=80)


"""Define the email value line"""

label_email = Label(frame_down, text="Email", height =1, font = ('Ivy 10'),bg = color_1, anchor = NW)
label_email.place (x=10,y=110)
entry_email = Entry(frame_down,width = 25, justify ='left',highlightthickness = 1,relief= "solid")
entry_email.place (x=80,y=110)

"""Create the search button"""

button_search = Button(frame_down, text="SEARCH",height =1, bg = color_2, font = ('Ivy 8 bold'))
button_search.place(x=290,y=50)
entry_search = Entry(frame_down,width = 16, justify ='left',font = ('Ivy',11),highlightthickness = 1,relief= "solid")
entry_search.place(x=347,y=20)

"""Creating the view button"""
button_view = Button(frame_down, text="VIEW",width=10,height =1, bg = color_2, font = ('Ivy 8 bold'))
button_view.place(x=290,y=50)


"""Create the add button"""
button_add = Button(frame_down, text="ADD",width=10,height =1, bg = color_2, font = ('Ivy 8 bold'))
button_add.place(x=400,y=50)
"""Create the update button"""
button_update = Button(frame_down, text="UPDATE",width=10,height =1, bg = color_2, font = ('Ivy 8 bold'))
button_update.place(x=400,y=80)


"""Create the delete button"""
button_delete = Button(frame_down, text="UPDATE",width=10,height =1, bg = color_2, font = ('Ivy 8 bold'))
button_delete.place(x=400,y=110)



window.mainloop()
"""
Book Database that store information like
Book Title, Author, Borrowed, Lent, Name, Date

User can
view all records
View Borrowed
View lent
Search an entry
Add an entry
Update entry
Delete entry
close
"""

from tkinter import *

window = Tk()

l1 = Label(window , text = "Title")
l1.grid(row = 0 , column = 0 )

l2 = Label(window , text = "Author")
l2.grid(row = 0 , column = 2 )

l3 = Label(window , text = "Name(optional)")
l3.grid(row = 1 , column = 0 )


l4 = Label(window , text = "Date(optional)")
l4.grid(row = 1, column = 2 )

title_text = StringVar()
e1 = Entry(window , textvariable = title_text )
e1.grid(row = 0 , column = 1)

author_text = StringVar()
e2 = Entry(window , textvariable = author_text )
e2.grid(row = 0 , column = 3)

name_text = StringVar()
e3 = Entry(window , textvariable = name_text )
e3.grid(row = 1 , column = 1)

date_text = StringVar()
e4 = Entry(window , textvariable = date_text )
e4.grid(row = 1 , column = 3)

list1 = Listbox(window, height = 15 , width = 40)
list1.grid(row = 2 , column = 0 , rowspan = 8 , columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2 , column = 2 , rowspan = 8)

#now we tell the list and scrollbar about each other

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window , text = "View all" , width = 15)
b1.grid(row = 2 , column = 3 )

b2 = Button(window , text = "Borrowed" , width = 15)
b2.grid(row = 3 , column = 3 )

b3 = Button(window , text = "lent" , width = 15)
b3.grid(row = 4 , column = 3 )

b4 = Button(window , text = "Search" , width = 15)
b4.grid(row = 5 , column = 3 )

b5 = Button(window , text = "Add" , width = 15)
b5.grid(row = 6 , column = 3 )

b6 = Button(window , text = "Update" , width = 15)
b6.grid(row = 7 , column = 3 )

b7 = Button(window , text = "Delete" , width = 15)
b7.grid(row = 8 , column = 3 )

b8 = Button(window , text = "Close" , width = 15)
b8.grid(row = 9 , column = 3 )



window.mainloop()

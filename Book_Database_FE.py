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
import Book_Database_BE

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)

    e1.delete(0 , END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0 , END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0 , END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0 , END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0 , END)
    for row in Book_Database_BE.view():
        list1.insert(END,row)
def search_command():
    list1.delete(0 , END)
    for row in Book_Database_BE.search(title_text.get(),author_text.get(),name_text.get(),date_text.get()):
        list1.insert(END , row)
def add_command():
    Book_Database_BE.insert(title_text.get(),author_text.get(),name_text.get(),date_text.get())
    list1.delete(END , 0 )
    list1.insert(END,(title_text.get(),author_text.get(),name_text.get(),date_text.get()))
def view_lent():
    list1.delete(0 , END)
    for row in Book_Database_BE.viewlent():
        list1.insert(END,row)
def delete_command():
    Book_Database_BE.delete(selected_tuple[0])
def update_command():
    Book_Database_BE.update(selected_tuple[0] ,title_text.get(),author_text.get(),name_text.get(),date_text.get() )



window = Tk()

window.wm_title("Library Database")

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

list1 = Listbox(window, height = 15 , width = 40  , selectmode = "single")
list1.grid(row = 2 , column = 0 , rowspan = 8 , columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2 , column = 2 , rowspan = 8)

#now we tell the list and scrollbar about each other

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window , text = "View all" , width = 15, command = view_command)
b1.grid(row = 2 , column = 3 )

b3 = Button(window , text = "lent" , width = 15 , command = view_lent)
b3.grid(row = 4 , column = 3 )

b4 = Button(window , text = "Search" , width = 15 , command = search_command)
b4.grid(row = 5 , column = 3 )

b5 = Button(window , text = "Add" , width = 15 , command = add_command)
b5.grid(row = 6 , column = 3 )

b6 = Button(window , text = "Update" , width = 15 , command = update_command)
b6.grid(row = 7 , column = 3 )

b7 = Button(window , text = "Delete" , width = 15 , command  = delete_command)
b7.grid(row = 8 , column = 3 )

b8 = Button(window , text = "Close" , width = 15 , command = window.destroy)
b8.grid(row = 9 , column = 3 )



window.mainloop()

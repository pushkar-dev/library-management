from tkinter import Tk,Menu,Label,Button
import tkinter.messagebox
from tkinter import ttk
from app_backend import lib_issue,lib_return,add_book,add_mem,lib_card_display,clerr
print('hi!using p-lid')
win=Tk()
win.title('p-lid |v 1.0.0|')
win.geometry('2000x700')


def issuebookwin():lib_issue(win)
def retrnbookwin():lib_return(win)
def addbookwin():add_book(win)
def addmemwin():add_mem(win)
def libcard():lib_card_display(win)   


def prepare():
    head=Label(win,text='LIBRARY MANAGEMENT SYSTEM',font=('arial',17,'italic'),fg='orange',bg='cyan')
    head.place(x=500,y=5)
    add_mem=Button(win,text='Add New Member',font=('arial',20,'bold'),relief='raised',bg='orange',fg='black',command=addmemwin)
    add_mem.place(x=150,y=100)
    add_book=Button(win,text='  Add New Book  ',font=('arial',20,'bold'),relief='raised',bg='orange',fg='black',command=addbookwin)
    add_book.place(x=550,y=100)
    find_book=Button(win,text='  Issue Book  ',font=('arial',20,'bold'),relief='raised',bg='orange',fg='black',command=issuebookwin)
    find_book.place(x=950,y=100)
    member_list=Button(win,text='     Return Book    ',font=('arial',20,'bold'),relief='raised',bg='orange',fg='black',command=retrnbookwin)
    member_list.place(x=150,y=200)
    update_mem_data=Button(win,text='Library Card',font=('arial',20,'bold'),relief='raised',bg='orange',fg='black',command=libcard)
    update_mem_data.place(x=520,y=200)
    update_bk_data=Button(win,text='Update book data',font=('arial',20,'bold'),relief='raised',bg='orange',fg='black')
    update_bk_data.place(x=920,y=200)
    #clerr_but=Button(win,text='__clear__',font=('arial',20,'bold'),relief='raised',bg='orange',fg='black',command=clerr).place(x=150,y=300)
    
def about():
    tkinter.messagebox.showinfo('p-lid| v 1.0.0 |','thank you for using p-lid!')
def Help():
    tkinter.messagebox.showinfo('p-lid| v 1.0.0 |','sorry!help cannot be accessed.')
def menu_bar():
    menu=Menu(win)
    drp_file=Menu(menu,tearoff=0)
    menu.add_cascade(label='File',menu=drp_file)
    menu.add_cascade(label='About',command=about)    
    menu.add_cascade(label='Help',command=Help)
    drp_file.add_cascade(label='Exit',command=exit)
    win.config(menu=menu)

menu_bar()
prepare()
win.mainloop()
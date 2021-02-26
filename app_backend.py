from tkinter import Toplevel,StringVar,IntVar,Label,Entry,Button
from lib_proj_fh import Library
from lib_proj_base import book,member
import tkinter.messagebox

library=Library()


def lib_issue(MASTER):
    win1=Toplevel()
    bkid=StringVar()
    userid=StringVar()
    def on_close():
        MASTER.wm_state('zoomed')
        win1.destroy()
    def doit():
        bid=bkid.get()
        uid=userid.get()  
        if len(bid)==0:
            tkinter.messagebox.showinfo('p-lid','p-lid says book id should not be blank')
            retry=True
        elif len(uid)==0:
            tkinter.messagebox.showinfo('p-lid','p-lid says user id should not be blank')
            retry=True
        else : retry=False
        if retry==False:
                a=library.issue(uid,bid)
                win1.destroy()
                tkinter.messagebox.showinfo('p-lid',f'p-lid says {a}')
                MASTER.wm_state('zoomed')
    win1.geometry('500x500')
    MASTER.wm_state('iconic')
    label1=Label(win1,text='BOOK ISSUE MENU',font=('arial',20,'bold')).place(x=150,y=10)
    
    label2=Label(win1,text='BOOK ID:').place(x=50,y=80)
    entry2=Entry(win1,textvar=bkid).place(x=140,y=80)
    
    label3=Label(win1,text='MEMBER ID:').place(x=50,y=100)
    entry3=Entry(win1,textvar=userid).place(x=140,y=100)
    
    b1=Button(win1,text='Issue',relief='raised',command=doit).place(x=140,y=200)
    win1.protocol('WM_DELETE_WINDOW',on_close)
    
def add_book(MASTER):
    win1=Toplevel()
    bkid=StringVar()
    bkname=StringVar()
    author=StringVar()
    number=IntVar()
    def on_close():
        MASTER.wm_state('zoomed')
        win1.destroy()
    def doit():
        bid=bkid.get()
        bname=bkname.get()
        aut=author.get()
        num=number.get()
        if len(bid)==0:
            tkinter.messagebox.showinfo('p-lid','p-lid says book id should not be blank')
            retry=True
        elif len(bname)==0:
            tkinter.messagebox.showinfo('p-lid','p-lid says book name should not be blank')
            retry=True
        elif len(aut)==0:
            tkinter.messagebox.showinfo('p-lid','p-lid says book author should not be blank')
            retry=True
        elif(num==0):
            tkinter.messagebox.showinfo('p-lid','p-lid says book number should not be blank')
            retry=True
        else : retry=False
        if retry==False:
                bk=book(bid,bname,aut,num)
                library.bkshelf.addnew(bk)
                win1.destroy()
                tkinter.messagebox.showinfo('p-lid','p-lid says books added succesfully')
                MASTER.wm_state('zoomed')
    win1.geometry('500x500')
    MASTER.wm_state('iconic')
    label1=Label(win1,text='NEW BOOK MENU',font=('arial',20,'bold')).place(x=150,y=10)
    
    label2=Label(win1,text='BOOK ID:').place(x=50,y=80)
    bookid=Entry(win1,textvar=bkid).place(x=170,y=80)
    
    label3=Label(win1,text='BOOK NAME:').place(x=50,y=100)
    bookname=Entry(win1,textvar=bkname).place(x=170,y=100)
    
    label4=Label(win1,text='NUMBER OF BOOKS :').place(x=50,y=120)
    numberentry=Entry(win1,textvar=number).place(x=170,y=120)
    
    label5=Label(win1,text='AUTHOR :').place(x=50,y=140)
    authorentry=Entry(win1,textvar=author).place(x=170,y=140)
    b1=Button(win1,text='Add',relief='raised',command=doit).place(x=140,y=200)
    win1.protocol('WM_DELETE_WINDOW',on_close)

def add_mem(MASTER):
    win1=Toplevel()
    userid=StringVar()
    username=StringVar()
    def on_close():
        MASTER.wm_state('zoomed')
        win1.destroy()
    def doit():
        uid=userid.get()
        name=username.get()
        if len(uid)==0:
            tkinter.messagebox.showinfo('p-lid','p-lid says  id should not be blank')
            retry=True
        elif len(name)==0:
            tkinter.messagebox.showinfo('p-lid','p-lid says  name should not be blank')
            retry=True
        else : retry=False
        if retry==False:
                mem=member(uid,name)
                library.diary.addnew(mem)
                win1.destroy()
                tkinter.messagebox.showinfo('p-lid','p-lid says member registered succesfully')
                MASTER.wm_state('zoomed')
    win1.geometry('500x500')
    MASTER.wm_state('iconic')
    label1=Label(win1,text='ADD MEMBER MENU',font=('arial',20,'bold')).place(x=150,y=10)
    
    label2=Label(win1,text='MEMBER ID:').place(x=50,y=80)
    entry2=Entry(win1,textvar=userid).place(x=140,y=80)
    
    label3=Label(win1,text='MEMBER NAME:').place(x=50,y=100)
    entry3=Entry(win1,textvar=username).place(x=140,y=100)
    
    b1=Button(win1,text='Add',relief='raised',command=doit).place(x=140,y=200)
    win1.protocol('WM_DELETE_WINDOW',on_close)

def lib_return(MASTER):
    win1=Toplevel()
    bkid=StringVar()
    userid=StringVar()
    def on_close():
        MASTER.wm_state('zoomed')
        win1.destroy()
    def doit():
        bid=bkid.get()
        uid=userid.get()  
        if len(bid)==0:
            tkinter.messagebox.showinfo('p-lid','p-lid says book id should not be blank')
            retry=True
        elif len(uid)==0:
            tkinter.messagebox.showinfo('p-lid','p-lid says user id should not be blank')
            retry=True
        else : retry=False
        if retry==False:
                a=library.retrn(uid,bid)
                win1.destroy()
                tkinter.messagebox.showinfo('p-lid',f'p-lid says {a}')
                MASTER.wm_state('zoomed')
    win1.geometry('500x500')
    MASTER.wm_state('iconic')
    label1=Label(win1,text='BOOK RETURN MENU',font=('arial',20,'bold')).place(x=150,y=10)
    
    label2=Label(win1,text='BOOK ID:').place(x=50,y=80)
    entry2=Entry(win1,textvar=bkid).place(x=140,y=80)
    
    label3=Label(win1,text='MEMBER ID:').place(x=50,y=100)
    entry3=Entry(win1,textvar=userid).place(x=140,y=100)
    
    b1=Button(win1,text='Return',relief='raised',command=doit).place(x=140,y=200)
    win1.protocol('WM_DELETE_WINDOW',on_close)
def lib_card_display(MASTER):
    win1=Toplevel()
    memid=StringVar()
    memname=StringVar()
    win1.geometry('500x500')
    MASTER.wm_state('iconic')
    def on_close():
        MASTER.wm_state('zoomed')
        win1.destroy()
    
        
    def doit():
        mid=memid.get()
        mname=memname.get()
        try:
            labelc.destroy()
        except: pass
        if len(mid)!=0 :
            mem=library.diary.lookup_byid(mid)
            if mem!=None:
                labelc=Label(win1,text=str(mem),font=('arial',20,'bold')).place(x=200,y=200)
            else:
                tkinter.messagebox.showinfo('p-lid','sorry!member not found')
        elif len(mname)!=0:
            mem=library.diary.lookup_byname(mname)
            if mem!=None:
                labelc=Label(win1,text=str(mem),font=('arial',20,'bold')).place(x=200,y=200)
            else:
                tkinter.messagebox.showinfo('p-lid','sorry!member not found')
    
    label1=Label(win1,text='LIBRARY CARD DISPLAY',font=('arial',20,'bold')).place(x=110,y=10)
    
    label2=Label(win1,text='MEMBER ID:').place(x=30,y=60)
    entry2=Entry(win1,textvar=memid).place(x=120,y=60)
    
    label3=Label(win1,text='MEMBER NAME:').place(x=30,y=80)
    entry3=Entry(win1,textvar=memname).place(x=120,y=80)
    
    loadbtn=Button(win1,text='Load',relief='raised',command=doit).place(x=250,y=100)
    win1.protocol('WM_DELETE_WINDOW',on_close)
def clerr():
    library.bkshelf.clean()
    library.diary.clean()
#def mem_list(MASTER,win1):
#end
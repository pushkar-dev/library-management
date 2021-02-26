import pickle
import os
from lib_proj_base import book,member

def createfile(filename):
    with open(filename,'wb') as f:
        pass
class bookshelf:
    def __init__(self,filename):
        self.__filename=filename
    def addnew(self,bk):
        try:
            with open(self.__filename,'rb+') as f:
                f.seek(0,2)
                pickle.dump(bk,f)
        except FileNotFoundError:
            createfile(self.__filename)
            self.addnew(bk)
    def lookup_byid(self,bkid):
        try:
            with open(self.__filename,'rb+') as f:
                f.seek(0)
                while True:
                    try:
                        book1=pickle.load(f)
                        if(book1.getid()==bkid):
                            return book1
                    except :
                        break
        except FileNotFoundError:
            raise FileNotFoundError
        return None
    def lookup_byname(self,bkname):
        try:
            with open(self.__filename,'rb+') as f:
                f.seek(0)
                while True:
                    try:
                        byt=f.tell()
                        book1=pickle.load(f)
                        if(book1.getauthor()==bkname):
                            return byt,book1
                    except :
                        break
        except FileNotFoundError:
            raise FileNotFoundError
        return -1,None        
    def lookup_byauthor(self,author):
        lst=[]
        with open(self.__filename,'rb+') as f:
            f.seek(0,0)
            while True:
                try:
                    book1=pickle.load(f)
                    if(book1.getauthor()==author):
                        lst.append(book1)
                except :
                    break
        if len(lst) != 0:
            return lst
        else:
            return -1
    def update_book(self,book1):
        self.discard_book(book1.getid())
        self.addnew(book1)
    def discard_book(self,bkid):
        with open(self.__filename,'rb+') as f:
            temp=open('tempf.txt','wb')
            while True:
                try:
                    obj=pickle.load(f)
                    if obj.getid() != bkid:
                        pickle.dump(obj,temp)
                except EOFError:
                    break
            temp.close()
        #os.chdir("D:\PUSHKAR'S STUDY MATERIAL\computer science\python\lib_proj")
        os.remove( self.__filename)
        os.rename('tempf.txt',self.__filename)
    def view_all(self):
         with open(self.__filename,'rb+') as f:
            f.seek(0)
            while True:
                #lst=[]
                try:
                    book1=pickle.load(f)
                    print(book1)
                    #lst.append(book1)
                except: break
    def clean(self):
        with open (self.__filename,'wb') as f: pass
    def return_dir(self):
        return self.__filename

class diary:
    def __init__(self,filename):
        self.__filename=filename
    
    def addnew(self,mem):
        try:
            with open(self.__filename,'rb+') as f:
                f.seek(0,2)
                pickle.dump(mem,f)
        except FileNotFoundError:
            createfile(self.__filename)
    def lookup_byid(self,uid):
        with open(self.__filename,'rb+') as f:
            f.seek(0)
            while True:
                try:
                    mem1=pickle.load(f)
                    if(mem1.getuid()==uid):
                        return mem1
                except :
                    break
        return None
    def lookup_byname(self,name):
        with open(self.__filename,'rb+') as f:
            f.seek(0)
            while True:
                try:
                    
                    mem1=pickle.load(f)
                    if(mem1.getname()==name):
                        return mem1
                except :
                    break
        return None
    def update_mem(self,mem1):
        self.remove_mem(mem1.getuid())
        self.addnew(mem1)
    def remove_mem(self,uid):
        with open(self.__filename,'rb+') as f:
            temp=open('tempf.txt','wb')
            while True:
                try:
                    obj=pickle.load(f)
                    if obj.getuid() != uid:
                        pickle.dump(obj,temp)
                except :
                    break
            temp.close()
        #os.chdir("D:\PUSHKAR'S STUDY MATERIAL\computer science\python\lib_proj")
        os.remove( self.__filename)
        os.rename('tempf.txt',self.__filename)
    def view_all(self):
         with open(self.__filename,'rb+') as f:
            f.seek(0,0)
            while True:
                lst=[]
                try:
                    mem1=pickle.load(f)
                    print(mem1)
                    lst.append(mem1)
                except EOFError: break
    def clean(self):
        with open (self.__filename,'wb') as f: pass
    def return_dir(self):
        return self.__filename
   


class Library:
    def __init__(self,shelffile='liddbms.txt',diaryfile='memdbms.txt'):
        self.bkshelf=bookshelf(shelffile)
        self.diary=diary(diaryfile)
    def issue(self,uid,bid):
        b1=self.bkshelf.lookup_byid(bid)
        mem1=self.diary.lookup_byid(uid)
        if (b1!=None and mem1!=None and b1.getno()>0):
            msg=mem1.issue(b1.getname())
            if msg==1:
                b1.issue()
                self.diary.update_mem(mem1)
                self.bkshelf.update_book(b1)
                return 'SUCCESS'
            elif msg==0:
                return 'TWO BOOKS CAN\'T BE ISSUED AT A TIME'
            elif msg==-1:
                return 'SORRY! MEMBER IS BLACKLISTED'
        elif b1==None:
            return 'BOOK NOT FOUND'
        elif b1.getno()==0:
            return 'THIS BOOK IS UNAVAILABLE'
        elif mem1==None:
            return 'MEMBER NOT FOUND'
    def retrn(self,uid,bid):
        b1=self.bkshelf.lookup_byid(bid)
        mem2=self.diary.lookup_byid(uid)
        if b1!=None and mem2!=None:
            msg=mem2.retrn(b1.getname())
            if msg==1:
                b1.retrn()
                self.diary.update_mem(mem2)
                self.bkshelf.update_book(b1)
                return 'SUCCESS'
            elif msg==0:
                return 'NO BOOK HAS BEEN ISSUED TO MEMBER' 
            elif msg==-1:
                return 'THIS BOOK WAS NOT ISSUED TO MEMBER'
        elif b1==None:
            return 'BOOK NOT FOUND'
        elif mem2==None:
            return 'MEMBER NOT FOUND'
        

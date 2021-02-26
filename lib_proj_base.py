class book:
    def __init__(self,bkid,bkname,author,number):
        self.__bkid=bkid
        self.__bkname=str(bkname)
        self.__author=str(author)
        self.__number=int(number)
    def getid(self):
        return self.__bkid
    def getno(self):
        return self.__number
    def getname(self):
        return self.__bkname
    def getauthor(self):
        return self.__author
    def __str__(self):
        return str(f'Book ID:{self.__bkid}\n Book Name:{self.__bkname}\n Author:{self.__author}\n Stock:{self.__number}')
    def issue(self):
        self.__number-=1
    def retrn(self):
        self.__number+=1

class member:
    def __init__(self,uid,name,dues=None):
        self.__name=str(name)
        self.__uid=str(uid)
        self.issued=False
        self.blacklisted=False
        self.bktaken=''
    def issue(self,bkname): 
        if self.issued==False and self.blacklisted==False:
            self.issued=True
            self.bktaken=bkname
            return 1# success
        elif self.issued==True:
            return 0 #0-->has a book
        elif self.blacklisted==True:
            return -1 #(-1)-->is blacklisted
    def retrn(self,bkname): 
        if self.issued==True and self.bktaken==bkname:
            self.issued=False
            self.bktaken=None
            return 1#success
        elif self.bktaken!=bkname:
            return -1#any other book was issued
        elif self.bktaken==None:
            return 0#no book was taken
    def clerr(self): 
        self.dues=None
    def blacklist(self):
        self.blacklisted=True
    def set_due(self,dues):
        self.dues=dues
    def getuid(self):
        return self.__uid
    def getname(self):
        return self.__name
    def __str__(self):
        return str(f'UID:{self.__uid}\nName:{self.__name}')
    

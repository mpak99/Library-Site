from calendar import c
from multiprocessing import connection
from select import select
import sqlite3
from tabnanny import check

import os ,sys
clear = lambda : os.system("cls")


database = sqlite3.connect("BooksDB.db", check_same_thread=False)
cur=database.cursor()



# database = sqlite3.connect('booksDB.db')
# cur = database.cursor()





cur.execute("CREATE TABLE IF NOT EXISTS books_tbl(ISBN INTEGER PRIMARY KEY,title TEXT,author TEXT,price FLOAT,pages INTEGER)")

    # cur.execute("INSERT INTO books_tbl VALUES (12345678, 'BIBLE', 'UNKNOWN', 100, 500)")

database.commit()

class WrongISBN(Exception):
    pass


class Book :
    
    count = 0
    def __init__(self,ISBN,title,author,price,pages) :

        self.ISBN=ISBN
        self.title=title
        self.author=author
        self.price=price
        self.pages=pages
        self.checkup_dates = []
        self.__maxprice = 250000
        Book.count +=1
        cur.execute("INSERT INTO books_tbl VALUES(?,?,?,?,?)",(self.ISBN,title,author,price,pages))
        database.commit()
        #insert into database
        

    @classmethod
    def find_book(cls,ISBN):
        select_books=list(cur.execute("SELECT * FROM books_tbl WHERE ISBN = ?" , (ISBN,)))
        if len(select_books) == 0 :
            raise Exception("Book does not exist in database !")
        else:
            return list(select_books)

    @classmethod
    def list(cls):
        return list(cur.execute("SELECT * FROM books_tbl"))

    @classmethod
    def update(cls,ISBN, title, author, price, pages):
        update_books=cur.execute("UPDATE books_tbl SET ISBN=?, title=?, author=?, price=?, pages=? WHERE ISBN=?" ,(ISBN,title,author,price,pages))
        if update_books.rowcount ==0:
            print("Book does not exist in database !")
        database.commit()

    @classmethod
    def delete(cls,ISBN):
        del_book=cur.execute("DELETE FROM books_tbl WHERE ISBN = ?",(ISBN,))
        if del_book.rowcount == 0 :
            raise Exception("Book does not exist in database !")
        database.commit()
    
    @property
    def ISBN(self) :
        return self.code
    @ISBN.setter
    def ISBN(self,value):
        if len(value) == 8 :
            self.code = value
        else : 
            raise WrongISBN

def add_book():
    try:
        bk = Book(
        input("ISBN : "), 
        input("Tiltle : "),
        input("Author :"), 
        int(input("Price :")), 
        int(input("Pages :")))
    except(WrongISBN):
        print("ISBN is a 8 digit number")
        return 0

    clear()
    return bk
# add_book()
# creat_table()
















# def create_books_table():
#     cur.execute("CREATE TABLE IF NOT EXISTS books_tbl(ISBN INTEGER PRIMARY KEY,title TEXT,author TEXT,price FLOAT,pages INTEGER)")

def insert_book(*rec):
    try :
        cur.execute("INSERT INTO books_tbl(ISBN, title, author, price, pages) VALUES(?,?,?,?,?)",rec)
    except(sqlite3.IntegrityError):
        print("CarID Already Exists !")
        return False
    return True    













#=============================== Main ==============================================
# create_books_table()
# book1=Book("12345677","bible","unknown",100,500)



from datetime import datetime

from book import Book

VERSION = "0.1"

class LibraryDB:

    def __init__(self) -> None:
        self.books = []

    def add_book(self, new_book: Book) -> None:
        self.books.append(new_book)
    
    def list_books(self) -> None:
        print("----------------- Book List -----------------")
        for x in self.books:
            print(x.__dict__())
    

def main():
    print(f"----------------- Book Catalog Manager V{VERSION}----------------- \n©Clara Yau, June 12 2024, all Rights Reserved")
    myDB = LibraryDB()
    book1 = Book("On Modern Motion Pictures", "Helen Keller")
    myDB.add_book(book1)

    book2 = Book("The Book of Morons", "John Smith")
    myDB.add_book(book2)

    book3 = Book("Harry Potter and the Crystals of Meth", "JK Rolling")
    myDB.add_book(book3)
    myDB.list_books()

    book1.lend_out()
    myDB.list_books()

    book2.discontinue()
    myDB.list_books()

    book1.restock()
    myDB.list_books()
    


if __name__ == "__main__":
    main()
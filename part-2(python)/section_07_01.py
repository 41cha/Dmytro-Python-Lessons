class Reader():
    def __init__(self, name, contact, ticket_num):
        self.name = name
        self.contact = contact
        self.ticket_num = ticket_num

    def get_name(self):
        return self.name
    
    def get_contact(self):
        return self.contact
    
    def get_ticket_num(self):
        return self.ticket_num

class Book():
    def __init__(self, name, year, author, isbn):
        self.__name = name
        self.__year = year
        self.__author = author
        self.__isbn = isbn

    def __str__(self):
        return f"Title: {self.get_name()}, Author: {self.get_author()}, Year: {self.get_year()}, ISBN: {self.get_isbn()}"
    
    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

class Catalog():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                self.books.remove(book)
                break

    def find_book(self, query):
        for book in self.books:
            if book.get_name() == query or book.get_author() == query:
                return book
        return None

class Borrowing():
    def __init__(self, reader, book, borrow_date):
        self.reader = reader
        self.book = book
        self.borrow_date = borrow_date

    def get_reader(self):
        return self.reader

    def get_book(self):
        return self.book

    def get_borrow_date(self):
        return self.borrow_date
    

class IllustratedBook(Book):
    def __init__(self, name, year, author, isbn, illustrator, illustrations_count):
        super().__init__(name, year, author, isbn)
        self.__illustrator = illustrator
        self.__illustrations_count = illustrations_count

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Illustrator: {self.__illustrator}, Illustrations count: {self.__illustrations_count}"

    def get_illustrator(self):
        return self.__illustrator
    
    def illustration_num(self):
        return self.__illustrations_count
    


catalog = Catalog()

book = Book("Назва", 2022, "Автор", "1234")
catalog.add_book(book)

reader = Reader('Vova', 380633058397, 2727)
found_book = catalog.find_book("Назва")
if found_book:
    borrowing = Borrowing(reader, found_book, "2025-11-23")
    print(borrowing.get_borrow_date())

illustr_book = IllustratedBook("Аліса", 1865, "Льюїс Керролл", "1111", "Джон Тенніел", 42)
print(illustr_book.get_illustrator())
print(illustr_book.illustration_num())

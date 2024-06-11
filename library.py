import csv
from book import Book

class Library:
    def __init__(self, filepath='library.csv'):
        self.filepath = filepath    #csv files misamarti
        self.books = self.load_books()  #arsebuli wignebis dabruneba

    def add_book(self, title, author):
        #shevqmnat axali book objecti
        book = Book(title, author)
        self.books.append(book)
        self.save_books() #shevinaxot yvelaferi csv fileshi
        print(f'Book "{title}" by {author} added to the library.')

    def issue_book(self, title):
        #wingebis dzebna saxelis mixedvit
        for book in self.books:
            if book.title == title:
                if not book.is_issued:
                    book.is_issued = True
                    self.save_books() #daupdatebuli wignebis shenaxva
                    print(f'Book "{title}" has been issued.')
                    return
                else:
                    print(f'Book "{title}" is already issued.')
                    return
        print(f'Book "{title}" not found in the library.')

    def return_book(self, title):
        #wingebis dabrunebis logika
        for book in self.books:
            if book.title == title:
                if book.is_issued:
                    book.is_issued = False
                    self.save_books()
                    print(f'Book "{title}" has been returned.')
                    return
                else:
                    print(f'Book "{title}" was not issued.')
                    return
        print(f'Book "{title}" not found in the library.')

    def view_books(self):
        #arsebuli wignebis naxva
        for book in self.books:
            status = 'Issued' if book.is_issued else 'Available'
            print(f'Title: {book.title}, Author: {book.author}, Status: {status}')

    def save_books(self):
        with open(self.filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Author', 'Status'])
            for book in self.books:
                writer.writerow(book.to_list())

    def load_books(self):
        #wignebis loadis funqcia
        books = []
        try:
            with open(self.filepath, 'r') as file:
                reader = csv.reader(file)
                try:
                    next(reader)
                except StopIteration:
                    return books
                for row in reader:
                    book = Book('', '')
                    book.from_list(row)
                    books.append(book)
        except FileNotFoundError:
            pass #tu file ar arsebobs davpassavt
        return books

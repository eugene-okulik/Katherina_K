class Book:
    material_pages = 'paper'
    presence_text = True

    def __init__(self, title, author, pages_number, isbn, reserved):
        self.title = title
        self.author = author
        self.pages_number = pages_number
        self.isbn = isbn
        self.reserved = reserved


book_1 = Book('Don Quixote', 'Miguel de Cervantes', 580, 9992158111, True)
book_2 = Book('Lord of the Rings', 'J.R.R. Tolkien', 345, 9992158112, False)
book_3 = Book('Harry Potter and the Sorcerer Stone', 'J.K. Rowling', 543, 9992158113, False)
book_4 = Book('And Then There Were None', 'Agatha Christie', 290, 9992158114, False)
book_5 = Book('Twenty Thousand Leagues Under the Sea', 'Jules Verne', 389, 9992158115, False)

all_books = [book_1, book_2, book_3, book_4, book_5]

for book in all_books:
    if book.reserved:
        print(
            f"Title: {book.title}, Author: {book.author}, pages: {book.pages_number}, "
            f"material: {book.material_pages}, reserved"
        )
    else:
        print(
            f"Title: {book.title}, Author: {book.author}, pages: {book.pages_number}, material: {book.material_pages}"
        )

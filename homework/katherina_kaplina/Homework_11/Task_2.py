class Book:
    material_pages = 'paper'
    presence_text = True

    def __init__(self, title, author, pages_number, isbn, reserved):
        self.title = title
        self.author = author
        self.pages_number = pages_number
        self.isbn = isbn
        self.reserved = reserved


class SchoolBook(Book):

    def __init__(self, title, author, pages_number, isbn, reserved, subject, grade, presence_tasks):
        super().__init__(title, author, pages_number, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.presence_tasks = presence_tasks


school_book_1 = SchoolBook('Algebra', 'Ivanov', 100, 9992150001, True, 'Maths', 2, True)
school_book_2 = SchoolBook('Geometry', 'Petrov', 200, 9992150002, False, 'Maths', 5, False)
school_book_3 = SchoolBook('Physics', 'Sidorov', 300, 9992150003, False, 'Physics', 2, True)


all_school_books = [school_book_1, school_book_2, school_book_3]

for school_book in all_school_books:
    if school_book.reserved:
        print(
            f"Title: {school_book.title}, Author: {school_book.author}, pages: {school_book.pages_number}, "
            f"subject: {school_book.subject}, grade: {school_book.grade}, reserved"
        )
    else:
        print(
            f"Title: {school_book.title}, Author: {school_book.author}, pages: {school_book.pages_number}, "
            f"subject: {school_book.subject}, grade: {school_book.grade}"
        )

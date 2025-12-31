# Create a class Book with:
# instance attributes title, author
# a class variable total_books
# a class method from_string(cls, book_str) that creates an object from "title-author" format
# a static method is_valid_title(title) that checks if title has at least 3 characters
# increment total_books for every book created
# Demonstrate:
# Creating books using both the constructor and the class method
# Validating titles before creation

class Book:
    total_books = 0
    def __init__(self,title,author):
        if Book.is_valid_title(title):
            self.title = title
            self.author = author
            print(f'{title}-{author}'
                  )
            Book.total_books += 1
            print(Book.total_books)

        else:
            print("not a valid title")

    @classmethod
    def form_string(cls,book_str):
        # print(f"{cls.title}-{cls.author}")
        t, a = book_str.split('-')
        return cls(t,a) #calls init method

    @staticmethod
    def is_valid_title(title):
        c = 0
        for t in title:
            c += 1
        if c >= 3:
            return True
        else:
            return False


b = Book("Ramayana","Valmiki")

b1 = Book.form_string("Ramayana-Valmiki")




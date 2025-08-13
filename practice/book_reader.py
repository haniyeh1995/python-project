
book_title = input("Enter your book'name: \n")
book_author = input("Enter your book'author: \n")
book_total_pages = int(input("Enter your book'total_pages: \n"))

class Book:
    def __init__(self, title, author, total_pages, current_page = 1):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page
    
    def read(self, pages): 
        if self.current_page + pages >= self.total_pages:
           self.current_page = self.total_pages
           print(f"you've already finish the book! the book has {self.current_page} pages")
        else:
            self.current_page += pages
            print(f"you are at page {self.current_page}")
    
    def bookmark(self):
        print(f"you are at page {self.current_page} right now")
    
    def page_remaining(self):
        remain = self.total_pages - self.current_page 
        print(f"{remain} pages of your book remains")

    def book_info(self):
        print(f"You are currently reading '{self.title}' by {self.author}. Page {self.current_page}/{self.total_pages}")


my_book = Book(book_title, book_author, book_total_pages)
read_pages = int(input("how many pages of your book do you read now? \n"))
my_book.read(read_pages)
my_book.bookmark()
my_book.page_remaining()
my_book.book_info()

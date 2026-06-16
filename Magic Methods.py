#Magic Methods in Python or Dunder Methods

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.num_pages == other.num_pages

    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            raise KeyError(f"{key} is not a valid attribute of Book")
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("1984", "George Orwell", 328)

print(book1)  # Output: The Great Gatsby by F. Scott Fitzgerald
print(book2)  # Output: To Kill a Mockingbird by Harper Lee
print(book3)  # Output: 1984 by George Orwell
print("")
print(book1 == book2)  # Output: False
print(book1 == book3)  # Output: False
print(book2 == book3)  # Output: False
print("")
print(book1 < book2)  # Output: True
print(book2 < book3)  # Output: True
print(book1 < book3)  # Output: True
print("")
print(book1> book2)  # Output: False
print(book2 > book3)  # Output: False
print(book3 > book1)  # Output: True
print("")
print(book1 + book2)  # Output: 461
print(book2 + book3)  # Output: 609
print(book1 + book3)  # Output: 508
print("")
print("Gatsby" in book1)  # Output: True
print("Bott" in book2)  # Output: False
print("1984" in book3)  # Output: True
print("")
print(book1["title"])  # Output: The Great Gatsby
print(book2["author"])  # Output: Harper Lee
print(book3["num_pages"])  # Output: 328
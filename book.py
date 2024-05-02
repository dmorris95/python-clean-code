#Task 1

class Book:
    def __init__(self, title, author, genre, price):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__price = price
        self.stock_number = 10

    #getters & setters for values
    def get_book_title(self):
        return self.__title
    def set_book_title(self, new_title):
        if new_title == "":
            print("The new title must not be blank!")
        else:
            self.__title = new_title

    def get_book_author(self):
        return self.__author
    def set_book_author(self, new_author):
        if new_author == "":
            print("The new author must not be blank!")
        else:
            self.__author = new_author

    def get_book_genre(self):
        return self.__genre
    def set_book_genre(self, new_genre):
        if new_genre == "":
            print("The books new genre must not be blank!")
        else:
            self.__genre = new_genre

    def get_book_price(self):
        return self.__price
    def set_book_price(self, new_price):
        if new_price == "":
            print("The books new price must not be blank!")
        else:
            self.__price = new_price
    
    def get_book_stock_number(self):
        return self.stock_number
    #set stock if new stock of book came in
    def set_book_stock_number(self, new_stock):
        if new_stock == "":
            print("The books new stock not be blank!")
        else:
            self.stock_number = new_stock

    #Function to remove books from stock based on the requested quantity
    def remove_from_stock(self, quantity=1):
        if self.stock_number <= 0 or (self.stock_number - quantity) < 0:
            print(f"Sorry, we don't have that many of '{self.get_book_title()}', please try a different amount or a differnet book!")
        else:
            self.stock_number = self.stock_number - quantity
    
book1 = Book("A New Day", "George Georges", "Fantasy", "5.99")
book1.remove_from_stock()
print(book1.get_book_stock_number())

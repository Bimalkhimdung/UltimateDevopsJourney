class book:
    def __init__(self,name,author,publish):
        self.name = name 
        self.author = author
        self.publish = publish 
    
    def __str__(self):
        return f"Name of book is {self.name} Who's Author is {self.author} Published in {self.publish}"
    
book_ = book("Sufi","Subin Bhattrai",2020)

print(book_)
class Book:
    def __init__(self, title, price=0.0, page_count=0):
        # print(f'Book.__init__() called with self as {self}')
        self.title = title
        self.price = price
        self.page_count = page_count

    def __str__(self):
        return f'Title="{self.title}", Price={self.price}, Pages={self.page_count}'


if __name__ == '__main__':
    # in java --> Book b1 = new Book()
    b1 = Book()
    # 1. python runtime allocates memory required for an empty 'object'
    # 2. calls the __init__ of the class by passing the reference of the newly constructed object along with any
    #    additional parameters passed while creating an object. Generally, the parameters passed will be added
    #    as data members of the object (e.g, self.title = title). This is where the object is growing in terms of
    #    attributes (member data)
    # 3. new constructed object's reference is returned and assigned to b1
    b2 = Book('let us python', 1999, 450)
    b3 = Book('java unleashed')

    # print(f'b1 is an object of {type(b1)} and b1 is {b1}')
    print(b1)  # print(b1.__str__())   # Book.__str__(b1)
    print(b2)
    print(b3)

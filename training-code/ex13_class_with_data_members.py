class Book:
    # shared across all instances of this class, like a static member
    available_genres = ['comedy', 'drama', 'romance', 'programming']

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.price = kwargs.get('price', 0.0)
        self.page_count = kwargs.get('page_count', 0)
        self.genre = kwargs.get('genre')
        if self.genre is None:
            self.genre = Book.available_genres[0]
        elif self.genre not in Book.available_genres:
            raise ValueError(f'Invalid genre supplied. Must be one of {Book.available_genres}')

    def __str__(self):
        return f'Title="{self.title}", Price={self.price}, Pages={self.page_count}, Genre={self.genre}'


if __name__ == '__main__':
    b1 = Book(title='Gods must be crazy', price=200)
    print(b1)

    # pprint(dir(b1))
    b2 = Book(title='let us C', genre='programming')
    # pprint(dir(b2))
    b1.available_genres.append('crime')  # affects b2.available_genres too
    print(b1.available_genres)
    print(b2.available_genres)


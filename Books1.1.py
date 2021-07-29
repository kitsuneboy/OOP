# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
# издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
# равенство и неравенство, методы __repr__ и __str__.

class BookDescription:

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def print_info(self):
        print("Автор: ", self.author)
        print("Название: ", self.title)
        print("Год издания: ", self.year)
        print("Жанр :", self.genre)

    def __repr__(self):
        return 'Book %s, %s, %d, %s' % (self.author, self.title, self.year, self.genre)

    def __str__(self):
        return 'The book %s, %s, %d, %s' % (self.author, self.title, self.year, self.genre)

    def __eq__(self, other):
        if self.author != other.author:
            return False
        elif self.title != other.title:
            return False
        elif self.year != other.year:
            return False
        elif self.genre != other.genre:
            return False
        else:
            return True


book1 = BookDescription("Марио Пьюзо", "Крёстный отец", 1969, "драма")
book2 = BookDescription("Александр Дюма", "Граф Монте-Кристо", 1844, "исторический роман")
book3 = BookDescription("Александр Дюма", "Граф Монте-Кристо", 1844, "исторический роман")

book1.print_info()
print()
book2.print_info()
print()
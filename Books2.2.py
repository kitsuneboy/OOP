# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.

class BookRew:

    def __init__(self, user, rewiew):
        self.user = user
        self.rewiew = rewiew

    def __str__(self):
        return 'Rewiews: %s says "%s"' % (self.user, self.rewiew)


class Book:

    def __init__(self, author, title, rewiews):
        self.author = author
        self.title = title
        self.rewiews = rewiews

    def __str__(self):
        return 'Book: %s - %s  %s' % (self.author, self.title, self.rewiews)


rewiew1 = BookRew("Alex", "Good")
rewiew2 = BookRew("Matt", "Fantastic")
book1 = Book("Марио Пьюзо", "Крёстный отец", rewiew1)
book2 = Book("Александр Дюма", "Граф Монте-Кристо", rewiew2)
print(book1)
print(book2)


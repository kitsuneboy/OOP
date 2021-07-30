# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.

class BookRewiew:
    feedback_list = "Good!"
    feedback_list1 = "Gooood!"
    feedback_list2 = "Okay!"


class Book(BookRewiew):

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
        print()
        print("Cписок отзывов:", self.feedback_list, self.feedback_list1, self.feedback_list2, sep=" | ")


book1 = Book("Марио Пьюзо", "Крёстный отец", 1969, "драма")
book1.print_info()


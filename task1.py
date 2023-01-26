class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name_atr(self):
        return self.name

    @property
    def autor_atr(self):
        return self.author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages_atr = pages

    @property
    def pages_atr(self) -> int:
        return self._pages

    @pages_atr.setter
    def pages_atr(self, pages: int) -> None:
        if isinstance(pages, int):
            self._pages = pages
        else:
            raise ValueError("Число страниц должно быть типа int")
        if pages >= 0:
            self._pages = pages
        else:
            raise ValueError("Число страниц в книге должно быть положительное")

    def __str__(self):
        return f"Бумажная книга: '{self.name}'. Автор: {self.author}. Количество страниц: {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration_atr = duration

    @property
    def duration_atr(self) -> float:
        return self._duration

    @duration_atr.setter
    def duration_atr(self, duration) -> None:
        if isinstance(duration, float):
            self._duration = duration
        else:
            raise ValueError("Продолжительность книги должна быть типа float")
        if duration > 0:
            self._duration = duration
        else:
            raise ValueError("Продолжительность книги должна быть положительным числом")


    def __str__(self):
        return f"Аудио книга: '{self.name}'. Автор: {self.author}. Продолжительность книги: {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._duration!r})"



book1 = PaperBook("Война и мир", "Толстой", 800)
print(PaperBook.__repr__(book1))
print(PaperBook.__str__(book1))
book2 = AudioBook("1984", "Джордж Оруэлл", 1345.80)
print(AudioBook.__str__(book2))
print(AudioBook.__repr__(book2))
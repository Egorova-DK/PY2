# Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Door:
    def __init__(self, height: Union[int, float], width: Union[int, float]):
        """Создание и подготовка к работе объекта класса Door - дверь
        :param height: высота двери
        :param width: ширина двери

        Примеры:
        >>> door = Door(200, 60) # инициализация объекта
        """
        if height < 0:
            raise ValueError("Высота двери должна быть положительным числом")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота двери должна быть int или float")
        self.height = height

        if width < 0:
            raise ValueError("Ширина двери должна быть положительным числом")
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина двери должна быть int или float")
        self.width = width

    def open_door(self) -> bool:
        """Метод, который проверяет открыта ли дверь
        :return является ли дверь открытой
        Примеры:
        >>> door = Door(200,60)
        >>> door.open_door()
        """
        ...

    def the_presence_of_a_door_handle(self) -> bool:
        """Метод, который проверяет есть ли у двери ручка
        :return есть ли ручка у двери
        Примеры:
        >>> door = Door(200,60)
        >>> door.the_presence_of_a_door_handle()
        """
        ...


class TV:

    def __init__(self, diagonal: Union[int, float], mark: str, volume: int):
        """
        Создание и подготовка к работе объекта класса TV - телевизор
        :param diagonal: диагональ экрана телевизора;
        :param mark: бренд телевизора;
        :param volume: громкость телевизора;
        Примеры:
        >>> television = TV(40,"Phillips",12) # инициализация объекта
        """
        if diagonal < 0:
            raise ValueError("Диагональ экрана телевизора должна быть положительным числом")
        if not isinstance(diagonal, (int, float)):
            raise TypeError("Диагональ экрана телевизора должна быть int или float")
        self.diagonal = diagonal

        if not isinstance(mark, str):
            raise TypeError("Бренд телевизора должен быть типа str")
        self.mark = mark

        if volume < 0:
            raise ValueError("Громкость телевизора должна быть положительным числом")
        if not isinstance(volume, int):
            raise TypeError("Громкость телевизора должен быть типа int")
        self.volume = volume

    def increase_the_volume(self, volume: int) -> None:
        """Метод, который увеличивает громкость телевизора
        :raise ValueError: Если значение громкости больше возможного для данного телевизора, то вызовем ошибку
        Примеры:
         >>> television = TV(40,"Philips",12)
         >>> television.increase_the_volume(18)
         """
        if volume < 0:
            raise ValueError("Громкость телевизора должна быть положительным числом")
        if not isinstance(volume, int):
            raise TypeError("Новое значение громкости телевизора должно быть типа int")
        self.volume = volume

    def turn_on_the_TV(self) -> None:
        """Метод, который включает телевизор
        Примеры:
        >>> television = TV(40,"Philips",15)
        >>> television.turn_on_the_TV()
        """
        ...


class Wallet:
    def __init__(self, material: str, color: str, value_money: Union[int, float]):
        """Создание и подготовка к работе объекта класса Wallet - кошелек
        :param material: материал, из которого изготовлен кошелек;
        :param color: цвет кошелька;
        :param value_money: количество денег в кошельке;
        Примеры:
        >>> wallet1 = Wallet("skin", "black", 100) # инициализация объекта
        """
        if not isinstance(material, str):
            raise TypeError("Материал кошелька должен быть типа str")
        self.material = material

        if not isinstance(color, str):
            raise TypeError("Цвет кошелька должен быть типа str")
        self.color = color

        if not isinstance(value_money, (int, float)):
            raise TypeError("Количество денег должно быть типом int или float")
        if value_money < 0:
            raise ValueError("Количество денег должно быть положительным числом или 0")
        self.value_many = value_money


    def add_money(self, add_value_money: Union[int, float]) -> None:
        """Метод, который добавляет деньги в кошелек
        Примеры:
        >>> wallet1 = Wallet("skin", "black", 120)
        >>> wallet1.add_money(50)
        """
        if add_value_money < 0:
            raise ValueError("Количество добавленных денег должно быть положительным числом")
        self.add_value_money = add_value_money

        ...

    def spend_money(self, spend_value_money: Union[float, int]) -> None:
        """Трата денег
        :raise ValueError: Если значение потраченных денег больше, чем имеется в кошельке, то вызовем ошибку
        Примеры:
        >>> wallet1 = Wallet("skin", "black", 50)
        >>> wallet1.spend_money(80)
        """
        if not isinstance(spend_value_money, (float, int)):
            raise TypeError("Количество потраченных денег должно быть типа int или float")
        if spend_value_money < 0:
            raise ValueError("Количество потраченных денег должно быть положительным числом")
        self.spend_value_money = spend_value_money
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass

if __name__ == "__main__":
    class Auto:
        def __init__(self, max_speed: float, brand: str):
            """Создание и подготовка к работе объекта класса Auto - автомобиль
            :param max_speed: максимально возможная скорость автомобиля
            :param brand: марка автомобиля
            Пример:
            >>> auto = Auto(220,"AUDI") # инициализация объекта
            """
            self.max_speed_atr = max_speed
            self.brand = brand

        @property
        def max_speed_atr(self) -> float:
            return self.max_speed

        @max_speed_atr.setter
        def max_speed_atr(self, max_speed: float) -> None:
            if max_speed > 0:
                self.max_speed = max_speed
            else:
                raise ValueError("Скорость должна быть положительным числом")

        def __str__(self):
            """Магический метод,отображающий информацию об объекте класса для пользователей"""
            return f"Автомобиль: '{self.brand}'. Максимальная скорость: {self.max_speed}."

        def __repr__(self):
            """Магический метод, предназначенный для представления того, как может быть инициализирован экземпляр класса.
            Представляет собой машинно-ориентированный вывод"""
            return f"{self.__class__.__name__}(brand={self.brand!r}, max speed={self.max_speed!r})"

        def amount_of_fuel(self, q: float, distance: float) -> float:
            """Метод,вычисляющий количество бензина, которое потребуется на поездку (км)
            :raise ValueError: Если объем двигателя и/или расстояние являются отрицательными числами
            :return требуемое количество бензина в литрах для поездки
            :param q: Объем двигателя
            :param distance: расстояние
            Примеры:
            >>> Auto.amount_of_fuel(3.5,300)
            """
            if q < 0 and distance < 0:
                raise ValueError("Объем двигателя и/или расстояение должны быть положительным числом")
            else:
                return round((q * distance) / 100, 2)


    class PassengerСar(Auto):
        def __init__(self, max_speed: float, brand: str, possible_number_of_passengers: int):
            """Создание и подготовка к работе объекта класса PassengerСar - легковой автомобиль
            :param max_speed: максимально возможная скорость автомобиля
            :param brand: марка автомобиля
            :param possible_number_of_passengers: максимально возможное количество пассажиров в автомобиле
            Пример:
            >>> auto = PassengerСar(210,"NISSAN",5) # инициализация объекта
            """
            super().__init__(max_speed, brand)
            self.possible_number_of_passengers_atr = possible_number_of_passengers

        @property
        def possible_number_of_passengers_atr(self) -> int:
            return self.possible_number_of_passengers

        @possible_number_of_passengers_atr.setter
        def possible_number_of_passengers_atr(self, possible_number_of_passengers) -> None:
            if possible_number_of_passengers > 0:
                self.possible_number_of_passengers = possible_number_of_passengers
            else:
                raise ValueError("Максимально возможное число пассажиров должно быть положительным числом")


    def __str__(self):
        """Метод был перегружен из-за дополнительного аргумента при инициализации экземпляра класса possible_number_of_passengers(Максимально возможное число пассажиров)"""
        return f"Автомобиль: '{self.brand}'. Максимальная скорость: {self.max_speed}. Максимально возможное число пассажиров: {self.possible_number_of_passengers}"


    def __repr__(self):
        """Метод был перегружен из-за дополнительного аргумента при инициализации экземпляра класса possible_number_of_passengers(Максимально возможное число пассажиров)"""
        return f"{self.__class__.__name__}(brand={self.brand!r}, max speed={self.max_speed!r}, possible_number_of_passengers={self.possible_number_of_passengers!r})"

    class Track(Auto):
        def amount_of_fuel(self, q, q1, distance, workload, allowance):
            """Метод,вычисляющий количество бензина, которое потребуется грузовому автомобилю
            :param q: норма расхода топлива на пробег автомобиля в снаряженном состоянии без груза;
            :param q1: норма расхода топлив на транспортную работу, л/100 т·км;
            :param distance: пробег автомобиля, км;
            :param workload:объем транспортной работы;
            :param allowance: поправочный коэффициент;
            Метод родительского класса перегружен, потому что расчет топлива для грузового автомобиля производится по другой формуле с дополнительными параметрами
            """
        ...


pass

auto1 = Auto(200, "BMW")
print(auto1.__str__())
print(auto1.__repr__())
auto2 = Auto(230, "FIAT")
print(auto2.amount_of_fuel(3.5, 5563))
auto3 = PassengerСar(210, "FORD", 5)
print(auto3.__str__())
print(auto3.__repr__())
print(auto3.amount_of_fuel(2.8, 6723))
auto4 = Track(180, "CAT")
print(auto4.__str__())
print(auto4.__repr__())

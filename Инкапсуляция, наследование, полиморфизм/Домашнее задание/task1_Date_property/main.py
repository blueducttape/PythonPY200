class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        return True if (year % 4 == 0) else False

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year):
            return self.DAY_OF_MONTH[1][month - 1]
        else:
            return self.DAY_OF_MONTH[0][month - 1]

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        if not (isinstance(day, int) & isinstance(month, int) & isinstance(year, int)):
            raise TypeError('Вводите целочисленные значения')
        if not ((1 <= day <= 31) & (1 <= month <= 12) & (year >= 0)):
            raise ValueError('Превышен диапазон возможных значений!')
        if not (day <= self.DAY_OF_MONTH[0][month - 1] or day <= self.DAY_OF_MONTH[1][month - 1]):
            raise ValueError('Проверьте корректность введенных данных')
        if self.get_max_day(month, year) < day:
            raise ValueError('В этом месяце не может быть так много дней')
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value: int):
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value: int):
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


if __name__ == "__main__":
    date1 = Date(2, 2, 2022)
    print(date1)

    date2 = Date(20, 12, -2020)
    print(date2)

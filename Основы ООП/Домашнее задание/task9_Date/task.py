class Date:
    def __init__(self, day: int, month: int, year: int):
        self.check_type_error(day)
        self.day = day
        self.check_type_error(month)
        self.month = month
        self. check_type_error(year)
        self.year = year


    @staticmethod
    def check_type_error(value: int) -> None:
        if not isinstance(value, int):
            raise TypeError

    def __repr__(self):
        return f'Date({self.day}, {self.month}, {self.year})'

    def __str__(self):
        return f'{self.day:0>2}/{self.month:0>2}/{self.year}'

date = Date(1,2,1999)

print(date)
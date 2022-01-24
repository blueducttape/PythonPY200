import typing


class Calc:

    @staticmethod
    def calc_sum(a, b):
        if not isinstance(a, (int, float)):
            raise TypeError
        if not isinstance(b, (int, float)):
            raise TypeError
        return a+b

    @staticmethod
    def _zero_division (a):
        print("Все равно не работает")

    @staticmethod
    def check_type(value, type:typing.Union[type, tuple]):
        if not isinstance(value, type):
            raise TypeError


if __name__ =='__main__':
    print(Calc().calc_sum(1, 2))
    print(Calc()._zero_divison(5))
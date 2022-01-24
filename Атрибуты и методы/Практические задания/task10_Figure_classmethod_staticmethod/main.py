import math


def area_by_angle(a, b, angle):
    """ Формула площади по двум сторонам и углу между ними. """
    return 0.5 * a * b * math.sin(angle)


def area_by_height(a, h):
    """ Формула площади по основанию и высоте. """
    return 0.5 * a * h


class TriangleCalculator:
    """ Класс-калькулятор площадей треугольников. """
    @staticmethod
    def area(*args):
        """
        Метод, который считает площадь по разным формулам,
         в зависимости от количества переданных аргументов.
        """
        if len(args) == 2:
            return area_by_height(*args)
        if len(args) == 3:
            return area_by_angle(*args)


if __name__ == '__main__':
    TriangleCalculator.area(5, 10)  # Работаем через экземпляр
    TriangleCalculator.area(10,5)  # Работаем через класс

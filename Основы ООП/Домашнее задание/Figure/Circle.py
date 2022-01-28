import matplotlib.pyplot as plt
import math


class Circle(object):

    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Увеличить радиус окружности
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

    # длина окружности
    def get_length(self):
        return 2*math.pi*self.radius

    # площадь окружности
    def get_area(self):
        return math.pi * (self.radius ** 2)

    # нарисовать круг
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

    def __repr__(self):
        return f'Circle(Окружность радиусом {self.radius})'


if __name__ == "__main__":
    c1 = Circle(10, 'red')
    c2 = Circle(34, '#000000')
    print(c1)
    c1.drawCircle()
    print(c2)
    c2.drawCircle()
    print(c1.get_area())
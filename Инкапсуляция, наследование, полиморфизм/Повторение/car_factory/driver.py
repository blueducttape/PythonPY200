class Driver:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return f"Водитель{self.name}"

    def driver_experience(self):
        pass


if __name__ == '__main__':
    driver_vasya = Driver('Василий')
    driver_ivan = Driver('Иван')
import hashlib
import random
import time
import uuid
from driver import Driver
import datetime

from typing import Union


class DriverTypeError(Exception):
    pass


class EngineIsNotRunning(Exception):   # двигатель не запущен
    pass


class DoTechnicalDiscussion(Exception):    # ТО не пройден
    pass


class DriverNotFoundError(Exception):    # водитель не найден
    pass


class EngineIsRunning(Exception):     # двигатель запущен
    pass


class Car:
    brand = None
    _max_speed = 180
    __created_car = 0

    def __init__(self, engine_type=None, body_type=None, gear_type=None,
                 drive_type=None, configuration=None, color=None) -> None:

        self.__body_type = body_type    # тип кузова
        self._engine_type = engine_type     # тип двигателя
        self._gear_type = gear_type     # тип коробки передач
        self._drive_type = drive_type   # тип привода
        self.configuration = configuration  # комплектация
        self.color = color  # цвет

        self.__vin_number = uuid.uuid4()    # vin (идентификационный номер транспортного средства)
        self.__created_time = time.time()   #
        self.__mileage = 0      # пробег

        self.__status_engine = False    # статус двигателя
        self.__driver = None    # водитель
        self.__last_to = 0  # пробег на котором было сделано последнее ТО
        self.__service_interval = 30  # необходимая частота ТО

        self.car_key = None  # ключ который хранится в машине, и сверяется с ключом водителя
        self.__keys_was_send = False  # переменная которая проверяет выдавались ли ключи

    def __new__(cls, *args, **kwargs) -> None:   # новые объекты класса
        cls.__append_new_car_counter()
        print(f"Создано {cls.__created_car} машин класса {cls.__name__}")
        return super().__new__(cls)

    # =============
    # Методы класса
    # =============
    @classmethod
    def change_brand(cls, new_brand) -> None:    # изменить марку машины
        cls.brand = new_brand

    @classmethod
    def _set_max_speed(cls, max_speed) -> None:  # установка максимальной скорости
        if not isinstance(max_speed, (int, float)):
            raise TypeError(
                f'Ожидается тип {int} или {float}, получен {type(max_speed)}')
        cls._max_speed = max_speed

    @classmethod
    def __append_new_car_counter(cls) -> None:
        """
        счетчик объектов класса
        """
        cls.__created_car += 1

    def start_engine(self, key) -> None:    # запуск двигателя
        if self.__check_keys(key):
            self.__status_engine = True
            print('Машина завелась')
        else:
            print('Крутится стартер')

    def __is_ready_move(self) -> bool:
        """
        проверяет готовность автомобиля к движению
        """
        if not self.__status_engine:
            raise EngineIsNotRunning("двигатель не запущен")
        if self.__driver is None:
            raise DriverNotFoundError("водитель не найден")

        return True

    def __create_keys(self) -> str:    # создание ключа
        h = hashlib.new('sha256')
        vin = str(self.__vin_number).encode('utf-8')
        h.update(vin)
        self.car_key = h.hexdigest()
        return self.car_key

    def get_keys(self) -> str:  # проверяет, выданы ли ключи
        """Ключи выдаются только 1 раз"""
        if self.__keys_was_send:
            print('Ключи уже были выданы')
        else:
            self.__keys_was_send = True
            return self.__create_keys()

    def __check_keys(self, key) -> bool:    # проверяет, подходят ли ключи
        if self.car_key == key:
            return True
        else:
            print('Ключи не подходят')
            return False

    def __check_limitations(self, m_time: [int, float], dist: int) -> None:
        """
        Проверка текущей поездки на ограничения водителя
        :param m_time: время в пути в минутах
        :param dist: пройденный путь в км
        """
        if self.driver.get_max_time_in_move() <= m_time:
            print(f"Ограничение по времени прибывания за рулем! Срочно отдохните! "
                  f"P.S. Ваше ограничение {self.driver.get_max_time_in_move() / 60} часа")
        if self.driver.get_max_allowed_speed() > (dist / (m_time / 60)):
            print(f"Вы превышаете максимально разрешенную скрость! "
                  f"Ваше ограничение {self.driver.get_max_allowed_speed()} км/ч")
        if self.driver.dist_limit % dist == 0:
            print(f"Ограничение по пройденной дистанции без отдыха! Отдохните! "
                  f"P.S. Ваше ограничение {self.driver.dist_limit} км")

    def move(self, distance=10) -> None:
        """
        функция движения
        :param distance: расстояние в км
        """
        try:
            if self.__is_ready_move():
                for i in range(distance):
                    if self.check_technical_discussion():
                        self.move_direction(random.randint(0, 10))
                        print(f'Машина проехала {i + 1} км.')
                        self.__mileage += 1
                        time.sleep(0.1)

                        if self.__mileage % 20 == 0:
                            a = 3
                            print(f'Вам необходимо отдохнуть. Вы можете продолжить движение через {a} минут(ы)')
                            time.sleep(a)

                    else:
                        raise DoTechnicalDiscussion("Срочно необходимо сделать ТО")
            print('Машина проехала указанный путь')
        except (EngineIsNotRunning, DriverNotFoundError) as e:
            print(f"Машина не может поехать, т.к. {e}")

    # ==================
    # Статические методы
    # ==================
    @staticmethod
    def move_direction(direction) -> None:  # выбирает направление движения
        direction_dict = {0: "прямо", 1: "налево", 2: "направо", 3: "разворот"}
        print(f"Автомобиль выполняет движение: {direction_dict.get(direction, 'прямо')}")

    #        print(f"Угол поворота = {angle}")
    #    if angle < -180:
    #        print("Поворот налево")
    #    elif angle == 0:
    #        print ("Автомобиль едет прямо")
    #    elif angle < 180:
    #        print("Поворот направо ")
    #    elif angle >= 180:
    #        print("Разворот")

    # Эквивалент свойствам (property)
    # def set_driver(self, driver: Driver):
    #     if not isinstance(driver, Driver):
    #         raise DriverTypeError(f"Ожидается тип {Driver}, получен {type(driver)}")
    #     self.__driver = driver
    #
    # def get_driver(self):
    #     return self.__driver

    @property
    def driver(self) -> Driver:   # водитель
        return self.__driver

    @driver.setter
    def driver(self, driver: Driver) -> Driver | Exception:     # сеттер для водителя
        if not isinstance(driver, Driver):
            raise DriverTypeError(
                f"Ожидается тип {Driver}, получен {type(driver)}")
        self.__driver = driver

    def get_mileage(self) -> int:   # пробег
        return self.__mileage

    def _set_mileage(self, mileage) -> int | float:     # сеттер для пробега
        if not isinstance(mileage, (int, float)):
            raise TypeError(
                f'Ожидается тип {int} или {float}, получен {type(mileage)}')
        self.__mileage = mileage

    def check_technical_discussion(self) -> bool:   # проверка необходимости техосмотра
        if self.__mileage - self.__last_to == 40:
            return False
        elif self.__mileage - self.__last_to == 20:
            print(f"Необходимо сделать ТО через 10 км")
        elif self.__mileage - self.__last_to == self.__service_interval:
            print(f"Сейчас необходимо сделать ТО")
        return True

    def do_technical_discussion(self) -> str:   # ТО
        self.__last_to = self.__mileage
        print("Очередной ТО пройден")

    def autostart_engine(self) -> bool:     # автозапуск двигателя
        if not self.__status_engine:
            self.__status_engine = True
            return True
        else:
            EngineIsRunning("двигатель уже запущен")
            return False


class Honda(Car):
    brand = "Honda"

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    pass
    car = Car('бензин', 'седан', 'автомат', 'полный', 'люкс', 'белый')
    car_2 = Car('бензин', 'седан', 'автомат', 'полный', 'люкс', 'черный')
    #
    # honda1 = Honda('бензин', 'седан', 'автомат', 'полный', 'люкс', 'черный')
    # honda2 = Honda('бензин', 'седан', 'автомат', 'полный', 'люкс', 'черный')
    #
    # Car.change_brand("Kia")
    #
    # print(honda1.brand)

    # print(car.brand)
    # print(car_2.brand)
    # Car.change_brand("Nissan")
    # print(car.brand)
    # print(car_2.brand)

    # print(car._max_speed)
    # print(car_2._max_speed)
    # Car._set_max_speed(190)
    # print(car._max_speed)
    # print(car_2._max_speed)

    # Блок работы с защищёнными методами
    driver_key = car.get_keys()
    car.start_engine(driver_key)
    car.driver = Driver('Иван')
    # Блок работы с методами
    car.move()
    print(car.get_mileage())
    car.move()
    print(car.get_mileage())
    car.move_direction(3)

    #
    # car._set_mileage(30)
    # print(car.get_mileage())
    # car.move()
    # print(car.get_mileage())
    # car._set_mileage(10)
    # print(car.get_mileage())

    # Блок сеттеров
    # car.driver = Driver('Иван')
    # print(car.driver)
    # car.set_driver(Driver('Иван'))
    # print(car.get_driver())

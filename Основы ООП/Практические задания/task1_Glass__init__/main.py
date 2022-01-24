from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume(int,float)):
            raise TypeError
        if capacity_volume <= 0:
            raise TypeError

        if not isinstance(occupied_volume(int,float)):
            raise TypeError
        if capacity_volume < 0:
            raise TypeError
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass1 = Glass(200,100)  # TODO инициализировать два объекта типа Glass

    glass1 = Glass(200 , "100")

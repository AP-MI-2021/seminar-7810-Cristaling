from typing import Dict

import jsonpickle as jsonpickle

from Domain.Car import Car


class CarRepository:

    def __init__(self, filePath):
        self.filePath = filePath

    def __read_file(self):
        try:
            with open(self.filePath, 'r') as theFile:
                return jsonpickle.loads(theFile.read())
        except Exception:
            return {}

    def __write_file(self, objects: Dict[int, Car]):
        try:
            with open(self.filePath, 'w') as theFile:
                theFile.write(jsonpickle.dumps(objects))
        except Exception:
            pass

    def create(self, car: Car):
        cars = self.__read_file()

        if self.read(car.id) is not None:
            raise KeyError(f'Exista deja o masina cu id-ul {car.id}')

        cars[car.id] = car
        self.__write_file(cars)

    def read(self, carId: int):
        cars = self.__read_file()
        if carId:
            if carId in cars:
                return cars[carId]
            else:
                return None

        return list(cars.values())

    def update(self, car: Car):
        cars = self.__read_file()

        if self.read(car.id) is None:
            raise KeyError(f'Nu exista o masina cu id-ul {car.id}')

        cars[car.id] = car
        self.__write_file(cars)

    def delete(self, carId):
        cars = self.__read_file()

        if self.read(carId) is None:
            raise KeyError(f'Nu exista o masina cu id-ul {carId}')

        del cars[carId]
        self.__write_file(cars)
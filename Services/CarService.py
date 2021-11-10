from Domain.Car import Car
from Domain.CarValidator import CarValidator
from Repositories.CarRepository import CarRepository


class CarService:

    def __init__(self, carRepository: CarRepository, carValidator: CarValidator):
        self.carRepository = carRepository
        self.carValidator = carValidator

    def add(self, carId: int, comfortLevel: str, allowsCard: str, model: str):
        car = Car(carId, comfortLevel, allowsCard, model)
        self.carValidator.validate(car)
        self.carRepository.create(car)

    def update(self, carId: int, comfortLevel: str, allowsCard: str, model: str):
        car = Car(carId, comfortLevel, allowsCard, model)
        self.carValidator.validate(car)
        self.carRepository.update(car)

    def delete(self, carId: int):
        self.carRepository.delete(carId)

    def getCars(self):
        return self.carRepository.read()

    def getCar(self, carId):
        return self.carRepository.read(carId)
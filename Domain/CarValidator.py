from Domain.Car import Car


class CarValidator:
    def validate(self, car: Car):
        comfortLevels = ["standard", "ridicat", "premium"]
        allowsCardValues = ["da", "nu"]
        if car.comfort_level not in comfortLevels:
            raise ValueError(f'{car.comfort_level} is not an allowed value.')
        if car.allowsCard not in allowsCardValues:
            raise ValueError(f'{car.allowsCard} is not an allowed value.')

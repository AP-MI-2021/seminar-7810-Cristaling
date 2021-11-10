from Services.CarService import CarService


class Console:

    def __init__(self, carService: CarService):
        self.carService = carService

    def handleMenu(self):
        print("Hello Menu")
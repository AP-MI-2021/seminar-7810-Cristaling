# Scrieți folosind OOP un program pentru gestionarea unei firme de taxi. Vor fi suportate operațiile:
#
# CRUD mașină. O mașină are: indicativ, nivel confort (standard, ridicat, premium), plata cu cardul (da / nu), model.
# CRUD locație. O locație are: nume stradă, număr, bloc, scară, alte indicații.
# CRUD comenzi. O comandă are: id mașină, id locație, timp final, cost / km, distanță parcursă, status (în desfășurare, finalizată).
# Ordonarea străzilor descrescător după lungimea indicațiilor
# Ordonarea mașinilor crescător după costul mediu / km.
# Determinarea străzilor cu cele mai lungi comenzi (ca distanță).
# Alte rapoarte.
# Undo+Redo în mod eficient.
# Propunere de organizare pe iterații:
#
# Iterația 1: 1-3, repository-uri distincte, validatori.
# Iterația 2: 4-7, repository generic, excepții proprii.
# Iterația 3: 7-8, filter, map, lambda, list comprehensions, recursivitate etc.
# Folosiți arhitectură stratificată conform discuțiilor de la curs.
from Domain.CarValidator import CarValidator
from Repositories.CarRepository import CarRepository
from Services.CarService import CarService
from UserInterface.Console import Console


def main():

    carRepository = CarRepository("cars.json")

    carValidator = CarValidator()

    carService = CarService(carRepository, carValidator)

    console = Console(carService)
    console.handleMenu()


if __name__ == '__main__':
    # test()
    main()

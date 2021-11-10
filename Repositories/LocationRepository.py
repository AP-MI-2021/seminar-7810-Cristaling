from typing import Dict

import jsonpickle

from Domain.Location import Location


class LocationRepository:

    def __init__(self, filePath):
        self.filePath = filePath

    def __read_file(self):
        try:
            with open(self.filePath, 'r') as theFile:
                return jsonpickle.loads(theFile.read())
        except Exception:
            return {}

    def __write_file(self, objects: Dict[int, Location]):
        try:
            with open(self.filePath, 'w') as theFile:
                theFile.write(jsonpickle.dumps(objects))
        except Exception:
            pass

    def create(self, location: Location):
        locations = self.__read_file()

        if self.read(location.id) is not None:
            raise KeyError(f'Exista deja o locatie cu id-ul {location.id}')

        locations[location.id] = location
        self.__write_file(locations)

    def read(self, locationId: int):
        locations = self.__read_file()
        if locationId:
            if locationId in locations:
                return locations[locationId]
            else:
                return None

        return list(locations.values())

    def update(self, location: Location):
        locations = self.__read_file()

        if self.read(location.id) is None:
            raise KeyError(f'Nu exista o locatie cu id-ul {location.id}')

        locations[location.id] = location
        self.__write_file(locations)

    def delete(self, locationId):
        locations = self.__read_file()

        if self.read(locationId) is None:
            raise KeyError(f'Nu exista o locatie cu id-ul {locationId}')

        del locations[locationId]
        self.__write_file(locations)
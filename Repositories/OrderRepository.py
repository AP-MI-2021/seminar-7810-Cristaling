from typing import Dict

import jsonpickle as jsonpickle

from Domain.Order import Order


class OrderRepository:

    def __init__(self, filePath):
        self.filePath = filePath

    def __read_file(self):
        try:
            with open(self.filePath, 'r') as theFile:
                return jsonpickle.loads(theFile.read())
        except Exception:
            return {}

    def __write_file(self, objects: Dict[int, Order]):
        try:
            with open(self.filePath, 'w') as theFile:
                theFile.write(jsonpickle.dumps(objects))
        except Exception:
            pass

    def create(self, order: Order):
        orders = self.__read_file()

        if self.read(order.id) is not None:
            raise KeyError(f'Exista deja o masina cu id-ul {order.id}')

        orders[order.id] = order
        self.__write_file(orders)

    def read(self, orderId: int):
        orders = self.__read_file()
        if orderId:
            if orderId in orders:
                return orders[orderId]
            else:
                return None

        return list(orders.values())

    def update(self, order: Order):
        orders = self.__read_file()

        if self.read(order.id) is None:
            raise KeyError(f'Nu exista o masina cu id-ul {order.id}')

        orders[order.id] = order
        self.__write_file(orders)

    def delete(self, orderId):
        orders = self.__read_file()

        if self.read(orderId) is None:
            raise KeyError(f'Nu exista o masina cu id-ul {orderId}')

        del orders[orderId]
        self.__write_file(orders)
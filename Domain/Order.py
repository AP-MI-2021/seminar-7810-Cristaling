from dataclasses import dataclass


@dataclass(init=True)
class Order:
    id: int
    carId: int
    locationId: int
    totalTime: int
    costPerKm: float
    travelDistance: float
    status: str

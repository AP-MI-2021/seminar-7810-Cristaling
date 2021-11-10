from dataclasses import dataclass


@dataclass(init=True)
class Car:
    id: int
    comfort_level: str
    allowsCard: str
    model: str

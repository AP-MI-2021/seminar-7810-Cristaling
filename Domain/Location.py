from dataclasses import dataclass


@dataclass(init=True)
class Location:
    id: int
    streetName: str
    streetNr: int
    blockNr: str
    model: str
    entranceNr: str

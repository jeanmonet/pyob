from dataclasses import dataclass

@dataclass
class Coordinate:
    lat: float
    long: float

    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'EW'[self.long < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.long):.1f}°{we}'


sp = Coordinate(-23, 'bla')

print(sp)


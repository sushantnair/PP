from abc import ABC, abstractmethod
from operator import methodcaller
class Vehicle(ABC):
    @abstractmethod
    def speed(self, name, spd):
        pass
class FourWheeler(Vehicle):
    def speed(self, name, spd):
        self.name = name
        self.spd = spd
        print(self.name, self.spd)
class TwoWheeler(Vehicle):
    def speed(self, name, spd):
        self.name = name
        self.spd = spd
        print(self.name, self.spd)
f_w = FourWheeler()
t_w = TwoWheeler()
f_w.speed("Maruti Suzuki Alto 800\t", 100)
t_w.speed("TVS\t", 150)
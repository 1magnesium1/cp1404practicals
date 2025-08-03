import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialized version of car that includes reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise unreliable car"""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """Drive the unreliable car"""
        random_number = random.randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven


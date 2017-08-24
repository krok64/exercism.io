from decimal import *

class SpaceAge(object):
    def __init__(self, seconds):
        getcontext().prec = 1000
        self.seconds = Decimal(seconds)

    def on_earth(self):
        return round(self.seconds / Decimal(31557600), 2)

    def on_mercury(self):
        return self.get_year(0.2408467)

    def on_venus(self):
        return self.get_year(0.61519726)

    def on_mars(self):
        return self.get_year(1.8808158)

    def on_jupiter(self):
        return self.get_year(11.862615)

    def on_saturn(self):
        return self.get_year(29.447498)

    def on_uranus(self):
        return self.get_year(84.016846)

    def on_neptune(self):
        return self.get_year(164.79132)

    def get_year(self, num):
        return round(Decimal(self.seconds) / Decimal(31557600) / Decimal(num), 2)


from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of taxi that includes new attribute fanciness"""

    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Create instance of silver service taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Returns string output of silver service taxi instance"""
        return f"{super().__str__()} includes flag fall of ${self.flag_fall}"

    def get_fare(self):
        """Gets fare"""
        return self.flag_fall + super().get_fare()

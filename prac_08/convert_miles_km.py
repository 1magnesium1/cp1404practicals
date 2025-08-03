"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to km
Started 27/07/25
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesToKilometersApp(App):
    """"Miles to kilometer app is a kivy app that converts miles to kilometers"""
    output_km = StringProperty()

    def build(self):
        """Builds the kivy app layout"""
        self.title = "Miles to Kilometers App"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, text):
        """Handles the conversion from miles to kilometers"""
        miles = self.convert_to_number(text)
        kilometers = miles * FACTOR_MILES_TO_KM
        self.root.ids.output_label.text = str(kilometers)

    def handle_increment(self, text, change):
        """Allows the user to use up and down button to change the entered value by one"""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    @staticmethod
    def convert_to_number(text):
        """Convert a string to a float or 0.0 if invalid."""

        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKilometersApp().run()

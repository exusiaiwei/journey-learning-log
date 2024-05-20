class SpaceAge:
    # Class constructor that initializes an instance with seconds.
    def __init__(self, seconds):
        # Set the initial seconds and calculate the earth year (31557600).
        self.seconds = seconds
        self.earth_year = 31557600

        # Initialize a dictionary for orbital periods of different planets.
        self.orbital_periods = {
            'Mercury': 0.2408467,
            'Venus': 0.61519726,
            'Earth': 1.0,
            'Mars': 1.8808158,
            'Jupiter': 11.862615,
            'Saturn': 29.447498,
            'Uranus': 84.016846,
            'Neptune': 164.79132
        }

    # Method to calculate the age on Earth.
    def on_earth(self):
        return round(self.seconds / (self.earth_year * self.orbital_periods['Earth']), 2)

    # Method to calculate the age on Mercury.
    def on_mercury(self):
        return round(self.seconds / (self.earth_year * self.orbital_periods['Mercury']), 2)

    # Method to calculate the age on Venus.
    def on_venus(self):
        return round(self.seconds / (self.earth_year * self.orbital_periods['Venus']), 2)

    # Method to calculate the age on Mars.
    def on_mars(self):
        return round(self.seconds / (self.earth_year * self.orbital_periods['Mars']), 2)

    # Method to calculate the age on Jupiter.
    def on_jupiter(self):
        return round(self.seconds / (self.earth_year * self.orbital_periods['Jupiter']), 2)

    # Method to calculate the age on Saturn.
    def on_saturn(self):
        return round(self.seconds / (self.earth_year * self.orbital_periods['Saturn']), 2)

    # Method to calculate the age on Uranus.
    def on_uranus(self):
        return round(self.seconds / (self.earth_year * self.orbital_periods['Uranus']), 2)

    # Method to calculate the age on Neptune.
    def on_neptune(self):
        return round(self.seconds / (self.earth_year * self.orbital_periods['Neptune']), 2)

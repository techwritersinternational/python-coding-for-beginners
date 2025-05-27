class Spacecraft:
    def __init__(self):
        self.fuel = 0
        self.oxygen = 0
        self.systems_check = False

    def load_fuel(self, amount):
    
        if not (amount < 0):
            self.fuel += amount

        if self.fuel > 100:
            self.fuel = 100

    def load_oxygen(self, amount):
        if not (amount < 0):
            self.oxygen += amount

        if self.oxygen > 100:
            self.oxygen = 100

    def check_systems(self):
        if self.fuel >= 50 and self.oxygen >= 60:
            self.systems_check = True
        else:
            self.systems_check = False

    def launch(self):
        if self.fuel >= 80 and self.oxygen >= 90 and self.systems_check:
            return "Spacecraft launched successfully!"
        elif not self.systems_check:
            return "Launch failed: Systems check not passed."
        else:
            return "Launch failed: Insufficient fuel or oxygen."
class Spacecraft:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.location = "deep space"

    def travel_to(self, destination):
        self.location = destination.name
        return f"{self.name} is traveling to {destination.name}."

    def report_location(self):
        print(f"{self.name} is near {self.location}.")


class Explorer:
    def __init__(self, name):
        self.name = name
        self.discoveries = []

    def explore(self, stellar_object):
        discovery = f"{self.name} explored {stellar_object.name}"
        self.discoveries.append(discovery)
        return discovery

    def report_discoveries(self):
        return f"{self.name}'s discoveries: " + ", ".join(self.discoveries)
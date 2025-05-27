class Spaceship:
   def __init__(self, name):
       self.name = name
       self.hyperdrive = None
       print(f"Spaceship {self.name} constructed.")
   
   def install_hyperdrive(self, hyperdrive):
       self.hyperdrive = hyperdrive
       print(f"{self.hyperdrive.model} installed on {self.name}")
   
   def activate_hyperdrive(self):
       if self.hyperdrive:
           self.hyperdrive.activate()
       else:
           print("Error: No hyperdrive installed")

class Hyperdrive:
   def __init__(self, model, rating):
       self.model = model
       self.rating = rating
   
   def activate(self):
       print(f"Standard hyperdrive jump initiated. Rating: {self.rating}")

class QuantumHyperdrive(Hyperdrive):
   def __init__(self):
       super().__init__("Quantum Drive Mk IV", "Class 1")
       self.quantum_state = "stable"
   
   def activate(self):
       print(f"Quantum tunneling engaged. Creating artificial wormhole...")
       print("Ship enters quantum superposition...")
       print(f"Quantum state: {self.quantum_state}")

class ProbabilityHyperdrive(Hyperdrive):
   def __init__(self):
       super().__init__("Probability Engine", "Class 2")
       self.probability_field = 100
   
   def activate(self):
       print(f"Calculating infinite improbabilities...")
       print(f"Probability field strength: {self.probability_field}%")
       print("Ship transforms through probability space...")


# Create two ships
nova = Spaceship("Nova")
stellar = Spaceship("Stellar")

# Install different hyperdrives
nova.install_hyperdrive(QuantumHyperdrive())
stellar.install_hyperdrive(ProbabilityHyperdrive())

# Test standard hyperdrive abilities
print("\nTesting standard hyperdrive:")
standard_ship = Spaceship("Standard")
standard_ship.install_hyperdrive(Hyperdrive("Basic Drive", "Class 3"))
standard_ship.activate_hyperdrive()

# Test quantum hyperdrive
print("\nTesting quantum hyperdrive:")
nova.activate_hyperdrive()

# Test probability hyperdrive
print("\nTesting probability hyperdrive:")
stellar.activate_hyperdrive()
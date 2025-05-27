import random

class QuantumMainframe:
    def __init__(self):
        self.qubits = 0
        self.entanglement_level = 0
        self.error_rate = 0.05
        self.is_operational = False

    def initialize_qubits(self, num_qubits):
        if 0 < num_qubits <= 1000:
            self.qubits = num_qubits
            return True
        return False

    def entangle_qubits(self, level):
        if 0 <= level <= 10:
            self.entanglement_level = level
            return True
        return False

    def perform_quantum_computation(self):
        if not self.is_operational:
            return "Error: System not operational"
        if self.qubits == 0:
            return "Error: No qubits initialized"
        
        computation_success = random.random() > self.error_rate
        if computation_success:
            result = random.randint(1, 10**6)  # Simulated quantum computation result
            return f"Computation successful. Result: {result}"
        else:
            return "Error: Quantum decoherence occurred"

    def calibrate_system(self):
        if self.qubits > 0 and 0 < self.entanglement_level <= 10:
            self.is_operational = True
            self.error_rate = max(0.01, self.error_rate - 0.01)
            return "System calibrated and operational"
        return "Calibration failed: Check qubit count and entanglement level"
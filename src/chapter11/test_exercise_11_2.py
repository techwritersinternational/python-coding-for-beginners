import pytest
from exercise_11_2 import QuantumMainframe

def test_initialization():
   """Test quantum mainframe initialization."""
   qm = QuantumMainframe()
   assert qm.qubits == 0
   assert qm.entanglement_level == 0
   assert qm.error_rate == 0.05
   assert qm.is_operational == False

def test_qubit_initialization():
   """Test qubit initialization."""
   qm = QuantumMainframe()
   
   # Test valid qubit count
   assert qm.initialize_qubits(100) == True
   assert qm.qubits == 100
   
   # Test invalid qubit count
   assert qm.initialize_qubits(0) == False
   assert qm.initialize_qubits(1001) == False

def test_entanglement():
   """Test qubit entanglement."""
   qm = QuantumMainframe()
   
   # Test valid entanglement levels
   assert qm.entangle_qubits(5) == True
   assert qm.entanglement_level == 5
   
   # Test invalid entanglement levels
   assert qm.entangle_qubits(-1) == False
   assert qm.entangle_qubits(11) == False

def test_quantum_computation():
   """Test quantum computation."""
   qm = QuantumMainframe()
   
   # Test computation without initialization
   assert "Error" in qm.perform_quantum_computation()
   
   # Test with initialization
   qm.initialize_qubits(100)
   qm.entangle_qubits(5)
   qm.calibrate_system()
   result = qm.perform_quantum_computation()
   assert isinstance(result, str)

def test_calibration():
   """Test system calibration."""
   qm = QuantumMainframe()
   
   # Test calibration without initialization
   assert qm.calibrate_system() == "Calibration failed: Check qubit count and entanglement level"
   
   # Test successful calibration
   qm.initialize_qubits(100)
   qm.entangle_qubits(5)
   assert qm.calibrate_system() == "System calibrated and operational"
   assert qm.is_operational == True
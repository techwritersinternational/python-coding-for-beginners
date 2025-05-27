import pytest
from spacecraft import *

@pytest.fixture
def default_spacecraft():
    return Spacecraft()

def test_initialize_spacecraft(default_spacecraft):
    assert default_spacecraft
    assert default_spacecraft.fuel == 0
    assert default_spacecraft.oxygen == 0
    assert default_spacecraft.systems_check == False

def test_load_fuel(default_spacecraft):
    assert default_spacecraft.fuel == 0
    default_spacecraft.load_fuel(50)
    assert default_spacecraft.fuel == 50
    default_spacecraft.load_fuel(50)
    assert default_spacecraft.fuel == 100
    default_spacecraft.load_fuel(50)
    assert default_spacecraft.fuel == 100
    default_spacecraft.load_fuel(-50)
    assert default_spacecraft.fuel == 50

def test_load_oxygen(default_spacecraft):
    assert default_spacecraft.oxygen == 0
    default_spacecraft.load_oxygen(50)
    assert default_spacecraft.oxygen == 50
    default_spacecraft.load_oxygen(50)
    assert default_spacecraft.oxygen == 100
    default_spacecraft.load_oxygen(50)
    assert default_spacecraft.oxygen == 100
    default_spacecraft.load_oxygen(-50)
    assert default_spacecraft.oxygen == 100

def test_systems_check(default_spacecraft):
    default_spacecraft.oxygen = 60
    default_spacecraft.fuel = 50
    default_spacecraft.check_systems()
    assert default_spacecraft.systems_check == True

    default_spacecraft.oxygen = 50
    default_spacecraft.fuel = 50
    default_spacecraft.check_systems()
    assert default_spacecraft.systems_check == False

def test_launch(default_spacecraft):
    default_spacecraft.oxygen = 60
    default_spacecraft.fuel = 50
    assert default_spacecraft.launch() == "Launch failed: Systems check not passed."

    default_spacecraft.check_systems()
    assert default_spacecraft.launch() == "Launch failed: Insufficient fuel or oxygen."

    default_spacecraft.oxygen = 90
    default_spacecraft.fuel = 80
    assert default_spacecraft.launch() == "Spacecraft launched successfully!"
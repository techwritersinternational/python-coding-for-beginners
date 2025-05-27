import pytest
from star_map import Star, StarMap

@pytest.fixture
def empty_map():
   """Fixture that returns an empty StarMap."""
   return StarMap()

@pytest.fixture
def populated_map():
   """Fixture that returns a StarMap with predefined stars."""
   star_map = StarMap()
   stars = [
       Star("Sol", 0, 0, 0, 1.0),
       Star("Alpha Centauri", 4.37, 0.5, -0.2, 1.1),
       Star("Sirius", 8.6, -1.2, 0.4, 25.4)
   ]
   for star in stars:
       star_map.add_star(star)
   return star_map

class TestStarInitialization:
   """Tests for Star class initialization."""
   
   def test_star_creation(self):
       """Test creating a star with valid parameters."""
       star = Star("Sol", 0, 0, 0, 1.0)
       assert star.name == "Sol"
       assert star.x == 0
       assert star.y == 0
       assert star.z == 0
       assert star.luminosity == 1.0

class TestStarMapEmpty:
   """Tests for empty StarMap."""
   
   def test_empty_map_creation(self, empty_map):
       """Test creating an empty star map."""
       assert empty_map.star_count() == 0
   
   def test_get_nonexistent_star(self, empty_map):
       """Test getting a star that doesn't exist."""
       assert empty_map.get_star("NonexistentStar") is None
   
   def test_remove_nonexistent_star(self, empty_map):
       """Test removing a star that doesn't exist."""
       empty_map.remove_star("NonexistentStar")
       assert empty_map.get_star("NonexistentStar") is None    

class TestStarMapPopulated:
   """Tests for populated StarMap."""
   
   def test_initial_star_count(self, populated_map):
       """Test initial number of stars in populated map."""
       assert populated_map.star_count() == 3
   
   def test_get_existing_star(self, populated_map):
       """Test getting an existing star."""
       star = populated_map.get_star("Sol")
       assert star is not None
       assert star.name == "Sol"
       assert star.luminosity == 1.0
   
   def test_add_new_star(self, populated_map):
       """Test adding a new star."""
       new_star = Star("Proxima Centauri", 4.24, 0.3, -0.1, 0.0017)
       populated_map.add_star(new_star)
       assert populated_map.star_count() == 4
       retrieved_star = populated_map.get_star("Proxima Centauri")
       assert retrieved_star is not None
       assert retrieved_star.luminosity == 0.0017
   
   def test_add_duplicate_star(self, populated_map):
       """Test adding a star that already exists."""
       duplicate_star = Star("Sol", 1, 1, 1, 2.0)
       populated_map.add_star(duplicate_star)
       # Verify original star wasn't replaced
       original_star = populated_map.get_star("Sol")
       assert original_star.x == 0
       assert original_star.y == 0
       assert original_star.z == 0
   
   def test_remove_existing_star(self, populated_map):
       """Test removing an existing star."""
       initial_count = populated_map.star_count()
       populated_map.remove_star("Sol")
       assert populated_map.star_count() == initial_count - 1
       assert populated_map.get_star("Sol") is None

class TestStarMapOperations:
   """Tests for StarMap operations."""
   
   def test_add_multiple_stars(self, empty_map):
       """Test adding multiple stars."""
       stars = [
           Star("Star1", 1, 1, 1, 1),
           Star("Star2", 2, 2, 2, 2),
           Star("Star3", 3, 3, 3, 3)
       ]
       for star in stars:
           empty_map.add_star(star)
       assert empty_map.star_count() == 3
   
   def test_remove_all_stars(self, populated_map):
       """Test removing all stars."""
       stars_to_remove = list(populated_map.stars.keys())
       for star_name in stars_to_remove:
           populated_map.remove_star(star_name)
       assert populated_map.star_count() == 0
   
def test_comprehensive_workflow(empty_map):
   """Test a comprehensive workflow of map operations."""
   # Add stars
   stars = [
       Star("Star1", 1, 1, 1, 1),
       Star("Star2", 2, 2, 2, 2)
   ]
   for star in stars:
       empty_map.add_star(star)
   assert empty_map.star_count() == 2
   
   # Remove a star
   empty_map.remove_star("Star1")
   assert empty_map.star_count() == 1
   
   # Add a new star
   empty_map.add_star(Star("Star3", 3, 3, 3, 3))
   assert empty_map.star_count() == 2
   
   # Verify final state
   assert empty_map.get_star("Star1") is None
   assert empty_map.get_star("Star2") is not None
   assert empty_map.get_star("Star3") is not None
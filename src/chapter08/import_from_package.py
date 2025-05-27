from space_program import navigation
from space_program.life_support import check_oxygen_levels
import space_program.propulsion as prop

print(navigation.calculate_fuel_efficiency(5, 100))

check_oxygen_levels("2023-05-21", "Liftoff", "Orbit achieved")

prop.launch_spacecraft("Apollo", "Soyuz")
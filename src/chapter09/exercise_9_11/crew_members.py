class CrewMember:
   def __init__(self, name, specialization, years_experience):
       self.name = name
       self.specialization = specialization
       self.years_experience = years_experience


class Engineer(CrewMember):
   def __init__(self, name, years_experience, engineering_type):
       super().__init__(name, "Engineer", years_experience)
       self.engineering_type = engineering_type       


class Miner(CrewMember):
   def __init__(self, name, years_experience, mining_specialty):
       super().__init__(name, "Miner", years_experience)
       self.mining_specialty = mining_specialty
       

class Captain(CrewMember):
   def __init__(self, name, years_experience, command_rating):
       super().__init__(name, "Captain", years_experience)
       self.command_rating = command_rating
       


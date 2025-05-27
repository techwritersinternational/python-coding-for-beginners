eligible_voters = ['Alex', 'Bria', 'Chao', 'Dimitri', 'Elena']
has_voted = ['Bria', 'Dimitri']

for name in eligible_voters:
    if name in eligible_voters:
       if name in has_voted:
           print(f"{name} has already voted and cannot vote again.")
       else:
           print(f"{name}'s vote has been recorded.")
           has_voted.append(name)
    voter_turnout = (len(has_voted)/len(eligible_voters)) * 100
    print(f"Voter turnout: {voter_turnout}%")

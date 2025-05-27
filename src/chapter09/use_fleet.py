import fleet

orcadia = fleet.Fleet("Orcadia Fleet")

nova_horizon = fleet.Spacecraft("Nova Horizon", "Warp 5")
serenity = fleet.CargoShip("Serenity", "Full Burn", 500)
phoenix = fleet.SpaceTug("Phoenix", "Low Speed", 100)

orcadia.add_ship(nova_horizon)
orcadia.add_ship(serenity)
orcadia.add_ship(phoenix)

orcadia.list_ships()
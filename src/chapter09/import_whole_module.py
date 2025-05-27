import spacecraft

nova_horizon = spacecraft.Spacecraft("Nova Horizon", "Warp 5")
serenity = spacecraft.CargoShip("Serenity", "Full Burn", 500)
phoenix = spacecraft.SpaceTug("Phoenix", "Low Speed", 100)

nova_horizon.fly()
serenity.load_cargo(300)
phoenix.pull()
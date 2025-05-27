def launch_spacecraft(*spacecraft):
    print(f"Launching {len(spacecraft)} spacecraft:")
    for craft in spacecraft:
        print(f"- {craft} is taking off!")

launch_spacecraft("Nova Horizon", "Stellar Wanderer", "Cosmic Voyager")
launch_spacecraft("Stellar Wanderer")
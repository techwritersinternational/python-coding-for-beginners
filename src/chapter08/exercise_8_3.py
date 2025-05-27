def equip_spacesuit(helmet, suit_color, boots="standard", gloves="insulated", backpack="life support"):
    spacesuit = {
        "helmet": helmet,
        "suit_color": suit_color,
        "boots": boots,
        "gloves": gloves,
        "backpack": backpack
    }
    
    print(f"Spacesuit equipped: {suit_color} suit with {helmet}, {boots} boots, {gloves} gloves, and {backpack} backpack.")

# Test the function with different combinations of arguments

# All positional arguments
equip_spacesuit("bubble helmet", "white")

# Mix of positional and keyword arguments
equip_spacesuit("visor helmet", "orange", boots="magnetic")

# All keyword arguments
equip_spacesuit(helmet="full-face helmet", suit_color="blue", gloves="tactile", backpack="extended life support")

# Using all default values for optional parameters
equip_spacesuit(helmet="smart helmet", suit_color="red")
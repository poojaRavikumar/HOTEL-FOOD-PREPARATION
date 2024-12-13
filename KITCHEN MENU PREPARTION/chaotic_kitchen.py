#Student Name 2024-2026: Pooja Ravikumar
#Asu ID :1234370880
# Date : 14/11/2024
# Define the kitchen tools as hardware resources
hardware_resources = {
    "Stove": "Available",
    "Oven": "Available",
    "Mixer": "Available",
    "Knife": "Available"
}

# Simulate a chaotic kitchen without an OS (Chef)
def chaotic_kitchen():
    print("No Chef (CS) to manage the kitchen...")
    print("Chefs are fighting over resources!")
    
    # Multiple users trying to use the same resource without coordination
    hardware_resources["Stove"] = "Occupied by Chef1"
    print("Chef1 starts using the Stove.")
    
    # Another chef tries to use the same resource without checking availability
    print("Chef2 tries to use the Stove...")
    hardware_resources["Stove"] = "Occupied by Chef2"
    print("Conflict! Chef2 also starts using the Stove. Chaos ensues!")

# Simulate chaos without an OS
chaotic_kitchen()

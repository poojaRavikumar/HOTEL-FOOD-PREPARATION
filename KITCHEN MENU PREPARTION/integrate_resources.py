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

# Function to simulate OS organizing these resources
def integrate_resources(resources):
    print("Organizing kitchen tools (hardware resources)...")
    for tool, status in resources.items():
        print(f"{tool}: {status}")

# Call the function to integrate resources
integrate_resources(hardware_resources)

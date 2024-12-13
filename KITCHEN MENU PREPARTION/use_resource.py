#Student Name 2024-2026: Pooja Ravikumar
#Asu ID :1234370880
# Date : 14/11/2024
import time

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

# Simulate a user (chef) requesting a resource
def request_resource(user, tool):
    if hardware_resources[tool] == "Available":
        hardware_resources[tool] = f"Occupied by {user}"
        print(f"{user} is now using the {tool}.")
    else:
        print(f"{tool} is already occupied by another user.")

# Simulate productive use of a resource
def use_resource(user, tool, time_needed):
    if hardware_resources[tool].startswith("Occupied by"):
        print(f"{user} must wait; {tool} is currently occupied.")
    else:
        hardware_resources[tool] = f"Occupied by {user}"
        print(f"{user} is using the {tool} for {time_needed} seconds.")
        time.sleep(time_needed)  # Simulate time taken to use the resource
        hardware_resources[tool] = "Available"
        print(f"{user} has finished using the {tool}. It is now available.")

# Simulate users using resources productively
use_resource("Chef1", "Stove", 2)
use_resource("Chef2", "Oven", 3)

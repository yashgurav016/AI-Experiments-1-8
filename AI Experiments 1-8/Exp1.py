# Simple Reflex Agent - Vacuum Cleaner World with Path Cost

# Environment definition
environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}       

# Initial state setup.            
location = 'A'
path_cost = 0

def reflex_agent(location, status):
    """
    Condition-Action Rules for the Simple Reflex Agent:
    - If current room is Dirty -> Suck
    - If in Room A and Clean -> Move Right
    - If in Room B and Clean -> Move Left
    """
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"

print("Initial Environment:", environment)

# Simulation loop
while True:
    status = environment[location]
    action = reflex_agent(location, status)

    print(f"\nVacuum is at {location}")
    print(f"Room Status : {status}")
    print(f"Action Taken: {action}")

    # State transition and cost accumulation logic
    if action == "Suck":
        environment[location] = "Clean"
        path_cost += 1  # Cost for cleaning
    elif action == "Right":
        location = "B"
        path_cost += 1  # Cost for moving
    elif action == "Left":
        location = "A"
        path_cost += 1  # Cost for moving

    # Termination condition: Stop when both rooms are clean
    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("\nBoth rooms are clean.")
        break

print("\nFinal Environment:", environment)
print("Total Path Cost:", path_cost)

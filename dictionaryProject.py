motor = {
    "voltage": 24,
    "current": 3,
    "power": 72,
    "temperature": 45
}

for key, value in motor.items():
    print(f"{key.upper()}: {value}") #difference bewteen upper() and capitalise() is that, the former capitalizes the entire text whiles the latter capitalises only the first letter
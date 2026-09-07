motors = [
    {"voltage": 24, "current": 3},
    {"voltage": 12, "current": 5},
    {"voltage": 48, "current": 2}
]

for i, motor in enumerate(motors):
    print(f"Motor {i+1}: {motor['voltage']} V, {motor['current']} A")
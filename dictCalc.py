motor = {
    "voltage": 24,
    "current": 3
}

motor["power"] = motor["voltage"] * motor["current"]
if motor["power"] > 60:
    print('HIGH POWER')
else:
    print('NORMAL')
print(motor)
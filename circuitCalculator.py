def calculate_current(voltage, resistance):
    current = voltage/ resistance
    return current

def calculate_power(voltage, current):
    power = voltage * current
    return power

def resistive_power(current, resistance):
    resistance_power = (current ** 2) * resistance
    return resistance_power

Current = calculate_current(12, 6)
Power = calculate_power(12, Current)
Resistive_power = resistive_power(Current, 6)

print(f"Current: {Current} A")
print(f"Power: {Power} W")
print(f"Resistive Power: {Resistive_power} W") 
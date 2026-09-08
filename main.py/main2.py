import electrical

voltage = float(input('Enter voltage: '))
current = float(input('Enter current: '))

power = electrical.calculate_power(voltage, current)
resistance = electrical.calculate_resistance(voltage, current)
power_limit = electrical.check_power_limit(power, 100)
print(f"Power: {power} W")
print(f"Resistance: {resistance} ohms")
print(f"Power Limit Check: {power_limit}")
line = "Voltage: 24.0 V | Current: 3.0 A | Power: 72.0 W"

parts = line.split("|")

voltage_part = parts[0].split()

voltage = float(voltage_part[1])

print(voltage)
print(type(voltage))
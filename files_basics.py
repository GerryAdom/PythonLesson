voltage = float(input('Enter voltage: '))
current = float(input('Enter current: '))

power = voltage * current

with open("measurement.txt", 'a') as file:
    file.write(f"Voltage: {voltage} V | Current: {current} A | Power: {power} W\n")
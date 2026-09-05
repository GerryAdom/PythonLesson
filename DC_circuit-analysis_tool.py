voltage = 24
resistances = [6, 8, 12]

def calculate_current(voltage, resistance):
    calculated_current = voltage/resistance
    return calculated_current

def calculate_power(voltage, current):
    calculated_power = voltage * current
    return calculated_power

currents = []
powers = []

for resistance in resistances:
    current = calculate_current(voltage, resistance)
    power = calculate_power(voltage, current)
    currents.append(current)
    powers.append(power)

total_current = 0
for current in currents:
    total_current += current
    
total_power = 0
for power in powers:
    total_power = total_power + power
highest_power_resistance = resistances[0]    
highest_power = powers[0]
for i in range(len(powers)):
    if highest_power < powers[i]:
        highest_power = powers[i]
        highest_power_resistance = resistances[i]

highest_current = currents[0]
for current in currents:
    if highest_current < current:
        highest_current = current

print('===== DC CIRCUIT ANALYSIS ===== \n')
for i in range(len(resistances)):

    print(f"Branch {i + 1}:")
    print(f"Resistance: {resistances[i]} ohms")
    print(f"Current: {currents[i]} A")
    print(f"Power: {powers[i]} W")
    power_limit = 80
    if powers[i] > power_limit:
        print("Status: OVERLOAD")
    else:
        print("Status: OK")

    print() #this creates a space so the blocks are separated
print('---------------------------------- \n')
print(f"Total Current: {total_current} A")
print(f"Total Power: {total_power} W")
print('\n')
print(f"Highest Power: {highest_power} W")
print(f"Highest Power Resistance: {highest_power_resistance} ohm")
print(f"Highest Current: {highest_current} A")
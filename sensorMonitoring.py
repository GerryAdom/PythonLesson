voltages = [12.1, 11.8, 13.2]
currents = [2.0, 2.5, 1.8]
temperatures = [25, 31, 42]

voltage_min = 11.5
voltage_max = 12.5

temperature_max = 40

for i, (voltage, current, temperature) in enumerate(zip(voltages, currents, temperatures)):
    power = voltage * current
    
    print(f"Sensor {i+1}")
    print(f"Voltage: {voltage} V")
    print(f"Current: {current} A")
    print(f"Temperature: {temperature} C")
    print(f"Power: {power:.2f} W")
    
    if voltage_min <= voltage <= voltage_max and temperature_max <= 40:
        print('Status: NORMAL')
    else:
        print('Status: ABNORMAL')
    print()
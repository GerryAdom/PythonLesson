counts = 0
highest_voltage = 0
highest_calculated_power = 0
total_voltage = 0
lowest_voltage = None

with open("measurements.txt", "r") as file:
    for line in file:
       
        part = line.split("|")
        
        voltage_part = part[0].split()
        current_part = part[1].split()
        power_part = part[2].split()

        current = float(current_part[1])
        voltage = float(voltage_part[1])
        recorded_power = float(power_part[1])
        
        counts += 1
        total_voltage += voltage
        
        calculated_power = voltage * current
        
        print(f"Voltage: {voltage} V | Current: {current} A | Power: {calculated_power} W")
        
        if recorded_power == calculated_power:
            print('Power Check: OK')
        else:
            print('Power Check: Mismatch')
        
        if highest_voltage < voltage:
            highest_voltage = voltage
        
        if lowest_voltage is None or voltage <  lowest_voltage:
            lowest_voltage = voltage
               
        if highest_calculated_power < calculated_power:
            highest_calculated_power = calculated_power
        
    average_voltage = total_voltage/counts
        
    print(f"Number of measurements: {counts}")
    print(f"Highest Voltage: {highest_voltage} V")
    print(f"Total Voltage: {total_voltage}")
    print(f"Average Voltage: {average_voltage:.2f} V")
    print(f"Lowest Voltage: {lowest_voltage}")
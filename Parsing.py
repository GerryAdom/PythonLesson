counts = 0
highest_voltage = 0
highest_calculated_power = 0
total_voltage = 0
lowest_voltage = None
power_ok = 0
power_mismatch = 0
lower_limit = 10
upper_limit = 50
low_voltage = 0
high_voltage = 0
normal_voltage = 0

with open("measurements.txt", "r") as file:
    for line in file:
        try:
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
            
            if lower_limit > voltage:
                low_voltage += 1
                print("LOW")
            elif lower_limit <= voltage <= upper_limit:
                normal_voltage += 1
                print("NORMAL")
            else:
                high_voltage += 1
                print("HIGH")
            
            if recorded_power == calculated_power:
                power_ok += 1
                print(f"Power Check: OK")
            else:
                power_mismatch += 1
                print(f"Power Check: Mismatch")
            
            if highest_voltage < voltage:
                highest_voltage = voltage
            
            if lowest_voltage is None or voltage <  lowest_voltage:
                lowest_voltage = voltage
                
            if highest_calculated_power < calculated_power:
                highest_calculated_power = calculated_power
                
        except ValueError:
                    print("Invalid Measurement")
            
average_voltage = total_voltage/counts
            
print(f"Number of measurements: {counts}")
print(f"Highest Voltage: {highest_voltage} V")
print(f"Total Voltage: {total_voltage}")
print(f"Average Voltage: {average_voltage:.2f} V")
print(f"Lowest Voltage: {lowest_voltage}")
print(f"Power checks OK: {power_ok}")
print(f"Power checks mismatch: {power_mismatch}")
print(f"Low Voltage: {low_voltage}")
print(f"Normal Voltage: {normal_voltage}")
print(f"High Voltage: {high_voltage}")
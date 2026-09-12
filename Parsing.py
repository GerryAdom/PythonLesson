import parse_function as pf

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
invalid_measurement = 0

with open("measurements.txt", "r") as file:
    for line in file:
        if not line.strip(): #the line.strip() eliminates the whitespaces since Python considers whitespaces to be characters and would not consider a line with only whitespaces to be empty.The line.strp() eliminates the whitespaces evaluating to a true. The not operator negates the boolean value returned by line.strip(), so if the line is empty or contains only whitespace, the condition evaluates to True, and the code inside the if block is executed.
            print("Empty line detected.")
            continue
        
        try:
            voltage, current, recorded_power = pf.parse_measurements(line)
            
            counts += 1
            total_voltage += voltage
            
            calculated_power = pf.calculate_power(voltage, current)
            
            print(f"Voltage: {voltage} V | Current: {current} A | Power: {calculated_power} W")
            
            voltage_classification = pf.classify_voltage(voltage, lower_limit, upper_limit)
            if voltage_classification == "LOW":
                low_voltage += 1
            elif voltage_classification == "NORMAL":
                normal_voltage += 1
            else:
                high_voltage += 1
            
            power_validation = pf.validate_power(recorded_power, calculated_power)
            if power_validation == "OK":
                power_ok += 1
            else:
                power_mismatch += 1
            
            if highest_voltage < voltage:
                highest_voltage = voltage
            
            if lowest_voltage is None or voltage <  lowest_voltage:
                lowest_voltage = voltage
                
            if highest_calculated_power < calculated_power:
                highest_calculated_power = calculated_power
                
        except (ValueError, IndexError):
            invalid_measurement += 1
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
print(f"Highest Calculated Power: {highest_calculated_power} W")
print(f"Invalid Measurements: {invalid_measurement}")
def parse_measurements(line):
    part = line.split("|")
    
    if len(part) != 3:
        raise ValueError("Invalid Measurement") #the raise keyword is used to trigger an exception in Python. This allows us to handle errors. In this case, the error was that, the line did not contain an expected number of parts, which is 3. The ValueError exception is raised to indicate that the input data is not in the expected format. This helps to catch and handle errors gracefully, allowing the program to continue running or provide meaningful feedback to the user.  
    voltage_part = part[0].split()
    current_part = part[1].split()
    power_part = part[2].split()
    
    current = float(current_part[1])
    voltage = float(voltage_part[1])
    recorded_power = float(power_part[1])
    
    return voltage, current, recorded_power

def calculate_power(voltage, current):
    return voltage * current

def classify_voltage(voltage, lower_limit = 10, upper_limit = 50):
    if lower_limit > voltage:
        return "LOW"
    elif lower_limit <= voltage <= upper_limit:
        return "NORMAL"
    else:
        return "HIGH"
    
def validate_power(recorded_power, calculated_power):
    if abs(recorded_power-calculated_power) < 0.01: #This is to aacount for floating point tolerance. It ensurees that with a marginal, negligible error of 0.01, the power is still considered valid.
            return "OK"
    else:
        return "Mismatch"
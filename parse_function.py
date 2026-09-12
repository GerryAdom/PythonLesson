def parse_measurements(line):
    part = line.split("|")
    
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
    if recorded_power == calculated_power:
        return "OK"
    else:
        return "Mismatch"
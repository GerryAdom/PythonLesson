def calculate_power(voltage, current):
    return voltage * current

def calculate_resistance(voltage, current):
    return voltage/current

def check_power_limit(power, limit):
    if power > limit:
        return 'HIGH'
    else:
        return 'NORMAL'
    
def classify_voltage(voltage, lower_limit, upper_limit):
    if voltage < lower_limit:
        return 'LOW'
    elif lower_limit <= voltage <= upper_limit:
        return 'NORMAL'
    else:
        return 'HIGH'
    
if __name__ == "__main__":
    print(calculate_power(24, 3))
    print(calculate_resistance(24, 3))
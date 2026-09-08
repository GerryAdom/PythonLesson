def calculate_power(voltage, current):
    power = voltage * current
    return power

def calculate_resistance(voltage, current):
    resistance = voltage/current
    return resistance

def check_power_limit(power, limit):
    if power > limit:
        return "HIGH"
    else:
        return "NORMAL"
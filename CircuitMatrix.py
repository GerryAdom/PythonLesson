branches = [
    [6, 4, 96],
    [8, 3, 72],
    [12, 2, 48]
]

power_limit = 80

for i in range(len(branches)):
    branch = branches[i]
    resistance = branch[0]
    current = branch[1]
    power = branch[2]

    print(f"Branch {i+1} ")
    print(f"Resistance: {resistance} ohm")
    print(f"Current: {current} A")
    print(f"Power: {power} W")
    
    if power > power_limit:
        print('OVERLOAD')
    else:
        print('OK')
    print()
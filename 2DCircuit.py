branches = [
    [12, 2, 24],
    [24, 3, 72],
    [48, 1, 48]
]

for i in range(len(branches)):
    branch = branches[i]
    voltage = branch[0]
    current = branch[1]
    power = branch[2]
    print(f'Branch {i+1}')
    print(f'Voltage: {voltage} V')
    print(f'Current: {current} A')
    print(f'Power: {power} W')
    if power > 50:
        print('HIGH POWER')
    else:
        print('NORMAL')
    print()
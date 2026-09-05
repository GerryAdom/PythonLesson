measurements = [
    [12.1, 12.3, 12.0],
    [23.8, 24.1, 24.3],
    [4.9, 5.1, 5.0]
]
doubled_measurements = []
for measurement in measurements:
    doubled_row = []
    for value in measurement:
        doubled_value = value * 2
        doubled_row.append(doubled_value)
    doubled_measurements.append(doubled_row)
print(doubled_measurements)
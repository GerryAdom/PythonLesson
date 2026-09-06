measurements = [
    [12.1, 12.3, 12.0],
    [23.8, 24.1, 24.3],
    [4.9, 5.1, 5.0]
]

for i in range(len(measurements)):
    for j in range(len(measurements[i])):
        print(f"Sensor {i+1}, Measuremnt {j+1}: {measurements[i][j]}")
    print()
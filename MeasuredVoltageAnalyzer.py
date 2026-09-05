measurements = [
    [11.8, 12.1, 11.9, 12.2],
    [23.5, 24.1, 23.8, 24.3],
    [4.8, 5.2, 5.0, 4.9]
]

lower_limit = 11.5
upper_limit = 12.5

for i in range(len(measurements)):

    sensor = measurements[i]

    total = 0
    abnormal_measurements = 0

    print(f"Sensor {i + 1}")

    for measurement in sensor:

        print(f"Measurement: {measurement} V")

        total += measurement

        if lower_limit <= measurement <= upper_limit:
            pass
        else:
            abnormal_measurements += 1

    average = total / len(sensor)

    print(f"Average: {average:.2f} V")
    print(f"Abnormal Measurements: {abnormal_measurements}")

    if abnormal_measurements == 0:
        status = "NORMAL"
    else:
        status = "ABNORMAL"

    print(f"Status: {status}")
    print()
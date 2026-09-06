measurements = [
    [12.1, 12.3, 12.0, 11.8],
    [23.8, 24.1, 24.3, 25.0],
    [4.9, 5.1, 5.0, 4.7]
]

lower_limit = 5.0
upper_limit = 24.5

for i in range(len(measurements)):
    abnormal_count = 0
    total_measurements = 0
    maximum_measurement = measurements[i][0]
    minimum_measurement = measurements[i][0]
    
    for j in range(len(measurements[i])):
       print(f"Sensor {i+1}, Measurement {j+1}: {measurements[i][j]}")
       total_measurements += measurements[i][j]
       
       if measurements[i][j] < minimum_measurement:
           minimum_measurement = measurements[i][j]
           
       if measurements[i][j] > maximum_measurement:
           maximum_measurement = measurements[i][j]
           
       if lower_limit <= measurements[i][j] <= upper_limit:
           print('NORMAL')
       else:
           abnormal_count += 1
           print('ABNORMAL')
    average = total_measurements/len(measurements[i])
    print(f"Abnormal Count: {abnormal_count}")
    print(f"Maximum: {maximum_measurement}")
    print(f"Minimum: {minimum_measurement}")
    print(f"Average: {average:.2f}")
    print()
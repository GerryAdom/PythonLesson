measurements = [
    [11.8, 12.1, 11.9, 12.2],
    [23.5, 24.1, 23.8, 24.3],
    [4.8, 5.2, 5.0, 4.9]
]

lower_limit = 11.5
upper_limit = 12.5
abnormal_measurements = 0
  
for sensors in measurements:
    total = 0
    for measurement in sensors:
        total += measurement
    average = total/len(sensors)      
    print(f"Average: {average:.2f} V")
    print(f"Abnormal Measurement: {abnormal_measurements}")
    if lower_limit <= measurement <= upper_limit:
                status = 'NORMAL'
    else:
            abnormal_measurements += 0
            status = 'ABNORMAL'
    print(f'Status: {status}')
    print()
voltages = [11.8, 12.1, 11.5, 13.2, 12.7, 10.9, 12.4]
#lists are highly inefficient when dealing with large lists. As we'd have to manually update each element of the list and its associated value every time in order to keep the relationship intact.
number_of_measurements = len(voltages)
first_measurement = voltages[0]
last_measurement = voltages[-1]

total = 0
for voltage in voltages:
    total += voltage
average = total/len(voltages)

maximum_voltage = voltages[0]
for voltage in voltages:
    if voltage > maximum_voltage:
        maximum_voltage = voltage
minimum_voltage = voltages[0]
for voltage in voltages:
    if minimum_voltage > voltage:
        minimum_voltage = voltage

abnormal_count = 0
abnormal = []
for voltage in voltages:
    if voltage < 11.5 or voltage > 12.5:
        abnormal_count += 1
        abnormal.append(voltage)
if abnormal_count > 2:
            print(' Status: CRITICAL')
elif abnormal_count == 1 or abnormal_count == 2:
            print('Status: WARNING')
else:
            print('Status: NORMAL')

print('==== Voltage Monitor ====')
print(f'Measurements: {number_of_measurements}')
print(f'First Measurement: {first_measurement}')
print(f'Last Measurement: {last_measurement}')
print(f'Average: {average:.2f}')
print(f'Maximum: {maximum_voltage}')
print(f'Minimum: {minimum_voltage}')
print(f'Abnormal measurements: {abnormal_count}')
print(f'Abnormal count: {abnormal}')

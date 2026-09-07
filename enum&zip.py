#Using the enumerate keyword is a much cleaner way of writing the key/value pair of a dictionary. It eliminates the need to write manually write the index and then match the key/value pairs to them. It takes the structure, for i, variable in enumerate(dictionaryName). enumerate by default loops through a dictionary and gives you its keyssd

'''
sensors = ["Voltage", "Current", "Temperature"]

for i, sensor in enumerate(sensors):
    print(i, sensor)
'''
   
#the zip function allows us to join two different lists together by pairing them together correspondingly

"""
for i in range(len(voltages)):
    voltage = voltages[i]
    current = currents[i]

    power = voltage * current

    print(f"{voltage} V, {current} A, {power} W")
"""
#th piece of code above can be cleanly written using the zip function as below.
"""
for voltage, current in zip(voltages, currents):
    power = voltage * current

    print(f"{voltage} V, {current} A, {power} W")
"""

#now when the lists are of different lengths, the code is cut short when the shorter list's index run out. It's therefore very neccessary to check the lengths of lists whenever we want to apply the zip function.
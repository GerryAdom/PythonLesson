import electricals as e

running = True
while running:
    try:
        voltage = float(input('Enter voltage: '))
        current = float(input('Enter current: '))

        power = e.calculate_power(voltage, current)
        resistance = e.calculate_resistance(voltage, current)
        power_limit = e.check_power_limit(power, 100)
        voltage_classification = e.classify_voltage(voltage, 10, 50)

        print('=== Electrical Measurement ===')
        print(f"Voltage: {voltage} V")
        print(f"Current: {current} A")
        print(f"Resistance: {resistance:.2f} ohms")
        print(f"Power: {power:.2f} W")
        print(f"Power Status: {power_limit}")
        print(f"Voltage Status: {voltage_classification}")
        
        while True:
            choice = input('Do you want another measurement? (yes/no): ')
            
            if choice == 'yes':
                break
            elif choice == 'no':
                running = False
                print('Program ended')
                break
            else:
                print('Please enter yes/no')
        
    except ValueError:
        print('Enter numbers!')
    except ZeroDivisionError:
        print('Cannot divide by zero!')
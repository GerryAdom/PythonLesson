while True: #while True gives the condition that allows the loop to begin. when it' false, the loop never executes
    try:
        voltage = float(input('Enter voltage: '))
        current = float(input('Enter current: '))

        if voltage < 0 or current < 0:
            print('Invalid Input')
            continue
        
        power = voltage * current
        
        print(f"Voltage: {voltage} V")
        print(f"Current: {current} A")
        print(f"Power: {power}")
        
        break
    
    except ValueError:
        print("Please enter numbers.")
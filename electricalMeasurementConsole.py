running = True
while True:
    try:
        voltage = float(input('Enter voltage: '))
        current = float(input('Enter current: '))
        
        if voltage < 0 or current < 0:
            print("Invalid inputs")
            continue
        
        power = voltage * current
        
        print(f"Current: {current} A")
        print(f"Voltage: {voltage} V")
        print(f"Power: {power:.2f} W")
        
        choice = input("Do you want to enter another measurement? (yes/no): ")
        
        if choice == "no":
            running = False
            break
    
    except ValueError:
        print('Enter numbers')
    

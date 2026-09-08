running = True
while running:
    
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
        while True:
            choice = input("Do you want to enter another measurement? (yes/no): ")
        
            if choice == 'yes':
                break
            
            elif choice == "no":
                running = False
                break
            
            else:
                print('Please enter yes/ no')
    
    except ValueError:
        print('Enter numbers')
    
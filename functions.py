#A function has the structure; 
# 'def' function_name(parameters):
        #return return value
def current(voltage, resistance):
    return voltage/resistance

I = current(12, 6)
print(I)

def power(voltage, current):
    result = voltage * current
    return result

P = power(12, 2)

print(result) #we are seeing an error here because the result parsed into the print function haven't been defined yet. It's a local variable that's only defined within the function.
#A dictionary stores information using keys and values.
#It has the strcutre; variable = {"key" : value}
#to print a value associated with a key we use this format; variable["key"]
#a completely new key can be added to a dictionary and a key can be completely modified as well

motor = {
    "voltage": 24,
    "current": 3,
    "power": 72
}

motor["current"] = 4
motor["speed"] = 1500

#We can remove a key/value pair with the del keyword or the pop function .pop()
#difference between the del and the .pop() is that del completely deletes the key/value pair whiles the .pop() removes the key/value pair from the dictionary and stores them in a variable. 
#Each take the following structure; del variable["key"] and key = variable.pop("key")

sensor = {
    "voltage": 12.5,
    "current": 2.0,
    "temperature": 35
}

del sensor["temperature"]
current = sensor.pop("current")

sensor = {
    "voltage" : 12.5,
    "current" : 2.0
}

if "temperature" in sensor:
    print(sensor["temperature"])
else:
    print("No temperature data")
    
#using the .items() allows us to access the key and value together. It uses the structure; for key, value in variable.items()
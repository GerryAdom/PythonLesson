'''file handling helps us to save and retrieve data we obtain from programmes we run.
there are three modes of handling data; write(w), read(r), append(a)

It follows the structure;

Writing to a file
file = open("name.txt", "w") 

#file is the name of the object Python uses to reference the file we are going to read from or append to or write to. Just like what we do when importing a module as an alias. name.txt is the actual file whiles 'file' is the alias we choose to reference it by.

file.write("Voltage: 24 V\n")
file.write("Current: 3 A\n")

file.close

Reading a file
file = open("measurements.txt", "r")

data = file.read()

print(data)

file.close()

a better way is to use the 'with' keyword
It has the following structure;
with open("name.txt", "mode") as "alias":
    alias.mode(".....: .../n)
'''

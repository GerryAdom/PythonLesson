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
    
We can also read the data one line at a time. This makes the program display information one at at time starting with the very first data in the file.
This is made possible by the .readline() or a for loop to iterate over the data. without the for loop, we'd have to run the program everytime we want to display a line.

Readline is for when we want to manually track the reading ourselves but for larger data, it's impractical to use since, for every data, we'd have to type readline.
This is solved using a for loop.

Then we have the readlines. This function display the data as a list. Now readline displays each element of the data separately as a string and the readlines displays them as a list.
The difference between the three is that;

read prints all the elements of the data as a string
readline prints the data line-by-line
readlines prints the data together as a list
'''

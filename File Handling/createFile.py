# "a" - Append - will append to the end of the file

fs = open("Demo.txt","a")

fs.write("I am Writing")

fs.close()

open_read = open("Demo.txt","r")

print(open_read.read())

# "w" - Write - will overwrite any existing content

w = open("DemoTwo.txt","w")

w.write("This Text will Replace Existing Text")

w.close()

r = open("DemoTwo.txt","r")

print(r.read())


# Create File

create_w = open("myfileTwo.txt", "w")

create_a = open("myfileTwo.txt", "a")

# "x" - Create - will create a file, returns an error if the file exist

create_x = open("myfileThree.txt", "x")
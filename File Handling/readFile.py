
read_file = open("Demo.txt","rt")

# By default the read() method returns the whole text
# but you can also specify how many characters you want to return
print(read_file.read(5))


# Line by Line
print(read_file.readline())
print(read_file.readline())


#  Or 
#  Loop through Line by Line

for x in read_file :
    print(x)
    
read_file.close()
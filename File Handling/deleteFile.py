import os

# Check if File exist:

if os.path.exists("Demo1.txt") :
    os.remove("Demo1.txt")
else :
    print("No File There...")
    

# Delete - You can only remove empty folders

os.rmdir("folder")

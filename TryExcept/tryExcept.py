# The TRY block lets you test a block of code for errors.

# The EXCEPT block lets you handle the error.

# The ELSE block lets you execute code when there is no error.

# The FINALLY block lets you execute code, regardless of the result of the try- and except blocks


try :
    print(x)
except NameError:  # its our choice to choose a error type
    print("No x here !!!")
else :
    print("if else run , No Error exist")
finally :
    print("I am Always There")
    
    
# Raise

y = "karthi"

if not type(y) is int  : raise TypeError("Define the y type as an int")
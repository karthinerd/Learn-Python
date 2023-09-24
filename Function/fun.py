# Function 

def my_function(name="Karthigairaj") : # ---> PARAMETER
    return f"hi {name}"

res = my_function("karthi")  # ---> ARGUMENT

print(res)


def loop_any_iterable(iterable) :
    for x in iterable :
        print(x)
        
list = ["a","karthi",True]

loop_any_iterable(list)


# Arbitrary Arguments, *args -- will receive a tuple of arguments

def my_fun(*kids):
  print("The youngest child is " + kids[2])

my_fun("Emil", "Tobias", "Linus")


# Arbitrary Keyword Arguments, **kwargs  -- will receive a dictionary of arguments

def _function_(**kid):
  print("His last name is " + kid["lname"])

_function_(fname = "Tobias", lname = "sne")
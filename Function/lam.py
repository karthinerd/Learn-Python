# LAMBDA - Anonymous function take any number of arguments, but can only have one expression

# Syntax --> lambda arguments : expression

mul = lambda a,b : print((a+b)*2)

mul(100,66)

# POWER OF LAMBDA

def add(x) : 
    return lambda y : x/y
    
result = add(24)

print(result(8))
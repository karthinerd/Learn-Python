myFamily = {
  "child3" : {
    "name" : "karthi",
    "year" : 2002
  },
  "child2" : {
    "name" : "kumar",
    "year" : 1998
  },
  "mother" : {
    "name" : "latha",
    "year" : 1973
  }
}

# For Loop

for x in myFamily.items() :
    print(x)
    
# get Value without using value()

for x in myFamily : 
    print(myFamily[x])
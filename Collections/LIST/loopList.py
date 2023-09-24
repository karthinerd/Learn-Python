fruits = ["apple","orange","banana","Cherry"]

# FOR LOOP

for x in fruits :
    print(x)
    
# Loop by INDEX

print("---- Loop By Index ----")

for i in range(len(fruits)) :
    print(fruits[i])
    
# WHILE LOOP
print("---- WHILE Loop ----")

i = 0

while i < len(fruits) :
    print(fruits[i])
    i += 1
    
print("--- Comprehension ---")
# List COMPREHENSION (Short - Hand Loop)
    
comp = [x for x in fruits if "a" in x]

print(comp)

result = [f"{i} - {'odd' if i % 2 == 1 else 'even'}" for i in range(1, 21)]

for item in result:
    print(item)

# RANGE

for x in range(0,11,2):
    if x == 0 :
        continue
    print(f"{x} - Even")
    

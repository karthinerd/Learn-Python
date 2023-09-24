num = (1,23,4,5,3,2,53)

letter= ("karthigairaj",)

# For Loop

for x in letter[0]:
    print(x)
    
# Loop By Index

for i in range(len(letter)) :
    print(letter[i])
    
# Reverse Single Tuple

reverseLetter = (letter[0][::-1],)

print(reverseLetter)


# WHILE Loop

i=len(reverseLetter) - 1

while i>=0:
    re_reverse = reverseLetter[i]
    for x in re_reverse:
        print(x)
    i -= 1
    
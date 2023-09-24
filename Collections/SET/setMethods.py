
setOne = {1,32,3,42,43,"I am"}

setTwo = {'a','fds','gd',"I am"}

# Union() method that returns a new set containing all items from both sets

setThree = setOne.union(setTwo)

print(setThree)

# Keep ONLY the Duplicates #

# Intersection_update()

setOne.intersection_update(setTwo)

print(setOne)

#  Intersection - method will return a New Set

inter = setOne.intersection(setThree)

print(inter)

# Keep All, But NOT the Duplicates #

# Symmetric_difference_update

setOne.symmetric_difference_update(setTwo)

print("difUp",setOne)

# Symmetric_difference - method will return a new set 

print('One -->',setOne)

print("Two -->",setTwo)

diff = setOne.symmetric_difference(setTwo)

print(diff)
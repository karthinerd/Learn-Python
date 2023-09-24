# # An iterator is an object that contains a countable number of values #

# # Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__() #

# Iterator vs Iterable

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator

# Iterate Tuple

tup = ("karthi","kumar","latha")

it = iter(tup)

print(next(it))
print(next(it))

# Iterate String

my_name = "karthigairaj"

my_it = iter(my_name)

print(next(my_it))


# Create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object #

class my_class :
     def __iter__(self):
        self.a = 1
        return self
    
     def __next__(self) :
         x = self.a
         self.a += 1
         return x
     
my_obj = my_class()

my_obj_it = iter(my_obj)

print(next(my_obj_it))
print(next(my_obj_it))
print(next(my_obj_it))

# StopIteration - Add a terminating condition to raise an error if the iteration is done a specified number of times

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myc = MyNumbers()
myi = iter(myc)

for x in myi:
  print(x)
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.


# PARENT


class parent_base:
    def __init__(self, mark, rank, name):
        self.mark = mark
        self.rank = rank
        self.name = name

    def result(self):
        return f"Hi {self.name} , you got {self.mark} marks & you're Rank - {self.rank}"


parent_obj = parent_base(565, 5, "karthi")

print("Parent ---> ", parent_obj.result())


# CHILD


class child_derived(parent_base):
    def __init__(self, mark, rank, name, year):
        # SUPER() function that will make the child class inherit all the methods and properties from its parent
        super().__init__(mark, rank, name)

        # Child Properties
        self.passed_out_year = year

    # Child Method
    def end(self):
        parent_result = super().result()
        return f"{parent_result} and Graduated Year is {self.passed_out_year}"


child_obj = child_derived(990, 3, "kumar", 2019)

print("Child ---> ", child_obj.result())

print("Child passed out year ---> ", child_obj.passed_out_year)

print(child_obj.end())

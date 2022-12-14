class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1],params[2])
        return cls(*string.split("-"))
    @classmethod
    def printgood(str):
        print("this is good" + str)
        return 89

harry = Employee("Harry Potter", 4500, "born with magical power the hero")
ron = Employee("Ron Weasley", 450, "wizard1")
voldemort = Employee.from_str("Lord Voldemort-45000-villain")

harry.change_leaves(34)

print(harry.print_details())
print(ron.print_details())

# Employee.no_of_leaves = 89
print(harry.no_of_leaves)
print(voldemort.salary)
# Employee.printgood()
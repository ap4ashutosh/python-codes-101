print("enter number 1")
num1 = input()
print("enter number 2")
num2 = input()
try:
    print("The sum of two numbers is", int(num1) + int(num2))
except Exception as e:
    print(e)

print("This is a very important line")

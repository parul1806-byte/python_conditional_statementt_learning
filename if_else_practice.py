# 1.check number is positive or negative
num = int(input("enter the number:"))
if num > 0:
    print("positive")
else:
    print("negative")

# 2.even or odd
num = int(input("enter the number:"))
if num % 2 == 0:
    print("even")
else:
    print("odd")
# 3.check age
age = int(input("enter your age "))
if age >= 18:
    print("adult")
else:
    print("minor")

# 4. compare two number
num1 = int(input(" enter the first number :"))
num2 = int(input("enter the second number: "))
if num1 > num2:
    print(num1,"is gerater than",num2)
else:
    print(num2,"is greater than",num1)

# 5. check if sum of two num  is greater than 10
a = int(input("enter the first no :"))
b = int(input("enter the second no :"))
sum = a+b
if sum > 10:
    print("sum is greater than 10")
else:
    print("sum is less than 10")

# 6.check if sum of two no is even or odd
a = int(input("enter the first no:"))
b = int(input("enter the seconf no :"))
sum = a+b
if sum % 2 == 0:
    print("sum is even")
else:
    print("sum is odd")
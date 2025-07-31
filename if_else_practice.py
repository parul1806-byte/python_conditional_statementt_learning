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
#7.
n = int(input())
if n > 0:
  print("POSITIVE")
elif n == 0:
  print("ZERO")
else:
  print("NEGATIVE")    

#8
n = int(input())
if n%3==0 and n%5==0:
  print("HelloWorld")
elif n%3 == 0:
  print("Hello")
elif n%5 == 0:
  print("World")
else:
  print(n)

 #9.greatest among three
    a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
  print(a)
elif b>a and b>c:
  print(b)
else:
  print(c)

#10.greatest among four
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(max(a,b,c,d))

#11. A,B,C which denote the angles of a triangle, and return 'VALID' 
#if the angles can form a valid triangle or 'NOT VALID' if the angles cannot form a valid triangle. Print the type of triangle in case it is valid
A = int(input())
B = int(input())
C = int(input())
if A+B+C == 180 and A>0 and B>0 and C>0:
  print("VALID")
  if A == B == C:
    print("EQUILATERAL")
  elif A == B or B==C or C==A:
    print("ISOSCELES")
  else:
    print("SCALENE")
else:    
  print("NOT VALID")

#12.take a 4 digit integer denoting a year and print out "YES" if it is a leap year and "NO" if it is not a leap year.
n = int(input())
if n%4==0 and n%100!=0 or n%400 == 0:
  print("YES")
else:
  print("NO")

#13.take a 3 digit integer, print "YES" if the reversed integer is equal to the input. Print "NO" otherwise.
n = input()
reversed_integer= n[::-1]
if n == reversed_integer:
  print("YES")
else:
  print("NO")
#14.Take an integer ranging from 0 - 6 as input and print out the corresponding weekday. 0 corresponds to Sunday and 6 corresponds to Saturday.
for i in range(7):
  i = int(input())
  if i == 0:
    print("Sunday")
  elif i ==1:
    print("Monday")
  elif i == 2:
    print("Tuesday")
  elif i ==3:
    print("Wednesday")
  elif i ==4:
    print("Thrusday")
  elif i ==5:
    print("Friday")
  else:
    print("Saturday")

#14.Take marks in five subjects,find the average and return the corresponding grade
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
Average = sum([n1,n2,n3,n4,n5])/5
if Average >= 90 :
  print("A")
elif 80 <= Average < 90:
  print("B")
elif 70 <= Average < 80:
  print("C")
elif 50<= Average < 70:
  print("D")
else:
  print("F")
#15.Take a number , print "Hello" if the number is divisible by 3, print "World" if the number is divisible by 5, or print "HelloWorld" 
#if the number is divisible by both 3 and 5.
#if all these conditions are false than print the number itself
n = int(input())
if n%3==0 and n%5==0:
  print("HelloWorld")
elif n%3 == 0:
  print("Hello")
elif n%5 == 0:
  print("World")
else:
  print(n)

    

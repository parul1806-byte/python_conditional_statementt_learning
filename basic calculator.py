num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
operator = input("select the operator:,(+,-,*,/):")
if operator == '+':
 add = num1+num2
 print("addition =",add)
elif operator == '-':
 sub = num1-num2
 print("subtraction = ",sub)
elif operator == '*':
  mul = num1*num2
  print("multiplication =", mul)
elif operator == '/':
   div = num1/num2
   print("division =",div)
else:
    print("invalid operator or operant")



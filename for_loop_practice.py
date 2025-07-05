# 1.print 1 to 5
for i in range(1,6):
    print(i)

#2. print each character of a string
str = input("enter any text:")
for i in str:
    print(i)

#3.print even no between 1 to 10
for i in range(2,11,2):
    print(i)

#4.sum of number from 1 to 5
total = 0
for i in range(1,6):
    total+= i
print(total)

#5.sum of even no from 1 to 10
total = 0
for i in range (1,11):
    if i % 2 == 0:
     total+= i
print(total)

# another way
total = 0
for i in range(2,11,2):
    total+= i
print(total)
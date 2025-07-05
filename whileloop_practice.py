#1.print 1 to 5
count = 1
while count <= 5:
   print(count)
   count += 1 # indentation must ne correct

 #2.  countdown from 5
count = 5 # countdown must starts from 5
while count >= 0: # countdown must end at 0
     print(count)
     count -= 1 # decrement of count from 5 to 0

# 3.print even no up to 10
i = 1
while i <=10:
    if i % 2 == 0:
        print(i)
    i += 1

# 4.sum of number upto 20
total = 0
i = 1
while i <= 20:
    total += i
    i += 1
print(total)
 # 5.sum of odd numbers up to 10
total = 0
i = 1
while i <= 10:
    if i % 2 == 0:
      total += i
    i += 1
print(total)
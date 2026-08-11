# Print numbers from 1 to 10.
for i in range (1,11):
    print(i)


# Print numbers from 10 to 1.
for i in range (11 ,0,-1):
    print(i)


# Print all 0dd numbers from 1 to 20.
for i in range (1,21,2):
    print(i)


# Print all even numbers from 1 to 20.
for i in range (2,21,2):
    print(i)


# Print the first 15 natural numbers.
for i in range (1,16):
    print(i)


# Print the multiplication table of 7.
for i in range(1,11):
    print("7 *",i,"=",7*i)


# Find the sum of numbers from 1 to 10
total = 0
for i in range (1 ,11):
    total = total + i
    print(total)
# Find the sum of all even numbers from 1 to 100.
total=0
for i in range (2,101,2):
    total = total + i
    print(total)

 # Find the sum of all odd numbers from 1 to 100.
total = 0
for i in range(1, 101, 2):
    total = total + i
    print(total)

#Find the sum of the first N natural numbers.
n=6
total=0
for i in range(n):
    total=total+i
    print(total)

# Find the product of numbers from 1 to 5.
total=1
for i in range(1,6):
    total=total*i
    print(total)


# Find the factorial of a number INPUT=5
result=1
for i in range(1,6):
    result=result*i
print(result)

# Find the product of all even numbers from 2 to 10.
total=1
for i in range(2,11,2):
    total=total*i
print(total)

# Pattern Problems
# Print:
# *
# **
# ***
# ****
# *****

n=6
total="*"
for i in range(1,6):
    n=total*i
    print(n)

# Print:
# *****
# ****
# ***
# **
# *

n=6
total="*"
for i in range (5,0,-1):
    n=total*i
    print(n)

# Print:
# 1
# 12
# 123
# 1234
# 12345

# Print:
# 1
# 12
# 123
# 1234
# 12345

n=5
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
#print the numbers 5 4 3 2 1
count=5
while(count>0):
    print(count)
    count=count-1

# Extraction of Digits from an Integer
num=5870
while num>0:
    last_digit=num%10
    print(last_digit)
    num=num//10
print(num%10)
# output= 5 8 7 0

#Count the number of Digits in an Integer
 num=75443467
 count=0

 while num>0:
     count+=1
     num=num//10
    print(count)
#output=8

# Check if a number is Palindrome or Not
num = 153
n = num
rev = 0

while num > 0:
    ld = num % 10
    rev = rev * 10 + ld
    num = num // 10

if rev == n:
    print("Palindrome")
else:
    print("Not a Palindrome")
    #output= not a palindrome 

# count the numbner of digit in an integer
n=423568
count=0
while n>0:
      n=n//10
      count+=1
print(count)
#output=6

# count the numbner of digit in an integer
n=423568
count=0
while n>0:
      n=n//10
      count+=1
print(count)
#output=6
# Given an integer n, print the numbers from 1 to n consecutively without spaces or new lines.
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

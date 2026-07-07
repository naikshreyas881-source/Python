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

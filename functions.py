def greet (sname,nname):
    print("Hello",sname,nname)
name = ("shreyas","Abhi")

def greet(sname, nname):
    print("Hello", sname, nname)

name = ("shreyas", "bhai")
greet(name[0], name[1])



# average of thr terms
def average(a, b):
  print("the avarage of the program is", (a + b) / 2)
average(18,65)
average(151, 543)

# Simple Greeting
def name(lname):
    print(lname)
name("shreyas Boss")
name("Naik")

# . Sum of Two Numbers
def sum(a,b):
    print(a + b)
    return a+b
sum(3,4)
sum(9,8)

##### Create a function that takes a number and returns:
###Even" if number is even
### "Odd" if number is odd

num=int(input("enter the number"))
def check_even_odd(num):
    if(num%2==0):
        return"even"
    else:
        return"odd"
result = check_even_odd(num)
print(result)

###Arithmetic operations
def sub(a,b):
    print(a+b)
sub(3,4)

def check_even_odd(a):
    if(a % 2==0):
        return "The number is even"
    else:
        return "the number is odd"
result = check_even_odd(3)
result = check_even_odd(5)
print(result)
print(result)

###Find Square
def square(a):
    print(a**2)
    return (a)
square(4)

##Find cube
def square(a):
    print(a**3)
    return (a)
square(4)
square(5)

####Mminimum  of Two Numbers
def check_maximum(a,b):
    if a < b:
        print("A is minimum")
    else:
        print("B is minimum")
check_maximum(75,7)

###maximum of Two Numbers
def check_maximum(a,b):
    if a < b:
        print("A is maximum")
    else:
        print("B is maximum")
check_maximum(75,7)

###print a name with hello
def greet (sname):
    print("Hello",sname)
greet("shreyas")

def greet(sname):
    print("Hello", sname)

greet("shreyas")

num=int(input("enter the number"))
def check_even_odd(num):
    if (num%2==0):
        return("even")
    else:
        return("odd")
result=check_even_odd(num)
print(result)



num=int(input("enter the number"))
def check_even_odd(num):
    if (num%2==0):
        return("even")
    else:
        return("odd")
result=check_even_odd(num)
print(result)


#Write a function that takes a name and prints:
def name(lname,nname):
    print("hello",lname,nname)
name("shreyas",'naik')

#Write a function to add two numbers.
def add(a,b):
    return(a+b)
result=add(4,5)
print(result)


nums=[5,6,7,7,1,9,111,1,1,5,1,1]
freq_map = {}

for i in range(len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)














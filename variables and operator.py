# Swap Two Numbers Without a Third Variable
a=10
b=20
(a,b)=(b,a)
print(a)
print(b)

#Swapping using multiple assignment in Python
a=10
b=20
c=a+b
a=c-a
b=c-b
print(a)
print(b)

#Find the Last Digit of a Number 9876
n=9876
last_digit=n%10
print(last_digit)


#Reverse a 3-Digit Number Using Operators
a=123
a=1
b=2
c=3
a=a+b
b=b
c=c-b
print(a,b,c)

#Convert Total Days into Years, Months, and Days
#Input:800 days
n=800
Months=((n/365)/12)
year=n/365
days=n
print("number of months =",Months)
print("number of year =",year)
print("number of days =",days)

#Find the Sum of Digits of a 3-Digit Number Input: 456
n=564
last_digit = n%10
n = n//10

middle_digit = n%10
n = n//10

first_digit = n%10
n= n//10

total=(last_digit+middle_digit+first_digit)
print(total)
#output=15

#Calculate Compound Interest
p=10000
r=10
t=2
compound_intrest=p*((1+r/100)*(1+r/100))
print(compound_intrest)
# output=12100.000000000002

#Convert Seconds into Hours, Minutes, and Seconds
n=7384
hour=(7384/(60*24))
minutes=(7384/60)
seconds=n
print(hour)
print(minutes)
print(seconds)
# output=5.127777777777778
# 123.06666666666666
# 7384

#Find the Largest of Three Numbers Using Comparison Operators
a=45
b=78
c=56
if(a>b and  a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)
# output=78

#Check Whether a 3-Digit Number is a Palindrome
n=121
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
n=n//10
a=c
print("it is a palindrome")
#output=it is a palindrome



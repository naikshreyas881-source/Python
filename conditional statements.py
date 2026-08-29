age=int(float(input("enter the age of the person :")))
if age==18:
    print("may be eligible may not be eligible ")

elif age>18:
    print("eligible to vote")
if age == (17.9):
    print("may be not eligibleee")
elif age < 18:
    print("not eligible to vote"
          )

n = int(input().strip())

if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

n=int(input("enter the number"))
if(n%2 !=0):
    print("Weird")
else:
    if (2<=n<=5):
        print("not Weird")
    elif (6<=n<=20):
        print("Weird")

    n = int(input().strip())

###maximum of Two Numbers
def check_maximum(a,b):
    if a < b:
        print("A is maximum")
    else:
        print("B is maximum")
check_maximum(75,7)

num=int(input("enter the number"))
if (num%2==0):
    print("weird")
    if (num%2==0 and 2<=num>=5):
        print("not weird")
        if (num%2==0 and 6<=num>=20):
            print("weird")
            if (num>20):
                print("Not weird")

#Given a string s, check if it is a palindrome or not. A palindrome is a word, phrase, or sequence that reads the same backward as forward.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def func(left, right):
            if left >= right:
                return True

            if s[left] != s[right]:
                return False

            return func(left + 1, right - 1)

        return func(0, len(s) - 1)

#check it is leaf year or not 
def is_leap(year):
    leap = False
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    # Write your logic here
    
    return leap
year = int(input())



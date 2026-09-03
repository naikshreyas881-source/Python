# factorial of a number
def factorial(n):
    if(n ==0 or n==1):
        return 1
    else:
        return(n*factorial(n-1))
print(factorial(5))

# # fibonacci sequence
def fibbonacci(n):
    if n<=1:
        return 1
    else:
        return(fibbonacci(n-1)+fibbonacci(n-2))
print(fibbonacci(4))

# print Nto1
def func(n):
    if n == 0:
        return
    print(n)
    func(n-1)
func(6)

# print sum of 1 to N
def func(sum,i,n):
    if i>n:
        print(sum)
        return
        func(sum,i+1,n)
func(0,1,6)
print(func)

# Input: arr = [5, 5, 5, 5]
# Output: 5
# Explanation: The largest element of the given array is 5.
from typing import List

class Solution:
    def largest(self, arr: List[int]) -> int:
        pass
        largest=float("-inf")
        n=len(arr)
        for i in  range (0,n):
            largest=max(largest,arr[i])
        return largest

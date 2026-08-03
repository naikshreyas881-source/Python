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

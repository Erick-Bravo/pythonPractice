# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    if type(num) != int or num < 0:
        return None
    else:
        factorial = 1
        count = 1
        while count <= num:
            factorial = count * factorial
            count += 1
        return factorial
    


print(factorial(5)) #120
print(factorial(6)) #720
print(factorial(0)) #1
print(factorial(-2)) #None
print(factorial(1.2)) #None
print(factorial("string")) #None
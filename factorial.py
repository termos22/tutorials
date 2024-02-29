def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = 5
result = factorial(num)
print("Factorial of {} is {}". format(num,result))
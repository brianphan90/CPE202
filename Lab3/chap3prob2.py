def get_factorial(x,n):
    if n == 0:
        return 1
    return x**n * get_factorial(x, n-1)

print(get_factorial(2,3))
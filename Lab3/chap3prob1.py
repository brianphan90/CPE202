def intpow(x, n):
    if n == 0:
        return 1
    
    return x * intpow(x, n-1)

print(intpow(2, 3))
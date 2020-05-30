def f(n):
    if n <=0:
        return 0
    return n+f(int(n/2))
print(f(4))
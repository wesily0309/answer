def f(n,m):
    if n>m:
        return 0
    return n+f(n+1,m)
print(f(33,66))
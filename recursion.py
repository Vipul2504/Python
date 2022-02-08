def factorial(n):
    n=int(input(enter Your number))
    if n==0:
        return 1
    else:
        recurse = factorial(n-1)
        result =n*recurse
        return recurse

from functools import reduce

def add_all(a,b):
    return a+b

nums=[2,3,4,5,6,7,8,9,12,24,77,67]
even=list(filter(lambda n : n%2==0,nums))
doubles=list(map(lambda n : n**3,even))
sum=reduce(lambda a,b : a+b,doubles)
print(even)
print(doubles)
print(sum)

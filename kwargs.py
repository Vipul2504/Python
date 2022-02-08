# ** is used for keyword variable lenght arg
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('vipul',age=28,city='Mumbai',mob=9865432)

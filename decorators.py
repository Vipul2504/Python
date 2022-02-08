def div(a,b):
    print(a/b)
#decorators are used for adding in function the code withouth changing og

def smart_div(func):

    def inner(a,b):

        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

div = smart_div(div)

div(2,4)

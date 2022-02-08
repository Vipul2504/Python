def count(list):
    more=0
    less=0

    for i in range(len(list)):
        if len(list[i])>5:
            more=more+1
        else:
                less=less+1

    return more,less
list =[]
x=(input("How many names you want to enter:"))
for k in range(x):
    list.append((input()))
more,less=count(list)
print('names more than 5 charchters : {} and Names less than 5 charcters :{}'.format(more,less))

          

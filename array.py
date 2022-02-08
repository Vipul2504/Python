from array import*
vals = array('i',[3,5,7,9,6])
newArr = array(vals.typecode,(a for a in vals))
for e in newArr:
    print(e)

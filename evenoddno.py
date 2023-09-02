

def evenoddno(list):
    list2=[x for x in list if x%2 == 0]
    print(f"Even No are: {list2}")
    list3=[x for x in list if x%2 != 0]
    print(f"Odd No are: {list3}")

list = [3,3,1,3,5,6,3,2,5,7,8,9,10,22,23,54]
print(f"Given list is : {list}")
evenoddno(list)


def listitemcount(list):
    dict = {}
    for x in list:
        if x in dict:
            dict[x] = dict[x] + 1
            #dict.update({x:dict[x]+1})
        else:
            dict[x] = 1
            #dict.update({x:1})
    print(dict)

list = [1,4,6,6,6,6,'nil',"nil",6,6,633,4,2,5,6,2,3,6]
listitemcount(list)

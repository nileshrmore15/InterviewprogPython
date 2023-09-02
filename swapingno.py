no1 = int(input('no1:'))
no2 = int(input('no2:'))

print(f"before swapping no1: {no1} and no2: {no2}")

#shortcut method in python
no1, no2 = no2, no1

# with temp variable
# tmp = no1
# no1 = no2
# no2 = tmp

# #without temp variable
# no1 = no1 + no2
# no2 = no1 - no2
# no1 = no1 - no2
#


print(f"after swapping no1: {no1} and no2: {no2}")



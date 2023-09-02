
def primeno(num):
    if num <= 1:
        return False
    for x in range(2, int(num ** 0.5 + 1)):
        if num % x == 0:
            return False
    return True


# if primeno(int(input("Enter No:"))):
#     print("It is prime no")
# else:
#     print("It is not prime no")

for i in range(1, 100):
    if primeno(i):
        print(i)



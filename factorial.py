
# def factorial(num):
#     c = num
#     for x in range(1, num+1):
#         if num-x > 1:
#             c = c * (num-x)
#     return c
#print(factorial(5))

def factorial(num):
    if num<=1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))
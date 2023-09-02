
def reverseno(num):
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev*10 + dig
        num = num // 10
    return rev

number = 67394
reverse = reverseno(number)
print(f"Reverse of {number} is {reverse}.")

if reverse == number:
    print('Number is palindrom')
else:
    print('Number is not palindrom')
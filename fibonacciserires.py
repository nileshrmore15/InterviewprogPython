

def fibonacci(num):
    if num<0:
        return False
    else:
        a=0
        b=1
        while a<num:
            print(a)
            c=a+b
            a=b
            b=c



fibonacci(2)


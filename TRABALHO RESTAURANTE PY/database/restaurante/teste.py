def calc(num):
    a = 0
    
    while num > 0:
        a += num + (num-1)
        num -=2
    return a

print(calc(31))
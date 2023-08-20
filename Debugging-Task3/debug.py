def compute(n):
    if n < 10:                  #assuming n<10
        out = n ** 2
    elif n <=20:                #assuming n>=10 and n<=20 
        out = 1
        for i in range(1, n-9):  # if n=12, then for i in range(1, n-10) gives 1 so n-10 should be n-9 so that output gives 2 which is the factorial of (n-10)
            out *= i
    else:                       #only when n>20
        lim = n - 20
        out = 0                 # Initialize out to 0
        for i in range(1, lim + 1):
            out += i
    return out

n = int(input("Enter an integer: "))
result = compute(n)
print(result)



# Solution to Problem 12

# cook your dish here
x = int(input())
flag = 0
if x > 1:
    for n in range(2, int(x**0.5)+1):
        if x % n == 0:
            flag = 0
            break
    else:
        flag = 1
else:
    flag = 0
print(flag)

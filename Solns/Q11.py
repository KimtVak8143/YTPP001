# Solution to Problem 11

# cook your dish here
x = int(input())
f = 10
s = 2
for n in range(x):
    if n % 2 == 0:
        print(f, end=" ")
        f += 10
    else:
        print(s, end=" ")
        s += 2

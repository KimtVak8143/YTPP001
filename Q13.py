# Solution to Problem 13

# cook your dish here
y = int(input())
x = int(input())
for n in range(x + 1):
    if (y - n) % x == 0:
        print(y - n)
        break


# Solution of Problem 5

# cook your dish here
x, y = map(int, input().split())

for n in range(x, y+1):
    if n % 2 != 0:
        print(n, end=" ")

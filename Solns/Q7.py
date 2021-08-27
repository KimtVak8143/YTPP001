# Solution to problem 7

# cook your dish here
x, y = map(int, input().split())

new = list(map(int, input().split()))[:x]
flag = 0
for n in range(len(new)):
    if y == new[n]:
        print(1)
        flag = 1
        break

if flag != 1:
    print(-1)
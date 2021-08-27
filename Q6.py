# Solution of Problem 6

# cook your dish here

x = int(input())
y = list(map(int, input().split()))[:x]
rev = []
for n in range(len(y)):
    rev.append(str(y[n]))

new = rev[::-1]
s = " "
newone = s.join(new)
print(newone)

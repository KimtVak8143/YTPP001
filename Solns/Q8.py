# Solution to Problem 8

# cook your dish here
new = []
for x in range(3):
    i = int(input())
    new.append(i)

m = max(new)

while m == max(new):
    new.remove(m)

print(max(new))

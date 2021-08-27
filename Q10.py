# Solution to Problem 10

# cook your dish here
t = int(input())
for n in range(t):
    new = list(map(int, input().split()))[:5]
    xyz = []
    while new:
        first = new[0]
        for x in new:
            if x < first:
                first = x
        xyz.append(first)
        new.remove(first)

    print(xyz[2])

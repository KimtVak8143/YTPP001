# Solution of Problem 4

# cook your dish here
x = input()
last = []
for n in str(x):
    last.append(n)

if int(last[-2]) == 7:
    print(1)
else:
    print(0)

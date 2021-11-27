a = [1, 2, 4, 6, 7, 10, 'lr']
for i in range(len(a)):
    print(a[i])


b = [[1, 1], [2, 1], [3, 3], [4, 4]]

for x, y in b:
    if x == y:
        print(str(x) + " equals " + str(y))

print(list(range(-2, 2)))
print(list(range(4)))


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'm', 'n', 'o', 'p']
print([letters[i] for i in [3, 4, 6, 8]] )


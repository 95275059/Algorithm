a = ["flower","flow","flight"]
print(*a)
print(list(zip(*a)))
print(list(map(set, zip(*a))))

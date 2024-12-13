list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(len(list1) == len(list2))


print(sum(list1) == sum(list2))

print(any(val in list2 for val in list1))

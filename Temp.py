def consecutive_combo(lst1, lst2):
    min1 = lst1[0]
    max1 = lst1[0]
    for i in lst1:
        if i < min1:
            min1 = i
        if i > max1:
            max1 = i

    min2 = lst2[0]
    max2 = lst2[0]
    for i in lst2:
        if i < min2:
            min2 = i
        if i > max2:
            max2 = i

    min = min1 if min1 < min2 else min2
    max = max1 if max1 > max2 else max2

    # expected sum
    sum = 0
    for i in range(min, max + 1):
        sum = sum + (i - min + 1)

    # actual sum
    sum1 = 0
    for i in lst1:
        sum1 = sum1 + (i - min + 1)

    for i in lst2:
        sum1 = sum1 + (i - min + 1)

    return sum == sum1


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
print(consecutive_combo([44, 46], [45]))

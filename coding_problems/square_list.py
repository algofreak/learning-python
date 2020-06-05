def square_list(num):
    length = len(num)
    result = [None] * length

    if length > 0:
        i: int = 0
        j: int = length - 1
        k: int = j

        while i <= j:
            sqr_of_i = num[i] * num[i]
            sqr_of_j = num[j] * num[j]

            temp = 0
            if sqr_of_i > sqr_of_j:
                temp = sqr_of_i
                i += 1
            else:
                temp = sqr_of_j
                j -= 1
            result[k] = temp
            k -= 1

    return result


print(square_list([-6, -4, -3, -1, 0, 3, 5, 7, 8]))
print(square_list([0, 3, 5, 7, 8]))
print(square_list([-15, -12, -10, -9, -8, -6, -4, -3, -1, 0]))

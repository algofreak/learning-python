import re


# the function should return the strings "invalid" or "valid" based on the email ID entered
def checkmail(email):
    return 'valid' if re.search(r'^[a-zA-Z0-9]+@[a-z]+.[a-z]{2,3}$', email) else 'invalid'


# email='pgajjar@gmail.com'
# print("email: " + email + " : " + checkmail(email))
# email='pgajjar@gmail.co'
# print("email: " + email + " : " + checkmail(email))
# email='pgajjar1980@gmail.com'
# print("email: " + email + " : " + checkmail(email))
# email='pgajjar@1gmail.com'
# print("email: " + email + " : " + checkmail(email))
# email='pgajjar@gmail.comedy'
# print("email: " + email + " : " + checkmail(email))
# email='pgajjarZs1@gmail.com'
# print("email: " + email + " : " + checkmail(email))
# email='pgajjar1x4Z@gmail.co'
# print("email: " + email + " : " + checkmail(email))
# email="a#43@gmail.com"
# print("email: " + email + " : " + checkmail(email))


def flatten_me(l):
    res = []
    for i in l:
        if isinstance(i, list):
            for j in i:
                if not isinstance(j, (list, dict, tuple)):
                    res.append(j)
                else:
                    return None
        else:
            return None

    return res


# l = [[1,2],[3,4]]
# l = [[1,2,3],[4,5],[6,7,8,9]]
l = [[1, [2, 3], 4], 5]
print(flatten_me(l))

# flat_list = [item for sublist in l for item in sublist]
# print(flat_list)

l = [1, 2, 3, 4, 5, 6]
y = (lambda x: x ^ 2 if x % 3 == 0 else x, l)

n = '9'

sum = 0
for i in range(1, 5):
    sum += int(n * i)
print(sum)

string = 'aabbccc'
n = 2

counts = {}
base = ord('A')
for i in string:
    index = ord(i) - base
    val = counts.get(index, None)
    if val is not None:
        counts[index] = val + 1
    else:
        counts[index] = 0

counts = dict(filter(lambda e: e[1] != 0, counts.items()))

print(counts)

sorted_counts = sorted(counts.items(), reverse=True)[:n]

res = list(map(lambda x: chr(x[0] + base), sorted_counts))
res = sorted(res)
print(res)


# import collections
# out=[collections.Counter(string).most_common(i+1)[i][0] for i in range(n)]
# out.sort()
# print(out)


x = 3
y = 4

a = [[(r + c) / 2 for c in range(y)] for r in range(x)]
print(a)

# Q-1
# select student_id, marks,
#     (case
#         when mod(marks, 10) = 0 then 'yes'
#         else 'no'
#     end) as div_by_ten
# from marks;


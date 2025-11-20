l_list = [3, 4, 2, 1, 3, 3]
r_list = [4, 3, 5, 3, 9, 3]

result = sum(abs(l - r) for l, r in zip(sorted(l_list), sorted(r_list)))


print(result)

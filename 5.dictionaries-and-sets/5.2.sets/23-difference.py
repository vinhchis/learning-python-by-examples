set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference_result_12 = set1 - set2
difference_result_21 = set2 - set1
# or set1.difference(set2)

print("in set1 not set2:",difference_result_12)
print("in set2 not set1:",difference_result_21)

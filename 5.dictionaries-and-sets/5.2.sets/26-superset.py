set1 = {1, 2, 3, 4}
set2 = {1, 2}
is_superset = set1 >= set2 # or set1.issuperset(set2)

print(set1, 'is superset of', set2, ":", is_superset)
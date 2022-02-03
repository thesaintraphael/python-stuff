from itertools import combinations, permutations


letters = ["a", "b", "c", "d"]


# returning one combination for all positions ===> (a, b) is same as (b, a)
print("Combinations")
print(list(combinations(letters, 2)))
print(list(combinations(letters, len(letters))))  # result is letters itself


# returning same combination with different positions ===> (a, b), (b, a) ===> both will be returned
print("Permutations")
print(list(permutations(letters, 2)))
print(list(permutations(letters, len(letters))))


# Values can be only repated if elements does have same values ==> letters = ["a", "b", "a"]

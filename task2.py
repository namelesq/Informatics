import itertools

def calculate_difference_sum(permutation):
    return sum(abs(permutation[i] - permutation[(i + 1) % len(permutation)]) for i in range(len(permutation)))
def find_permutation_with_target_sum(target_sum):
    numbers = list(range(1, 13))
    for perm in itertools.permutations(numbers):
        if calculate_difference_sum(perm) == target_sum:
            return perm
    return None
target = 32
result = find_permutation_with_target_sum(target)
if result:
    print("Найдена перестановка:", result)
else:
    print("Перестановка с заданной суммой не найдена.")









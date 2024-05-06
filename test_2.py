def exact_combinations(arr, k):
    def backtrack(combination, start):
        if len(combination) == k:
            combinations.append(combination[:])  # Add a copy of the current combination
            return
        for i in range(start, len(arr)):
            combination.append(arr[i])
            backtrack(combination, i + 1)
            combination.pop()

    combinations = []
    backtrack([], 0)
    return combinations

# Example usage:
arr = [1, 2, 3, 4]
k = 3
result = exact_combinations(arr, k)
print("Exact combinations of", arr, "with size", k, "are:", result)


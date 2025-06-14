def generate_subsets(arr):
    """
    Generates all subsets of a given set using bit manipulation.

    Each number from 0 to (2^n - 1) represents a subset.
    A bit set to 1 means the corresponding element is included in the subset.

    Args:
        arr (list): A list of elements to create subsets from.

    Returns:
        list: A list of all subsets.

    Time Complexity: O(n * 2^n)
    Space Complexity: O(2^n)
    """
    n = len(arr)
    total_subsets = 1 << n  # 2^n subsets
    subsets = []

    for mask in range(total_subsets):
        subset = [arr[i] for i in range(n) if (mask & (1 << i)) != 0]
        subsets.append(subset)

    return subsets


# 🔥 Example usage
arr = ["a", "b", "c"]
subsets = generate_subsets(arr)

# 🧠 Display results
print("All subsets:")
for s in subsets:
    print(s)

# ✅ Expected Output:
# All subsets:
# []
# ['a']
# ['b']
# ['a', 'b']
# ['c']
# ['a', 'c']
# ['b', 'c']
# ['a', 'b', 'c']


def backtrack_subsets(arr):
    def backtrack(idx, current_subset):
        if idx == len(arr):
            subsets.append(current_subset[:])
            return
        # Include the current element
        current_subset.append(arr[idx])
        backtrack(idx + 1, current_subset)

        # Exclude the current element
        current_subset.pop()
        backtrack(idx + 1, current_subset)

    subsets = []
    backtrack(0, [])
    return subsets

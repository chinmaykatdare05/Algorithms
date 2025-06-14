def can_jump(nums):
    """
    Determines if you can reach the last index.

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    max_reach = 0
    n = len(nums)

    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True


# Example Usage
print(can_jump([2, 3, 1, 1, 4]))  # Output: True
print(can_jump([3, 2, 1, 0, 4]))  # Output: False


def min_jumps(nums):
    """
    Finds the minimum number of jumps to reach the last index.

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if len(nums) <= 1:
        return 0

    jumps = 0
    cur_end = 0
    farthest = 0

    for i in range(len(nums) - 1):  # Exclude last index
        farthest = max(farthest, i + nums[i])

        if i == cur_end:  # If we reach the current jump boundary
            jumps += 1
            cur_end = farthest  # Set new boundary

            if cur_end >= len(nums) - 1:
                return jumps

    return jumps


# Example Usage
print(min_jumps([2, 3, 1, 1, 4]))  # Output: 2
print(min_jumps([2, 3, 0, 1, 4]))  # Output: 2


from collections import deque


def can_reach(nums, start):
    """
    Determines if we can reach an index with value 0.

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(nums)
    queue = deque([start])
    visited = set()

    while queue:
        index = queue.popleft()
        if nums[index] == 0:
            return True
        if index in visited:
            continue
        visited.add(index)

        # Jump left and right
        for next_index in (index + nums[index], index - nums[index]):
            if 0 <= next_index < n:
                queue.append(next_index)

    return False


# Example Usage
print(can_reach([4, 2, 3, 0, 3, 1, 2], 5))  # Output: True
print(can_reach([3, 0, 2, 1, 2], 2))  # Output: False

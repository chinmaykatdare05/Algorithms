def word_break_recursive(s, wordDict):
    """
    Solves the Word Break problem using recursion.

    Time Complexity: O(2^n) (Exponential)
    Space Complexity: O(n) (Recursion depth)
    """
    word_set = set(wordDict)

    def can_break(start):
        if start == len(s):
            return True  # Entire string segmented

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and can_break(end):
                return True

        return False

    return can_break(0)


# Example Usage
s = "leetcode"
wordDict = ["leet", "code"]
print("Word Break (Recursion):", word_break_recursive(s, wordDict))  # Output: True


def word_break_dp(s, wordDict):
    """
    Solves the Word Break problem using Dynamic Programming.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always valid

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


# Example Usage
s = "applepenapple"
wordDict = ["apple", "pen"]
print("Word Break (DP):", word_break_dp(s, wordDict))  # Output: True


from collections import deque


def word_break_bfs(s, wordDict):
    """
    Solves the Word Break problem using BFS.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    word_set = set(wordDict)
    queue = deque([0])
    visited = set()

    while queue:
        start = queue.popleft()
        if start in visited:
            continue
        visited.add(start)

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set:
                if end == len(s):
                    return True
                queue.append(end)

    return False


# Example Usage
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print("Word Break (BFS):", word_break_bfs(s, wordDict))  # Output: False

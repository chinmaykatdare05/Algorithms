# LEETCODE 75


from typing import List, Optional


# ARRAY/STRING
# 1768. Merge Strings Alternately (Easy)
def mergeAlternately(self, word1: str, word2: str) -> str:
    """
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
    Return the merged string.
    """
    n = min(len(word1), len(word2))
    res = ""
    for i in range(n):
        res += word1[i] + word2[i]
    if len(word1) > len(word2):
        res += word1[n:]
    elif len(word2) > len(word1):
        res += word2[n:]
    return res


# 1071. Greatest Common Divisor of Strings (Easy)
def gcdOfStrings(self, str1: str, str2: str) -> str:
    """
    For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
    """
    pass


# 1431. Kids With the Greatest Number of Candies (Easy)
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    """
    There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
    Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
    Note that multiple kids can have the greatest number of candies.
    """
    res = []
    m = max(candies)
    for i in candies:
        if i + extraCandies >= m:
            res.append(True)
        else:
            res.append(False)
    return res


# 605. Can Place Flowers (Easy)
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    """
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
    """
    if len(flowerbed) > 1:
        if flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1

    i = 1
    while i < len(flowerbed) - 1:
        if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
            if n <= 0:
                return True
            i += 1
        i += 1
    return n <= 0


# 345. Reverse Vowels of a String (Easy)
def reverseVowels(self, s: str) -> str:
    """
    Given a string s, reverse only all the vowels in the string and return it.
    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
    """
    i, j = 0, len(s) - 1
    s = list(s)
    while i < j:
        if s[i] not in "aeiouAEIOU":
            i += 1
            continue
        if s[j] not in "aeiouAEIOU":
            j -= 1
            continue

        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return "".join(s)


# 151. Reverse Words in a String (Medium)
def reverseWords(self, s: str) -> str:
    """
    Given an input string s, reverse the order of the words.
    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
    Return a string of the words in reverse order concatenated by a single space.
    Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
    """
    x = s.split()
    return " ".join(x[::-1])


# 238. Product of Array Except Self (Medium)
def productExceptSelf(self, nums: List[int]) -> List[int]:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    """
    left_product, right_product = 1, 1
    length = len(nums)
    answer = [1] * length
    for i in range(length):
        answer[i] = left_product
        left_product *= nums[i]

    for i in range(length - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer


# 334. Increasing Triplet Subsequence (Medium)
def increasingTriplet(self, nums: List[int]) -> bool:
    """
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
    """
    first = second = float("inf")
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False


# 443. String Compression (Medium)
def compress(self, chars: List[str]) -> int:
    """
    Given an array of characters chars, compress it using the following algorithm:
    Begin with an empty string s. For each group of consecutive repeating characters in chars:
    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.
    The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
    After you are done modifying the input array, return the new length of the array.
    You must write an algorithm that uses only constant extra space.
    """
    if len(chars) == 1:
        return 1

    i = 0
    while i < len(chars):
        j = i
        while j < len(chars) and chars[j] == chars[i]:
            j += 1

        if j - i > 1:
            chars[i + 1 : j] = list(str(j - i))

        i = j

    return len(chars)


# TWO POINTERS
# 283. Move Zeroes (Easy)
def moveZeroes(self, nums: List[int]) -> None:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.
    """
    i = 0
    for j in range(len(nums)):
        if nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


# 392. Is Subsequence (Easy)
def isSubsequence(self, s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    """
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


# 11. Container With Most Water (Medium)
def maxArea(self, height: List[int]) -> int:
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
    """
    i, j = 0, len(height) - 1
    res = 0
    while i < j:
        res = max(res, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res


# 1679. Max Number of K-Sum Pairs (Medium)
def maxOperations(self, nums: List[int], k: int) -> int:
    """
    You are given an integer array nums and an integer k.
    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
    Return the maximum number of operations you can perform on the array.
    """
    res = 0
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > k:
            right -= 1
        elif nums[left] + nums[right] < k:
            left += 1
        else:
            res += 1
            left += 1
            right -= 1

    return res


#  SLIDING WINDOW
# 643. Maximum Average Subarray I (Easy)
def findMaxAverage(self, nums: List[int], k: int) -> float:
    """
    You are given an integer array nums consisting of n elements, and an integer k.
    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.
    """
    current_sum = sum(nums[:k])
    res = current_sum / k

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        res = max(res, current_sum / k)

    return res


# 1456. Maximum Number of Vowels in a Substring of Given Length (Medium)
def maxVowels(self, s: str, k: int) -> int:
    """
    Given a string s and an integer k.
    Return the maximum number of vowel letters in any substring of s with length k.
    Vowel letters in English are (a, e, i, o, u).
    """
    vowels = set("aeiou")
    count = 0
    for i in range(k):
        if s[i] in vowels:
            count += 1

    res = count
    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1
        if s[i - k] in vowels:
            count -= 1
        res = max(res, count)

    return res


# 1004. Max Consecutive Ones III (Medium)
def longestOnes(self, nums: List[int], k: int) -> int:
    """
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
    """
    pass


# 1493. Longest Subarray of 1's After Deleting One Element (Medium)
def longestSubarray(self, nums: List[int]) -> int:
    """
    Given a binary array nums, you should delete one element from it.
    Return the size of the longest non-empty subarray containing only 1's in the resulting array.
    Return 0 if there is no such subarray.
    """
    pass


# PREFIX SUM
# 1732. Find the Highest Altitude (Easy)
def largestAltitude(self, gain: List[int]) -> int:
    """
    There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
    You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
    """
    res = 0
    current = 0
    for i in gain:
        current += i
        res = max(res, current)

    return res


# 724. Find Pivot Index (Easy)
def pivotIndex(self, nums: List[int]) -> int:
    """
    Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
    Return the leftmost pivot index. If no such index exists, return -1.
    """
    leftSum, rightSum = 0, sum(nums)
    for i in nums:
        rightSum -= i
        if leftSum == rightSum:
            return nums.index(i)
        leftSum += i

    return -1


# HASH MAP / SET
# 2215. Find the Difference of Two Arrays (Easy)
def findDifference(self, nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
    Note that the integers in the lists may be returned in any order.
    """
    set1 = set(nums1)
    set2 = set(nums2)
    one = list(set1 - set2)
    two = list(set2 - set1)

    return [one, two]


# 1207. Unique Number of Occurrences (Easy)
def uniqueOccurrences(self, arr: List[int]) -> bool:
    """
    Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
    """
    element_hash = {}
    freq_hash = {}
    for i in arr:
        if i in element_hash:
            element_hash[i] += 1
        else:
            element_hash[i] = 1

    for i in element_hash:
        if element_hash[i] in freq_hash:
            return False
        else:
            freq_hash[element_hash[i]] = 1

    return True


# 1657. Determine if Two Strings Are Close (Medium)
def closeStrings(self, word1: str, word2: str) -> bool:
    """
    Two strings are considered close if you can attain one from the other using the following operations:
    Operation 1: Swap any two existing characters.
    For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
    You can use the operations on either string as many times as necessary.
    Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
    """
    pass


# 2352. Equal Row and Column Pairs (Medium)
def equalPairs(self, matrix: List[List[int]]) -> int:
    """
    Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
    A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
    """
    res = 0
    rows = {}
    for i in matrix:
        row_tuple = tuple(i)
        rows[row_tuple] = rows.get(row_tuple, 0) + 1

    for i in range(len(matrix)):
        col = tuple(matrix[j][i] for j in range(len(matrix)))
        if col in rows:
            res += rows[col]

    return res


# STACK
# 2390. Removing Stars From a String (Medium)
def removeStars(self, s: str) -> str:
    """
    You are given a string s, which contains stars *.
    In one operation, you can:
    Choose a star in s.
    Remove the closest non-star character to its left, as well as remove the star itself.
    Return the string after all stars have been removed.
    Note:
    The input will be generated such that the operation is always possible.
    It can be shown that the resulting string will always be unique.
    """
    stack = []
    for i in s:
        if i == "*" and stack:
            stack.pop()
        else:
            stack.append(i)

    return "".join(stack)


# 735. Asteroid Collision (Medium)
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    """
    We are given an array asteroids of integers representing asteroids in a row.
    For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
    Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
    """
    stack = []
    for i in asteroids:
        while stack and i < 0 < stack[-1]:
            if stack[-1] < -i:
                stack.pop()
                continue
            elif stack[-1] == -i:
                stack.pop()
            break
        else:
            stack.append(i)
    return stack


# 394. Decode String (Medium)
def decodeString(self, s: str) -> str:
    """
    Given an encoded string, return its decoded string.
    The encoding rule is k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
    You may assume that the input string is always valid; no extra white spaces, square brackets are well-formed, etc.
    Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
    The test cases are generated so that the length of the output will never exceed 10^5.
    """
    stack = []
    curr_num = 0
    res = ""

    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == "[":
            stack.append((res, curr_num))
            res, curr_num = "", 0
        elif char == "]":
            prev_str, num = stack.pop()
            res = prev_str + num * res
        else:
            res += char

    return res


# QUEUE
# 933. Number of Recent Calls (Easy)
def __init__(self):
    """
    You have a RecentCounter class which counts the number of recent requests within a certain time frame.
    Implement the RecentCounter class:
    RecentCounter() Initializes the counter with zero recent requests.
    int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
    It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
    """
    pass


def ping(self, t: int) -> int:
    pass


# 649. Dota2 Senate (Medium)
def predictPartyVictory(self, senate: str) -> str:
    """
    In the world of Dota2, there are two parties: the Radiant and the Dire.
    The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
    Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
    Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
    Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.
    The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
    Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".
    """
    pass


# LINKED LIST
# 2095. Delete the Middle Node of a Linked List (Medium)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
    The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
    For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
    """
    pass


# 328. Odd Even Linked List (Medium)
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
    The first node is considered odd, and the second node is even, and so on.
    Note that the relative order inside both the even and odd groups should remain as it was in the input.
    You must solve the problem in O(1) extra space complexity and O(n) time complexity.
    """
    pass


# 206. Reverse Linked List (Easy)
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    """
    pass


# 2130. Maximum Twin Sum of a Linked List (Medium)
def pairSum(self, head: Optional[ListNode]) -> int:
    """
    In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
    The twin sum is defined as the sum of a node and its twin.
    Given the head of a linked list with even length, return the maximum twin sum of the linked list.
    """
    pass


# BINARY TREE - DFS
# 104. Maximum Depth of Binary Tree (Easy)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root: Optional[TreeNode]) -> int:
    """
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    """
    pass


# 872. Leaf-Similar Trees (Easy)
def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """
    Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
    For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
    Two binary trees are considered leaf-similar if their leaf value sequence is the same.
    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
    """
    pass


# 1448. Count Good Nodes in Binary Tree (Medium)
def goodNodes(self, root: Optional[TreeNode]) -> int:
    """
    Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
    Return the number of good nodes in the binary tree.
    """
    pass


# 437. Path Sum III (Medium)
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    """
    You are given a binary tree in which each node contains an integer value.
    Find the number of paths that sum to a given value.
    The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
    """
    pass


# 1372. Longest ZigZag Path in a Binary Tree (Medium)
def longestZigZag(self, root: Optional[TreeNode]) -> int:
    """
    You are given the root of a binary tree.
    A ZigZag path for a binary tree is defined as follow:
    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
    Change the direction from right to left or right to left.
    Repeat the second and third steps until you can't move in the tree.
    Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
    Return the longest ZigZag path contained in that tree.
    """
    pass


# 236. Lowest Common Ancestor of a Binary Tree (Medium)
def lowestCommonAncestor(
    self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":
    """
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."
    """
    pass


# BINARY TREE - BFS
# 199. Binary Tree Right Side View (Medium)
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
    """
    pass


# 1161. Maximum Level Sum of a Binary Tree (Medium)
def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    """
    Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
    Return the smallest level x such that the sum of all the values of the nodes at level x is maximal.
    """
    pass


# BINARY SEARCH TREE
# 700. Search in a Binary Search Tree (Easy)
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    You are given the root of a binary search tree (BST) and an integer val.
    Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
    """
    pass


# 450. Delete Node in a BST (Medium)
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """
    Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
    Basically, the deletion can be divided into two stages:
    Search for a node to remove.
    If the node is found, delete the node.
    """
    pass


# GRAPHS - DFS
# 841. Keys and Rooms (Medium)
def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    """
    There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
    You are given an array rooms where rooms[i] is a set of distinct integers representing keys to room i.
    You know you can enter a room if you have the key to that room.
    Return true if you can enter every room in the building, or false otherwise.
    """
    pass


# 547. Number of Provinces (Medium)
def findCircleNum(self, isConnected: List[List[int]]) -> int:
    """
    There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
    A province is a group of directly or indirectly connected cities and no other cities outside of the group.
    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
    Return the total number of provinces.
    """
    pass


# 1466. Reorder Routes to Make All Paths Lead to the City Zero (Medium)
def minReorder(self, n: int, connections: List[List[int]]) -> int:
    """
    There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different cities (this network form a tree).
    Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
    Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.
    This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
    Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
    It's guaranteed that each city can reach the city 0 after reorder.
    """
    pass


# 399. Evaluate Division (Medium)
def calcEquation(
    self, equations: List[List[str]], values: List[float], queries: List[List[str]]
) -> List[float]:
    """
    You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
    You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
    Return the answers to all queries. If a single answer cannot be determined, return -1.0.
    Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
    Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
    """
    pass


# GRAPHS - BFS
# 1926. Nearest Exit from Entrance in Maze (Medium)
def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    """
    You are given a maze with entrance at the top left corner, (0, 0).
    The maze consists of empty cells and walls. Empty cells are represented as '.' and walls are represented as '+'.
    The maze contains exactly one entrance but the exit can be anywhere. You can move up, down, left, or right from a cell by one unit.
    Return the number of steps to reach the exit. If there is no exit
    """
    pass


# 994. Rotting Oranges (Medium)
def orangesRotting(self, grid: List[List[int]]) -> int:
    """
    You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
    """
    pass


# HEAP/PRIORITY QUEUE
# 215. Kth Largest Element in an Array (Medium)
def findKthLargest(self, nums: List[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Can you solve it without sorting?
    """
    pass


# 2336. Smallest Number in Infinite Set (Medium)
def smallestNumber(self, nums: List[int]) -> int:
    """
    You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
    Implement the SmallestInfiniteSet class:
    SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
    int popSmallest() Removes and returns the smallest integer contained in the infinite set.
    void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
    """


# 2542. Maximum Subsequence Score (Medium)
def maxScore(self, nums: List[int], k: int) -> int:
    """
    You are given an integer array nums of length n and an integer k. You are asked to construct a subsequence of nums of length k that maximizes the score of the subsequence.
    The score of a subsequence is the bitwise-OR of all elements in the subsequence.
    Return the maximum score of the subsequence.
    """
    pass


# 2462. Total Cost to Hire K Workers (Medium)
def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    """
    You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
    You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:
    You will run k sessions and hire exactly one worker in each session.
    In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
    For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
    In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
    If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
    A worker can only be chosen once.
    Return the total cost to hire exactly k workers.
    """


# BINARY SEARCH
# 374. Guess Number Higher or Lower (Easy)
def guessNumber(self, n: int) -> int:
    """
    We are playing the Guess Game. The game is as follows:
    I pick a number from 1 to n. You have to guess which number I picked.
    Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
    You call a pre-defined API int guess(int num), which returns 3 possible results:
    -1: The number I picked is lower than your guess (i.e., pick < num).
    1: The number I picked is higher than your guess (i.e., pick > num).
    0: The number I picked is equal to your guess (i.e., pick == num).
    Return the number that I picked.
    """

    def guess(num: int) -> int:
        pass

    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        res = guess(mid)
        if res == 1:
            left = mid + 1
        elif res == -1:
            right = mid - 1
        else:
            return mid

    return -1


# 2300. Successful Pairs of Spells and Potions (Medium)
def successfulPairs(self, spells: List[int], potions: List[int]) -> int:
    """
    You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
    You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
    Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
    """

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        res = []
        potions.sort()
        for i in spells:
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if i * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1

            res.append(len(potions) - left)

        return res


# 162. Find Peak Element (Medium)
def findPeakElement(self, nums: List[int]) -> int:
    """
    A peak element is an element that is strictly greater than its neighbors.
    Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
    You may imagine that nums[-1] = nums[n] = -∞.  In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
    You must write an algorithm that runs in O(log n) time.
    """
    pass


# 875. Koko Eating Bananas (Medium)
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    """
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards come back.
    Return the minimum integer k such that she can eat all the bananas within h hours.
    """
    pass


# 875. Koko Eating Bananas (Medium)
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    """
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
    Return the minimum integer k such that she can eat all the bananas within h hours.
    """
    pass


# BACKTRACKING
# 17. Letter Combinations of a Phone Number (Medium)
def letterCombinations(self, digits: str) -> List[str]:
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    """
    pass


# 216. Combination Sum III (Medium)
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    """
    Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    Only numbers 1 through 9 are used.
    Each number is used at most once.
    Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
    """
    pass


# 1137. N-th Tribonacci Number (Easy)
def tribonacci(self, n: int) -> int:
    """
    The Tribonacci sequence Tn is defined as follows:
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    Given n, return the value of Tn.
    """
    li = [0, 1, 1]
    if n <= 1:
        return li[n]
    else:
        for i in range(3, n + 1):
            li.append(li[i - 3] + li[i - 2] + li[i - 1])
    return li[-1]


# 746. Min Cost Climbing Stairs (Easy)
def minCostClimbingStairs(self, cost: List[int]) -> int:
    """
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0 or the step with index 1.
    Return the minimum cost to reach the top of the floor.
    """
    pass


# 198. House Robber (Medium)
def rob(self, nums: List[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    """
    pass


# 790. Domino and Tromino Tiling (Medium)
def numTilings(self, n: int) -> int:
    """
    We have two types of tiles: a 2x1 domino shape and an "L" tromino shape. These shapes may be rotated.
    Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
    In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
    """
    pass


# DP - Multidimensional
# 62. Unique Paths (Medium)
def uniquePaths(self, m: int, n: int) -> int:
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 109.
    """
    pass


# 1143. Longest Common Subsequence (Medium)
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.
    """
    pass


# 714. Best Time to Buy and Sell Stock with Transaction Fee (Medium)
def maxProfit(self, prices: List[int], fee: int) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
    Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
    Note:
    You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    The transaction fee is only charged once for each stock purchase and sale.
    """
    pass


# 72. Edit Distance (Medium)
def minDistance(self, word1: str, word2: str) -> int:
    """
    Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
    You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(max(m, n) + 1):
        if i <= m:
            dp[i][0] = i
        if i <= n:
            dp[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insert = dp[i - 1][j]
                delete = dp[i][j - 1]
                replace = dp[i - 1][j - 1]
                dp[i][j] = 1 + min(insert, delete, replace)

    return dp[m][n]


# BIT MANIPULATION
# 338. Counting Bits (Easy)
def countBits(self, n: int) -> List[int]:
    """
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
    """

    def count_bits(n):
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res

    res = []
    for i in range(n + 1):
        res.append(count_bits(i))

    return res

    # res = []
    #     for i in range(n + 1):
    #         res.append(i.bit_count())

    #     return res


# 136. Single Number (Easy)
def singleNumber(self, nums: List[int]) -> int:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.
    """
    xor = 0
    for i in nums:
        xor ^= i
    return xor


# 1318. Minimum Flips to Make a OR b Equal to c (Medium)
def minFlips(self, a: int, b: int, c: int) -> int:
    """
    Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
    Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
    """
    pass


# TRIE
# 208. Implement Trie (Prefix Tree) (Medium)
class Trie:

    def __init__(self):
        """
        A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
        Implement the Trie class:
        Trie() Initializes the trie object.
        void insert(String word) Inserts the string word into the trie.
        boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
        boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
        """
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


# 1268. Search Suggestions System (Medium)
def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    """
    Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
    Return list of lists of the suggested products after each character of searchWord is typed.
    """
    pass


#  Intervals
# 435. Non-overlapping Intervals (Medium)
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    """
    Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
    Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
    """
    pass


# 452. Minimum Number of Arrows to Burst Balloons (Medium)
def findMinArrowShots(self, points: List[List[int]]) -> int:
    """
    There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
    Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
    Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
    """
    pass


# MONOTONIC STACK
# 739. Daily Temperatures (Medium)
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    """
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
    """
    res = [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)

    return res


# 901. Online Stock Span (Medium)
class StockSpanner:

    def __init__(self):
        """
        Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
        The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.
        For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
        Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
        Implement the StockSpanner class:
        StockSpanner() Initializes the object of the class.
        int next(int price) Returns the span of the stock's price given that today's price is price.
        """
        pass

    def next(self, price: int) -> int:
        pass

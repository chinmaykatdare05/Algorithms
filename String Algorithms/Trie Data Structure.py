class TrieNode:
    """
    Represents a single node in the Trie.
    """

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """
    A Trie (Prefix Tree) implementation.

    Time Complexity:
        - Insertion: O(n), where n is the length of the word
        - Search: O(n)
        - Starts with: O(n)
    Space Complexity:
        - O(N * M), where N is the number of words and M is the average word length
    """

    def __init__(self):
        """Initializes the Trie with a root node."""
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.

        Args:
            word (str): The word to insert.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """
        Searches for a complete word in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word exists, False otherwise.
        """
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        """
        Checks if any words in the Trie start with the given prefix.

        Args:
            prefix (str): The prefix to check.

        Returns:
            bool: True if any word starts with the prefix, False otherwise.
        """
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        """
        A helper function to traverse the Trie to a given node based on the prefix.

        Args:
            prefix (str): The prefix to find.

        Returns:
            TrieNode or None: The last node in the prefix path or None if not found.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# 🚀 Example Usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("batman")

# Test cases
print(trie.search("apple"))  # True
print(trie.search("app"))  # True
print(trie.search("bat"))  # True
print(trie.search("batman"))  # True
print(trie.search("batwoman"))  # False
print(trie.starts_with("app"))  # True
print(trie.starts_with("batw"))  # True
print(trie.starts_with("cat"))  # False

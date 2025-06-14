class TrieNode:
    """
    A single node in the Trie.
    """

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie Data Structure supporting Insert, Search, StartsWith (prefix search), and Deletion.
    """

    def __init__(self):
        """
        Initialize the root node of the Trie.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.

        Time complexity: O(n) where n is the length of the word.
        Space complexity: O(ALPHABET_SIZE * n)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Search for a word in the Trie.

        Time complexity: O(n) where n is the length of the word.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Check if any word in the Trie starts with the given prefix.

        Time complexity: O(n) where n is the length of the prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        """
        Delete a word from the Trie (if it exists).

        Time complexity: O(n) where n is the length of the word.
        """

        def _delete(node, word, depth):
            if not node:
                return False

            # If we reach the end of the word
            if depth == len(word):
                # Mark this node as not end of word
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    # If node has no children, delete it
                    return len(node.children) == 0
                return False

            char = word[depth]
            if char not in node.children:
                return False

            # Recurse to the next character
            should_delete = _delete(node.children[char], word, depth + 1)

            # If the child node should be deleted, remove it from the dictionary
            if should_delete:
                del node.children[char]
                # Return True if the current node has no children and is not the end of another word
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        _delete(self.root, word, 0)


# 🎯 **Example Usage**
trie = Trie()

# 🚀 Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("batman")

# 🔍 Search words
print(trie.search("apple"))  # Output: True
print(trie.search("app"))  # Output: True
print(trie.search("bat"))  # Output: True
print(trie.search("batman"))  # Output: True
print(trie.search("batmobile"))  # Output: False

# 🔎 Prefix search
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("batm"))  # Output: True
print(trie.starts_with("cat"))  # Output: False

# 🔧 Delete words
trie.delete("batman")
print(trie.search("batman"))  # Output: False
print(trie.search("bat"))  # Output: True (still exists)

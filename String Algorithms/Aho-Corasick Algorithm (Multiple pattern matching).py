class AhoCorasickNode:
    """
    Node structure for the Aho-Corasick Trie.
    """

    def __init__(self):
        self.children = {}
        self.fail_link = None
        self.output = []


class AhoCorasick:
    """
    Aho-Corasick Algorithm for multiple pattern matching.

    Time Complexity:
        - Build Trie: O(m), where m is the total length of all patterns.
        - Build Failure Links: O(m)
        - Search: O(n + output), where n is the length of the text and output is the number of matches found.

    Space Complexity: O(m * σ), where σ is the alphabet size.
    """

    def __init__(self, patterns):
        self.root = AhoCorasickNode()
        self.build_trie(patterns)
        self.build_failure_links()

    def build_trie(self, patterns):
        """
        Build a trie from the given patterns.
        """
        for pattern in patterns:
            node = self.root
            for char in pattern:
                if char not in node.children:
                    node.children[char] = AhoCorasickNode()
                node = node.children[char]
            node.output.append(pattern)

    def build_failure_links(self):
        """
        Build failure links (BFS style).
        """
        from collections import deque

        queue = deque()
        # Set root children's failure links to root itself
        for node in self.root.children.values():
            node.fail_link = self.root
            queue.append(node)

        # BFS to establish failure links for deeper nodes
        while queue:
            current_node = queue.popleft()
            for char, child_node in current_node.children.items():
                # Set failure link
                fail = current_node.fail_link
                while fail is not None and char not in fail.children:
                    fail = fail.fail_link
                child_node.fail_link = fail.children[char] if fail else self.root
                # Merge output from fail_link to child_node
                child_node.output.extend(child_node.fail_link.output)
                queue.append(child_node)

    def search(self, text):
        """
        Search for patterns in the given text.
        Returns a list of tuples (end_index, matched_pattern).
        """
        node = self.root
        matches = []

        for index, char in enumerate(text):
            # Follow fail links on mismatches
            while node is not None and char not in node.children:
                node = node.fail_link

            # If match found, move to the corresponding node
            if node:
                node = node.children.get(char, self.root)
            else:
                node = self.root

            # Check if we've reached any output node
            if node.output:
                for pattern in node.output:
                    matches.append((index - len(pattern) + 1, pattern))

        return matches


# 🚀 **Example Usage**

patterns = ["he", "she", "his", "hers"]
text = "ahishers"

aho_corasick = AhoCorasick(patterns)
matches = aho_corasick.search(text)

print("Matches found:")
for index, pattern in matches:
    print(f"Pattern '{pattern}' found at index {index}")

import heapq


class HuffmanNode:
    """Represents a node in the Huffman Tree."""

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq  # Min Heap priority based on frequency


def build_huffman_tree(freq_dict):
    """
    Builds the Huffman Tree and returns the root node.

    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)  # Convert to Min Heap

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge nodes with a new node (internal node)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left, merged.right = left, right

        heapq.heappush(heap, merged)

    return heap[0]  # Root node of the Huffman tree


def generate_huffman_codes(root, prefix="", huffman_dict={}):
    """
    Generates Huffman Codes using a recursive tree traversal.

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if root is None:
        return

    if root.char is not None:  # Leaf node
        huffman_dict[root.char] = prefix

    generate_huffman_codes(root.left, prefix + "0", huffman_dict)
    generate_huffman_codes(root.right, prefix + "1", huffman_dict)

    return huffman_dict


def huffman_encoding(freq_dict):
    """
    Main function to generate Huffman Codes for given character frequencies.

    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    root = build_huffman_tree(freq_dict)
    return generate_huffman_codes(root)


# Example Usage
freq_dict = {"A": 5, "B": 9, "C": 12, "D": 13, "E": 16, "F": 45}
huffman_codes = huffman_encoding(freq_dict)

print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")

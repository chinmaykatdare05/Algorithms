import heapq


class ListNode:
    """Definition for singly-linked list nodes."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    """
    Merges K sorted linked lists into one sorted linked list using a Min-Heap.

    Time Complexity: O(N log K)
    - N: Total number of nodes across all lists.
    - K: Number of linked lists.
    - Each insertion and removal from the heap takes O(log K).

    Space Complexity: O(K)
    - The heap holds at most K nodes (one from each list).

    """
    # Min-heap initialization
    heap = []

    # Push the head of each linked list into the heap
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))

    # Dummy head to build the final merged list
    dummy = ListNode()
    current = dummy

    # Process the heap until it's empty
    while heap:
        val, i, node = heapq.heappop(heap)

        # Add the smallest node to the result list
        current.next = node
        current = current.next

        # If there's a next node, push it into the heap
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# 🔥 Helper function to create linked lists
def build_linked_list(values):
    """Converts a list of values into a linked list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 🔥 Test the function
lists = [
    build_linked_list([1, 4, 5]),
    build_linked_list([1, 3, 4]),
    build_linked_list([2, 6]),
]

merged_list = merge_k_lists(lists)

# Display the merged list
current = merged_list
result = []
while current:
    result.append(current.val)
    current = current.next

print("Merged K Sorted Lists:", result)

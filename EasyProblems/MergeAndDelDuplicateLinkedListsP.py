from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: 
      current = head 
      while current and current.next: 
        if current.val == current.next.val: 
          current.next = current.next.next 
        else:
           current = current.next
      return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the starting point of the merged list
        list3 = ListNode()
        current = list3

        # Iterate through both lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining part of the list that is not exhausted
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list, which starts after the dummy node
        return list3.next

# Example usage:
# Helper function to convert list to linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(node):
    while node:
        print(node.val,end = " ")
        node = node.next

# Example lists
list1 = create_linked_list([2, 2 ,2, 5, 7, 7])
list2 = create_linked_list([1, 3, 4])

# Merge lists
solution = Solution()
#merged_list = solution.mergeTwoLists(list1, list2)
FineList = solution.deleteDuplicates(list1)
# Print the merged list
print_linked_list(FineList)

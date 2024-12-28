from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next

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
    n =10
    while node and n >0:
        print(node.val,end = " ")
        node = node.next
        n-=1

# Example lists
list1 = create_linked_list([1,1,1,2,3,1,4,1,5])

solution = Solution()

listReturned = solution.removeElements(list1,1)

print_linked_list(listReturned)

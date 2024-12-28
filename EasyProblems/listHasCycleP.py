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

# Example usage:
# Helper function to convert list to linked list
def create_linked_list(arr,pos):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    curr2 =head.next
    if pos == 0 :
      current.next = head
    else :
      for i in range(pos) :
        current.next =curr2
        curr2=curr2.next
    return head  
    

# Helper function to print linked list
def print_linked_list(node):
    n =10
    while node and n >0:
        print(node.val,end = " ")
        node = node.next
        n-=1

# Example lists
pos = 2
list1 = create_linked_list([1,2,3,4,5], pos)

solution = Solution()

listCheck = solution.hasCycle(list1)

print(listCheck)
print_linked_list(list1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(hasCycle(node1))  
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

print(hasCycle(node1)) 

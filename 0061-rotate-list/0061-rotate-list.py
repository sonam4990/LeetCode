class Solution:
    def rotateRight(self, head, k):
        
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find length
        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Make circular
        tail.next = head
        
        # Step 3: Optimize k
        k = k % length
        
        # Step 4: Find new tail
        steps = length - k - 1
        new_tail = head
        
        for _ in range(steps):
            new_tail = new_tail.next
        
        # Step 5: New head
        new_head = new_tail.next
        
        # Step 6: Break
        new_tail.next = None
        
        return new_head
class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None


class linkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.head is None:
            return -1
        
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val            
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head is None:
            self.head = Node(val)
        else:    
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)
        self.size += 1    
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == self.size:
            self.addAtTail(val)
            return
        if index < 0 or index > self.size:
            return
        
        
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        node = Node(val)
        node.next = cur.next
        cur.next = node
        self.size += 1
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.head is None:
            return -1
        
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        cur.next = cur.next.next
    
        self.size -= 1
l=linkedList()
l.addAtTail(2)
l.addAtTail(3)
l.addAtTail(4)
l.addAtTail(55)
print (l.get(2))


from typing import Iterable
from node import Node

class LinkedList:

    def print_ll(self, head : Node):
        """
        Purpose : Prints the linked list
        Input Parameters:
            1. head  - Header node of the linked list 
        Outputs:
            None
        """
        while head.next is not None:
            print(head.data, '->', end = ' ')
            head = head.next
        print(f'{head.data} -> None')

    def length(self, head:Node) -> None:
        """
        Purpose : Length of the linked list
        Input Parameters:
            1. head  - Header node of the linked list
        Outputs:
            Length of the linked list
        """
        ct = 1
        while head.next is not None:
            ct += 1
            head = head.next
        return ct

    def create_ll(self, elements:Iterable) -> Node:
        """
        Purpose : To create a linked list
        Input parameters :
         1. An iterable of elements to be added
        Outputs : 
            Returns the head of the linked list
        """
        assert len(elements) > 0, 'Your input has 0 elements'
        head, tail = None, None
        for element in elements:
            newNode = Node(element)
            if head is None:
                head = newNode
                tail = head
            else:
                tail.next = newNode
                tail = tail.next
        return head

    def insert(self, head : Node, data : int, pos : int)  -> Node:
        """
        Purpose : To add elements at a specific position of the linked list
        Input parameters :
         1. head - Header node of the linked list
         2. data - Data to be inserted
         3. pos - The position to be inserted (starts from 0 index)
        Outputs : 
            Returns the head of the linked list
        """
        leng = self.length(head)
        assert pos >= 0 and pos <= self.length(head), f'Indices should range from 0 to {leng}'
        prev, curr = None, head
        ct = 0
        while ct < pos:
            ct += 1
            prev = curr
            curr = prev.next
        newNode = Node(data)
        if prev is None:
            head = newNode
        else:
            prev.next = newNode
        newNode.next = curr # in case of prev is None newNode.next is actually equal to head.next (shallow copy)
        return head

    def delete(self, head : Node, pos : int)  -> Node:
        """
        Purpose : To add elements at a specific position of the linked list
        Input parameters :
         1. head - Header node of the linked list
         2. pos - The position to be deleted (starts from 0 index)
        Outputs : 
            Returns the head of the linked list
        """
        leng = self.length(head)
        assert pos >= 0 and pos < self.length(head), f'Indices should range from 0 to {leng}'
        prev, curr = None, head
        ct = 0
        while ct < pos:
            prev = curr
            curr = prev.next
            ct += 1
        if prev is None:
            head = curr.next
        else:
            prev.next = curr.next
        return head

    def reverse(self, head):
        """
         Purpose : To reverse the elements of the linked list
         Input parameters :
         1. head - Header node of the linked list
         Outputs : 
            Returns the head of the linked list
        """
        if head.next is None:
            return head
        newHead = self.reverse(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return newHead
    
    def mid_point(self, head : Node) -> Node:
        """
         Purpose : To get the midpoint of the linked list
         Input parameters :
         1. head - Header node of the linked list
         Outputs : 
            Returns the mid point node
        """
        slow, fast = head.next, head.next.next
        while slow.next is not None and fast.next.next is not None:
            slow = fast
            fast = fast.next
        return slow


if __name__ == '__main__':
    o1 = LinkedList()
    head = o1.create_ll([1,2,3]) 
    leng = o1.length(head)
    print(f'The length of the linked list is {leng}')
    o1.print_ll(head)
    head = o1.insert(head, 4, 3)
    o1.print_ll(head)
    print(f'The mid point is {o1.mid_point(head).data}')
    head = o1.delete(head, 3)
    o1.print_ll(head)
    rev_ll = o1.reverse(head)
    o1.print_ll(rev_ll)

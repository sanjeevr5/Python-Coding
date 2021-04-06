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
        newNode.next = curr
        return head            


if __name__ == '__main__':
    o1 = LinkedList()
    head = o1.create_ll([1,2,3]) 
    leng = o1.length(head)
    print(f'The length of the linked list is {leng}')
    o1.print_ll(head)

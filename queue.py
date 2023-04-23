#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    module for a queue using a double chained list
"""

from DLL import DoublyLinkedList

class Queue:
    """
        represent a queue (FIFO)
        use a Doubly linked list as a base
        
        attributes
        ----------
        base : Doubly linked list
        
        methods
        -------
        is_empty() -> bool:
            test if the queue is empty
        enqueue(element: any) -> None:
            thread a new element in the queue
        dequeue() -> any:
            unthread the first element and return it
        head() -> any:
            check the first element
    """
    
    def __init__(self):
        """
            queue class' constructor
            set up attributes
            
            parameters
            ----------
            None
            
            returns
            -------
            None
        """
        self.base = DoublyLinkedList()
    
    def is_empty(self):
        """
            test if the queue is empty
            
            parameters
            ----------
            None
            
            returns
            -------
            bool
                True if the queue is empty
        """
        return self.base.is_empty()
    
    def enqueue(self, element) -> None:
        """
            thread a new element in the queue
            (add it at the end)
            
            parameters
            ----------
            element: any
                the new element
            
            returns
            -------
            None
            
            side effects
            ------------
            add a new element to the queue
        """
        self.base.insert_end(element)
    
    def dequeue(self):
        """
            unthread the first element from the queue
            
            parameters
            ----------
            None
            
            returns
            -------
            any
                the first element of the queue
            
            side effects
            ------------
            remove the element from the queue
        """
        return self.base.remove_first()
    
    def head(self):
        """
            check the first element of the queue
            this won't remove it from the queue
            
            parameters
            ----------
            None
            
            returns
            -------
            any
                the first element
        """
        return self.base.head()

if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(4)
    print(queue.is_empty())
    queue.enqueue(5)
    print(queue.head())
    queue.dequeue()
    print(queue.is_empty())
    print(queue.head())

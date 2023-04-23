#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    an implementation of a double chained list
"""

class DoublyLinkedList:
    """
        a double chained list
        allow to access the first and the last element
        
        attributes
        ----------
        first: Link
            the first link of the list
        last: Link
            the last link of the list
        
        methods
        -------
        is_empty() -> bool:
            test if the list is empty
        head() -> any:
            check the first element
        tail() -> any:
            check the last element
        insert_beginning(element) -> None:
            insert a new element at the beginning of the list
        insert_end(element) -> None:
            insert a new element at the end of the list
        remove_first() -> any:
            remove the first element
        remove_last() -> any:
            remove the last element
    """
    
    def __init__(self, first=None, last=None):
        """
            DCL class' constructor
            set up the attributes
            
            attributes
            ----------
            first: Link
                the first link of the list (default None)
            last: Link
                the last link of the list (default None)
            
            returns
            -------
            None
        """
        self.first = first
        self.last = last
    
    def is_empty(self) -> bool:
        """
            test if the list contain any element
            
            parameters
            ----------
            None
            
            returns
            -------
            bool
                True if the list is empty
        """
        return self.first is None
    
    def head(self):
        """
            check the data of first element of the list
            this won't remove it from the list
            
            parameters
            ----------
            None
            
            returns
            -------
            any
                the first element
        """
        if self.is_empty():
            raise DoublyLinkedListError('list is empty')
        return self.first.data
    
    def tail(self):
        """
            check the data of last element of the list
            this won't remove it from the list
            
            parameters
            ----------
            None
            
            returns
            -------
            any
                the last element
        """
        if self.is_empty():
            raise DoublyLinkedListError('list is empty')
        return self.last.data
    
    def insert_beginning(self, element) -> None:
        """
            insert a new element at the first position
            this will alter the original list
            
            parameters
            ----------
            element: any
                the element to add
            
            returns
            -------
            None
            
            side effects
            ------------
            add a new element to the list
        """
        new_node = Node(data = element)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
            self.first.next.prev = new_node
        return None
    
    def insert_end(self, element) -> None:
        """
            insert a new element at the last position
            this will alter the original list
            
            parameters
            ----------
            element: any
                the element to add
            
            returns
            -------
            None
            
            side effects
            ------------
            add a new element to the list
        """
        new_node = Node(data = element)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last = new_node
            self.last.prev.next = new_node
        return None
    
    def remove_first(self) -> None:
        """
            remove the first element of the list and return it
            this will alter the original list
            
            parameters
            ----------
            None
            
            returns
            -------
            result: any
                the first element
            
            side effects
            ------------
            remove an element from the list
        """
        result = self.first.data
        if self.is_empty():
            raise DoublyLinkedListError('list is empty')
        if self.first.next is None:
            self.last = None
        self.first = self.first.next
        return result
    
    def remove_last(self) -> None:
        """
            remove the last element of the list and return it
            this will alter the original list
            
            parameters
            ----------
            None
            
            returns
            -------
            result: any
                the last element
            
            side effects
            ------------
            remove an element from the list
        """
        result = self.last.data
        if self.is_empty():
            raise DoublyLinkedListError('list is empty')
        if self.last.prev is None:
            self.first = None
        self.last = self.last.prev
        return result


class Node:
    """
        a node of a double chained list
        
        attributes
        ----------
        data: any
            the data stored at this node
        next: DLL
            the rest of the list
        previous: DLL
            the beginning of the list
    """
    
    def __init__(self,
        data=None,
        next=None,
        prev=None):
        """
            Node class' constructor
            set up the attributes
            
            parameters
            ----------
            data: any
                the data to store
            next: DCL
                the rest of the list (default an empty DLL)
            previous: DCL
                the beginning of the list (default an empty DLL)
            
            returns
            -------
            None
        """
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedListError(Exception):
    """
        an exception for all that is related to Doubly linked lists
    """
    pass

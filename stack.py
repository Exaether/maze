#!/usr/bin/env python
#-*- coding:utf-8 -*-

import LSC

class Stack:
    """
        class stack that use a simply chained list as base
        
        attributes
        ----------
        SCL: LSC
            the base SCL
        
        methods
        -------
        is_empty() -> bool:
            test if the stack is empty
        push(element) -> None:
            stack a new element on top
        pop() -> any:
            unstack the top element
        top() -> any:
            check the top element
    """
    
    def __init__(self) -> None:
        """
            stack class' constructor
            set up the attributes
            
            parameters
            ----------
            None
            
            returns
            -------
            None
        """
        self.SCL = LSC.creer_liste_vide()
    
    def is_empty(self) -> bool:
        """
            test if the stack is empty
            
            parameters
            ----------
            None
            
            returns
            -------
            bool
                True if the stack is empty
        """
        return LSC.est_vide(self.SCL)
    
    def push(self, element) -> None:
        """
            stack a new element on top of the stack
            
            parameters
            ----------
            element: any
                the element to stack
            
            returns
            -------
            None
        """
        self.SCL = LSC.ajouter_en_tete(self.SCL, element)
        return None
    
    def pop(self):
        """
            unstack the top element of the stack
            and return it
            
            parameters
            ----------
            None
            
            returns
            -------
            result: any
                the top element
        """
        result = LSC.tete(self.SCL)
        self.SCL = LSC.queue(self.SCL)
        return result
    
    def top(self):
        """
            check the top element of the stack
            do not remove it from the stack
            
            parameters
            ----------
            None
            
            returns
            -------
            any
                the top element
        """
        return LSC.tete(self.SCL)

if __name__ == '__main__':
    print(Stack().is_empty())
    stack = Stack()
    stack.push(4)
    print(stack.is_empty())


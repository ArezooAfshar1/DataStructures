# !/usr/bin/python3.11.0

from typing import Any

class node:
    __slots__ = ('data', 'next')        
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class list:
    
    __slots__ = ('head', 'tail', 'size')
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self,) -> bool:
        """ simply checking the weather list is null or not """
        return self.size == 0

    def addTohead(self, data) -> None:
        """ adding a new node in front of list equivalent to pushFront method """
        
        self.head = node(data, self.head)
        if(self.isEmpty()):
            self.tail = self.head
        self.size += 1

    def addToTail(self, data) -> None:
        """ adding a new node in back of list equivalent to pushBack method """
        
        newNode = node(data)
        if(self.isEmpty()):
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.size += 1

    def insertAt(self, data, index: int) -> None:
        """ inserting a new node after index-1 """

        newNode = node(data)
        match index:
            case 0:
                self.addTohead(data)
            case self.size:
                self.addToTail(data)
            case _:
                if not(self.isEmpty()):
                    tempNode = self.head
                    while index > 1:
                        tempNode = tempNode.next
                        index -= 1
                    newNode.next, tempNode.next = tempNode.next, newNode
                    self.size += 1

    def deleteFromHead(self) -> Any:
        """ deleting in front of list equivalent to popFront method """
        
        data = None
        if not(self.isEmpty()):
            data = self.head.data
            if(self.head.next == None):
                self.head = self.tail = None
            else:
                self.head = self.head.next
        self.size -= 1
        
        return data
        
    def deleteFromTail(self) -> None:
        """ deleting in back of list equivalent to popBack method """
        
        data = None
        if not(self.isEmpty()):
            data = self.tail.data
            if (self.head.next == None):
                self.head = self.tail = None
            else:
                temp = self.head
                while (temp.next != self.tail):
                    temp = temp.next
                self.tail = temp
                temp.next = None
        self.size -= 1
        
        return data

if __name__ == "__main__":
    print("you are in it but there is no init.")
import random as rd
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Players:
    def __init__(self,lst):
        self.head = None
        self.tail = None
        for i in lst:
            newNode = Node(i, None)
            if self.head is None:     
                self.head = newNode    
                self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = newNode
                self.tail.next = self.head
    def size(self):
        c = 0
        currentNode = self.head 
        while currentNode.next is not self.head:
            c+=1
            currentNode = currentNode.next
        c+=1
        return c
    
    def nodeAt(self, idx):          
        i = 0
        currentNode = self.head
        while currentNode is not None:
            if i is idx:
                return currentNode
            currentNode = currentNode.next
            i+=1
    
    def showPlayers(self):
        currentNode = self.head
        print(currentNode.data,end=" -> ")
        currentNode = self.head.next
        while currentNode is not self.head:

            print(currentNode.data,end="")
            if currentNode.next is not None:
                print(" -> ",end="")
            currentNode = currentNode.next
        print()

    def removeMiddlenode(self):
        currentNode = self.head
        size = self.size()
        prevMiddleNode = self.nodeAt(int((size/2)-1))
        temp = prevMiddleNode.next
        prevMiddleNode.next = prevMiddleNode.next.next
        temp = None 

        

    def play(self):
        currentNode = self.head 
        while True:
            lastNode = self.nodeAt(self.size()-1)
            self.head = lastNode 
            if rd.randint(0,3) == 1:
                self.removeMiddlenode()
                self.showPlayers()

            if self.size() == 1:
                break 
            
        



obj = Players(["Steve","Tony","Bruce","Thor","Natasha","Clint","Abesh"])
obj.showPlayers() 
obj.play() 

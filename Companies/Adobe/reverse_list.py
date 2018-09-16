#function Template for python3
"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""
# your task is to complete this function
# function shouldn't return anything
# use self.head to access head in the method
def reverseList(self):
    # Code here
    if self.head is None:
        return None
    prev=None
    curr=self.head
    nex=curr.next
    while(curr!=None):
        curr.next=prev
        prev=curr
        curr=nex
        if nex!=None:
            nex=nex.next
    self.head=prev

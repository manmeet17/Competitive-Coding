# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# your task is to complete this function
# function should return true/false or 1/0
def isPalindrome(head):
    # Code here
    stack=[]
    slow=head
    while head!=None:
        if head:
            stack.append(head.data)
        head=head.next
    f=1
    while slow!=None:
        if stack.pop()!=slow.data:
            f=0
            break
        slow=slow.next
    if f==1:
        return 1
    return 0

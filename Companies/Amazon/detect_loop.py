def detectLoop(head):
    temp=head
    f=0
    while head.next is not None:
        head=head.next
        temp=temp.next.next
        if(head.data==temp.data):
            f=1
            break
    return True if f==1 else False

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
##########solution1##########
def mergeTwoLists(self,l1,l2):
    p=q=ListNode(0)
    while l1 and l2:
        if l1.val<l2.val:
            q.next=l1
            l1=l1.next
        else:
            q.next=l2
            l2=l2.next
        q=q.next
    if l1:
        q.next=l1
    else:
        q.next=l2
    return p.next

#######solution2############

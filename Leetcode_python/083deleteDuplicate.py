class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def deleteDuplicates(self, head):
        res=[]
        q=p=ListNode(0)
        while head:
            if head  not in res:
                res.append(head.val)
            head=head.next
        for i in range(len(res)):
            node=ListNode(res[i])
            p.next=node
        return q.next
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
####注意这道题并不是把重复元素全部去掉而是保留一个####

#####solution1##########
class Solution:
    def deleteDuplicates(self, head):
        res=[]
        p=ListNode(0)
        q=p
        while head:
            if head.val not in res:
                res.append(head.val)
            head=head.next
        for i in res:
            node=ListNode(i)
            p.next=node
            p=p.next
        return q.next
######solution2####faster####
class Solution:
    def deleteDuplicates(self, head):
        dummy_head = ListNode("*")
        prev_node = dummy_head
        while head:
            if head.val != prev_node.val:
                prev_node.next = head
                prev_node = head
            head = head.next
        prev_node.next = None
        return dummy_head.next
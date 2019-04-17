class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def addTwoNumbers(self,l1:ListNode,l2:ListNode):
    temp=0
    s = ListNode(0)
    pre=s
    while l1 and l2:
        a=l1.val+l2.val+temp
        temp=0
        if 0<=a<10:
            node=ListNode(a)
            pre.next=node
            pre=pre.next
        else:
            node=ListNode(a%10)
            pre.next = node
            pre = pre.next
            temp=a//10
        l1 = l1.next
        l2 = l2.next
    while l1:
        a=l1.val+temp
        temp=0
        if 0<=a<10:
            node = ListNode(a)
            pre.next = node
            pre = pre.next
        else:
            node = ListNode(a % 10)
            pre.next = node
            pre = pre.next
            temp = a // 10
        l1=l1.next
    while l2:
        a=l2.val+temp
        temp = 0
        if 0<=a<10:
            node = ListNode(a)
            pre.next = node
            pre = pre.next
        else:
            node = ListNode(a % 10)
            pre.next = node
            pre = pre.next
            temp = a // 10
        l2=l2.next
    if temp!=0:
        node = ListNode(temp)
        pre.next = node
        pre = pre.next
    return s.next




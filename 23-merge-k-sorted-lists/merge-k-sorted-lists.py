# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2list(l1,l2):
            if l1==None: return l2
            elif l2==None: return l1
            else:
                if l1.val<=l2.val:
                    l1.next=merge2list(l1.next,l2) 
                    return l1
                else:
                    l2.next=merge2list(l1,l2.next)
                    return l2
        def PartitionandMerge(startnode,endnode,lists):
            if startnode==endnode:
                return lists[startnode]
            else:
                mid=startnode+(endnode-startnode)//2
                l1=PartitionandMerge(startnode,mid,lists)
                l2=PartitionandMerge(mid+1,endnode,lists)
                return merge2list(l1,l2)

        if not lists or len(lists) == 0:
            return None

        return PartitionandMerge(0, len(lists) - 1, lists)

        
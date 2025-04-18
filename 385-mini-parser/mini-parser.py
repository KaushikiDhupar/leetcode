# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        context = None
        item = None
        stack = []
        sign = 1

        for token in s:
            if token.isdigit():
                if item is None:
                    item = NestedInteger()
                item.setInteger(10*(item.getInteger() or 0) + sign * int(token))
            elif token == '-':
                sign = -1
            elif token == '[':
                stack.append(context)
                context = NestedInteger()
                item = None
            elif token == ']':
                if item is not None:
                    context.add(item)
                item = context
                context = stack.pop()
            elif token == ',':
                context.add(item)
                item = None
                sign = 1
        return item
     
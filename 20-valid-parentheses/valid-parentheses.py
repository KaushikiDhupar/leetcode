class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values(): #either it will be an opening parethensis 
                stack.append(char) #if opening parenthsis simply push
            elif char in mapping.keys(): #or it will be closing parenthsis
                if not stack or mapping[char] != stack.pop(): #if closing parenthisis 
                #check if either stack is empty or closing parenthsis doesnt match opening parenthsis 
                    return False  #if any 1 condition is true return False
        
        return not stack # return if stack empty=true if stack not empty false
class Solution(object):
    def isValid(self, s):
        
        bracket_map= {')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in bracket_map:
                if stack and stack[-1]==bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
    pass







    



  


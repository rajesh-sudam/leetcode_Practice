class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        arr=[]
        for i in range(len(s)):
            if s[i]=='('or s[i]=='[' or s[i]=='{':
                arr.append(s[i])
            else:
                if not arr:
                    return False
                top=arr.pop()
                if s[i]==')' and top!='(':
                    return False
                if s[i]==']' and top!='[':
                    return False
                if s[i]=='}' and top!='{':
                    return False
        return len(arr)==0
        
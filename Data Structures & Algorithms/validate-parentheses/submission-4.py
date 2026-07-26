class Solution:
    def isValid(self, s: str) -> bool:

        dict = {')' : '(', '}' : '{' , ']' : '['  }

        queue = []

        for char in s:
            if char not in dict:
                queue.append(char)
            else:
                if len(queue) == 0:
                    return False
                elif dict[char] != queue[len(queue)-1]:
                    return False
                else:
                    queue.pop()

        if len(queue) == 0:
            return True
        
        return False




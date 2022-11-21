from collections import deque

def brackets (line):
    brackets_deque=deque()
    for i in line:
        if i == '(':
            brackets_deque.append(i)
        elif i == ')':
            if len(brackets_deque) == 0:
                return False
            brackets_deque.pop()
    if len(brackets_deque) == 0:
        return True
    return False

print (brackets('()()'))
 
from collections import Counter
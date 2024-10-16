#accessing = O(1)
#insertion = O(1)
#deletion = O(1)
#searchin = O(N)

stack = []
for i in range(10):
    stack.append(i+1)


print("Initial Stack: ",stack)

stack.pop()
print("After removing last element: \n",stack)

stack.remove(stack[0])
print("After removing first element: \n",stack)

print("Accessing top element",stack[-1])



##############################################################################################################################################################################


#stack using deque
from collections import deque

stack_deque = deque(stack)

print(stack_deque)

stack_deque.append(10)

print(stack_deque)

stack_deque.appendleft(1)

print(stack_deque)

stack_deque.pop()

print(stack_deque)

stack_deque.popleft()

print(stack_deque)



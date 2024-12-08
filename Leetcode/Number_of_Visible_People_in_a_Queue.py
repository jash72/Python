def fun(heights):
    ans = [0]*len(heights)
    stack = []
    for i in reversed(range(len(heights))): 
        while stack and stack[-1] <= heights[i]: 
            ans[i] += 1
            stack.pop()
        if stack: 
            ans[i] += 1
        stack.append(heights[i])
        print()
    return ans
    
heights = [10,6,8,5,11,9]
print(fun(heights))
nums = [-1, 0, 2, 6, 7, 11, 15, 19, 21, 77, 89]
target = 17
front = 0
rear = len(nums) - 1
while(front<rear):
    if(nums[front] == target or nums[rear] == target):
        print("Present")
        break
    else:
        front += 1
        rear -= 1
else:
    print("Not Found")



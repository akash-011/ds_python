def serach_insert_postion(nums, target):
    x =0
    y = len(nums) - 1

    while x <= y:
        mid = (x + y) // 2
        if (nums[mid] == target):
            return mid
        elif target > nums[mid]: 
            x = mid + 1
        else:
            y = mid -1 

    return x 

"""
Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
#time complexity - O(n^2)
#Space complexity - O(1)
def two_sum_1(arr, target):
    #brute force approach 
    for i in range(len(arr)-1):
        for j in range(i+1 , len(arr)):
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j])
                return True 
    return False

#time complexity - O(n)
#space complexity - O(n)
def two_sum_2(arr, target):
    #using a hashtable
    hash_table = {}
    for i in range(len(arr)):
        if arr[i] in hash_table:
            print(hash_table[arr[i]], arr[i] )
            return True
        else:
            hash_table[target - arr[i]] = arr[i]
    return False       


def two_sum_3(arr, target):
    #array needs to be sorted for this to work
    i = 0
    j = len(arr) - 1

    while i <= j:
        if arr[i] + arr[j] ==  target:
            print (arr[i], arr[j])
            return True
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1 
    
    return False 


if __name__ == "__main__":
    print(two_sum_3([-1,2,3,5,6,10], 13))
    print(two_sum_3([-1,2,3,5,6,10], 19))
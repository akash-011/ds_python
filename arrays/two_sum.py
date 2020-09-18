"""
Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
def two_sum_1(arr, target):
	#brute force approach - n squared
	for i in range(len(arr)-1):
		for j in range(i+1 , len(arr)):
			if arr[i] + arr[j] == target:
				print(arr[i], arr[j])
				return True 
	return False

if __name__ == "__main__":
	print(two_sum_1([-1,2,5,6,3,10], 13))
	print(two_sum_1([-1,2,5,6,3,10], 19))



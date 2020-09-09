"""
Array Advanced Game 

You are given an array of non-negative. For Example:

[3,3,1,0,1,2,5]

Each number represents the mazimun you can advance in an array 

Is it possible to advance from the start to array to the last element ?

"""
def arrays_game(arr):

	furthest_reached = 0 
	last_index = len(arr) - 1
	i = 0 

	while i <= furthest_reached and furthest_reached < last_index:
		furthest_reached = max(furthest_reached, arr[i] + i)
		i += 1
	
	return furthest_reached >= last_index

a1 = [3,3,1,0,2,0,1]
a2 = [3,2,0,0,2,0,1]
print(arrays_game(a1))
print(arrays_game(a2))
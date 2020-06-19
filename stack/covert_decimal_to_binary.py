from stack import Stack

def divide_by_2(num):
	stack = Stack()

	while num > 0:
		stack.push(num%2)
		num = num // 2 
	
	ans = ''

	while not stack.is_empty():
		ans += str(stack.pop())
	
	return ans 

if __name__ = "__main__":
	print(divide_by_2(242))

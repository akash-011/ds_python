"""
Given an array of numbers consisting of daily stock prices, 
calculate the maximum amount of profit that can be made from buying on one day and selling on another day.
"""
#time complexity - O(n^2)
#space complexity - O(1)
def brute_force(arr):
    max_profit = 0

    for i in range(len(arr) - 1):
        for j in range(i+1 , len(arr)):
            if arr[j] - arr[i] > max_profit:
                max_profit = arr[j] - arr[i]
    
    return max_profit

#time cmplexity - O(n)
#space complexity - O(1)
def buy_and_sell_stock(arr):
    min_value = arr[0]
    max_profit = 0 

    for i in arr:
        min_value = min(min_value, i)
        compare_profit = i - min_value
        max_profit = max(compare_profit, max_profit) 
    
    return max_profit

if __name__ == "__main__":
    arr = [310, 315, 275, 260, 280, 290, 265]
    print(buy_and_sell_stock(arr))
    
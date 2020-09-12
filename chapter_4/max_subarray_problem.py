"""
Find the maximum difference in subarrays ie: Buy and sell stocks with one transaction find the maximum profit

"""
from timeit import timeit

def max_profit_BF(array):
	n = len(array)
	max_profit = 0
	for i in range(n):
		for j in range(i, n):
			profit = array[j] - array[i]
			if profit > max_profit:
				max_profit = profit
	return max_profit


"""
what if we divide these to continuous chunks such that max subarray lies on
1. left side
2. right side
3. crossing midpoint
"""


def max_crossing_subarray(A, low, mid, high):
	left_sum = float("-inf")
	sum = 0
	for i in range(mid, low-1, -1):
		sum = sum + A[i]
		if sum > left_sum:
			left_sum = sum
			max_left = i
	right_sum = float("-inf")
	sum = 0
	for j in range(mid+1, high+1):
		sum = sum + A[j]
		if sum > right_sum:
			right_sum = sum
			max_right = j
	return max_left, max_right, left_sum + right_sum


def max_subarray(A, low, high):
	if low == high:
		return low, high, A[low]
	else:
		mid = (low + high ) // 2
		left_low, left_high, max_left_sum = max_subarray(A, low, mid)
		right_low, right_high, max_right_sum = max_subarray(A, mid+1, high)

		cross_low, cross_high , max_cross_sum = max_crossing_subarray(A, low, mid, high)
		if max_left_sum >= max_right_sum and max_left_sum >= max_cross_sum:
			return left_low, left_high, max_left_sum
		elif max_right_sum >= max_left_sum and max_right_sum >= max_cross_sum:
			return right_low, right_high, max_right_sum
		else:
			return cross_low, cross_high , max_cross_sum

def max_profit(A):
	diff_array = [A[i] - A[i-1] for i in range(1, len(A))]
	low_index, high_index, max_sum = max_subarray(diff_array, 0, len(diff_array)-1)
	return max_sum




def max_subarray_optimized(nums):
	curr_max = float("-inf")
	best_max = float("-inf")

	for num in nums:
		curr_max = max(num, curr_max + num)
		best_max = max(curr_max, best_max)
	return best_max


def max_profit_optimized(A):
	diff_array = [A[i] - A[i-1] for i in range(1, len(A))]
	return max_subarray_optimized(diff_array)


def max_subarray_optimized_2(nums):
	curr_sum = 0 
	max_sum = None
	n = len(nums)
	if n == 0:
		return max_sum
	elif n == 1:
		return nums[0]
	
	for i in range(n):
		curr_sum += nums[i]
		if curr_sum > max_sum:
			max_sum = curr_sum
		if curr_sum < 0:
			curr_sum = 0
	return max_sum




def max_profit_optimized_2(A):
	diff_array = [A[i] - A[i-1] for i in range(1, len(A))]
	return max_subarray_optimized_2(diff_array)




"""
Suppose we change the definition of the maximum-subarray problem to allow the result to be an empty subarray, where the sum of the values of an empty subarray is 0. How would you change any of the algorithms that do not allow empty subarrays to permit an empty subarray to be the result?
"""

def max_crossing_subarray_4_1_4(A, low, mid, high):
	left_sum = 0
	sum = 0
	max_left, max_right = high, low
	for i in range(mid, low-1, -1):
		sum = sum + A[i]
		if sum > left_sum:
			left_sum = sum
			max_left = i
	right_sum = 0
	sum = 0
	for j in range(mid+1, high+1):
		sum = sum + A[j]
		if sum > right_sum:
			right_sum = sum
			max_right = j
	return max_left, max_right, left_sum + right_sum


def max_subarray_4_1_4(A, low, high):
	if low == high:
		return low, high, A[low]
	else:
		mid = (low + high ) // 2
		left_low, left_high, max_left_sum = max_subarray_4_1_4(A, low, mid)
		right_low, right_high, max_right_sum = max_subarray_4_1_4(A, mid+1, high)

		cross_low, cross_high , max_cross_sum = max_crossing_subarray_4_1_4(A, low, mid, high)
		if max_left_sum >= max_right_sum and max_left_sum >= max_cross_sum:
			return left_low, left_high, max_left_sum
		elif max_right_sum >= max_left_sum and max_right_sum >= max_cross_sum:
			return right_low, right_high, max_right_sum
		else:
			return cross_low, cross_high , max_cross_sum


def max_profit_4_1_4(A):
	diff_array = [A[i] - A[i-1] for i in range(1, len(A))]
	low_index, high_index, max_sum = max_subarray_4_1_4(diff_array, 0, len(diff_array)-1)
	return max_sum






# print max_profit_BF([10, 11, 7, 10, 6]),
# print max_profit([10, 11, 7, 10, 6]),
# print max_profit_optimized([10, 11, 7, 10, 6]),
# print max_profit_optimized_2([10, 11, 7, 10, 6])

prices = [100,113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
print max_profit_BF(prices),
print max_profit(prices),
print max_profit_optimized(prices),
print max_profit_optimized_2(prices),
print max_profit_4_1_4(prices)







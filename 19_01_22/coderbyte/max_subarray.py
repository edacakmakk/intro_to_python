"""
Max Subarray
HIDE QUESTION
Have the function MaxSubarray(arr) take the array of numbers stored in arr and 
determine the largest sum that can be formed by any contiguous subarray in the array. 
For example, if arr is [-2, 5, -1, 7, -3] then your program should return 11 
because the sum is formed by the subarray [5, -1, 7]. 
Adding any element before or after this subarray would make the sum smaller.
"""
def MaxSubarray(arr):
  max_sum = arr[0]
  current_sum = 0
  
  for i in range(len(arr)):
    current_sum =  current_sum + arr[i]
    if current_sum < 0:
      current_sum = 0
    elif max_sum < current_sum:
      max_sum = current_sum
  
  return max_sum


print(MaxSubarray(input()))
"""
Have the function HistogramArea(arr) read the array of non-negative integers stored in arr 
which will represent the heights of bars on a graph (where each bar width is 1), 
and determine the largest area underneath the entire bar graph. 
For example: if arr is [2, 1, 3, 4, 1] then this looks like the following bar graph:

             __
          __|  |
    __   |x |x |   
   |  |__|x |x |__
   |  |  |x |x |  |

You can see in the above bar graph that the largest area underneath the graph is 
covered by the x's. The area of that space is equal to 6 because 
the entire width is 2 and the maximum height is 3, therefore 2 * 3 = 6. 
Your program should return 6. The array will always contain at least 1 element.
"""

def max_area_histogram(arr):
    max_area = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            min_height = min(arr[i], arr[j])
            for k in range(i, j):
                min_height = min(min_height, arr[k])

            max_area = max(max_area, min_height * ((j - i) + 1))
    return max_area


print(max_area_histogram(input()))
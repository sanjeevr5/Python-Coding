from typing import Iterable

def merge_sort(array : Iterable) -> None:
    """
    Purpose: Merge sort algorithm
    Time complexity : O(n logn (n))
    Algorithm type : Divide & Conquer
    Approach : Recursive
    Idea inspired by : https://www.educative.io/edpresso/merge-sort-in-python
    """
    # If the length of array is greater than 1 then find the mid index of the array
    if len(array) > 1:

        mid_point = len(array) // 2 #Floor division

        # Splitting the array into left and right half
        left_array = array[:mid_point] # < mid index becomes the left array
        right_array = array[mid_point:] # >= mid index becomes the right array

        #Recursive calls until the left and right array becomes of length 1 {for the first iteration}
        merge_sort(left_array)
        merge_sort(right_array)

        #When it reaches the length of 1 {for the first iteration}
        left_iterator = right_iterator = array_iterator = 0
        while left_iterator < len(left_array) and right_iterator < len(right_array):
            if left_array[left_iterator] < right_array[right_iterator]:
                #add to the original array
                array[array_iterator] = left_array[left_iterator]
                left_iterator += 1
            else:
                array[array_iterator] = right_array[right_iterator]
                right_iterator += 1
            array_iterator += 1
        
        #Now, add the remaining elements to the array
        # WKT, the elements on the left are smaller and elements on the right are greater
        while left_iterator < len(left_array):
            array[array_iterator] = left_array[left_iterator]
            array_iterator += 1
            left_iterator += 1
        
        while right_iterator < len(right_array):
            array[array_iterator] = right_array[right_iterator]
            array_iterator += 1
            right_iterator += 1

if __name__ == '__main__':
    array = [54,26,93,17,77,31,44,55,20]
    merge_sort(array)
    print(array)

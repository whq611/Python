"""
Given an array of integers and an integer k, find the kth largest element in the array

https://stackoverflow.com/questions/251781/how-to-find-the-kth-largest-element-in-an-unsorted-array-of-length-n-in-on
"""

def partition(arr,low,high):
    """
    Partitions list based on the pivot element
    Args:
        arr: The list to be partitioned
        low: The lower index of the list
        high: The higher index of the list
    Returns:
        int: The index of pivot element after partitioning

        Examples:
        >>> partition([3,1,4,5,9,2,6,5,3,5],0,9)
        4
        >>> partition([7,1,4,5,9,2,6,5,8],0,8)
        1
    """
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]>= pivot:
            i+=1
            arr[i], arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def kth_largest_element(arr,k):
    """
    Finds the kth largest element in a list.

    Args:
        nums : The list of numbers.
        k : The position of the desired kth largest element.

    Returns:
        int: The kth largest element.

    Examples:
        >>> kth_largest_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3)
        5
        >>> kth_largest_element([2, 5, 6, 1, 9, 3, 8, 4, 7, 3, 5], 1)
        9
        >>> kth_largest_element([9, 1, 3, 6, 7, 9, 8, 4, 2, 4, 9], 11)
        1
        >>> kth_largest_element([1, 2, 4, 3, 5, 9, 7, 6, 5, 9, 3], 0)
        'Invalid value of k'
    """
    if not 1 <= k <= len(arr):
        return "Invalid value of k"
    low,high=0,len(arr)-1
    while low<=high:
        if low>len(arr)-1 or high<0:
            return "Invalid value of k"
        pivot_index=partition(arr,low,high)
        if pivot_index==k-1:
            return arr[pivot_index]
        elif pivot_index>k-1:
            high=pivot_index-1
        else:
            low=pivot_index+1
    return "Kth largest element not found"
if __name__=="__main__":
    import doctest
    doctest.testmod()
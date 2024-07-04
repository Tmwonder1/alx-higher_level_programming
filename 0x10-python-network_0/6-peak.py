#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers, lo=0, hi=None):
    """Finds a peak in list_of_integers using modified binary search"""
    if list_of_integers is None or not list_of_integers:
        return None
    
    if hi is None:
        hi = len(list_of_integers) - 1

    if lo == hi:
        return list_of_integers[lo]

    mid = (hi + lo) // 2

    if list_of_integers[mid] >= list_of_integers[mid + 1]:
        return find_peak(list_of_integers, lo, mid)
    else:
        return find_peak(list_of_integers, mid + 1, hi)

# Example usage
# print(find_peak([1, 3, 4, 3, 1]))

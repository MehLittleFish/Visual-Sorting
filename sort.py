#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(array):
    for i in range(1, len(array)):

        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


#array = [5, 9, 7, 1, 2, 3, 15, 20, 12]
#quick_sort(array, 0, len(array)-1)
#print(array)


def heap_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        canvas.after(15, update_bar(arr[i].id, arr[0].id))
        canvas.update()
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arr[i].height < arr[l].height:
        largest = l
    if r < n and arr[largest].height < arr[r].height:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        canvas.after(15, update_bar(arr[i].id, arr[largest].id))
        canvas.update()
        heapify(arr, n, largest)
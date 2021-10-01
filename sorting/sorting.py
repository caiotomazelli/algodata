from random import randint

class Sorting:
    """Groups different sorting algorithms."""
    @classmethod
    def qsort(cls, arr, beggining=0, pivot=None):
        """Quick sort implementation."""
        start = beggining
        if pivot is None:
            pivot = len(arr) - 1
        arr_lenght = pivot - start + 1

        if arr_lenght < 2:
            return arr
        elif arr_lenght == 2:
            if arr[start] > arr[pivot]:
                arr[start], arr[pivot] = arr[pivot], arr[start]
            return arr
        
        # From here on, arr_lenght > 2
        
        end = pivot - 1
        # swap pivot with a random entry to mitigate worst case performance
        rand_idx = randint(beggining, pivot - 1)
        arr[rand_idx], arr[pivot] = arr[pivot], arr[rand_idx]

        while start <= end:
            if arr[end] <= arr[pivot] and arr[start] > arr[pivot]:
                arr[start], arr[end] = arr[end], arr[start]
                end -= 1
            elif arr[end] <= arr[pivot] and arr[start] <= arr[pivot]:
                start += 1
            elif arr[end] > arr[pivot]:
                end -= 1
            else: # arr[end] < arr[pivot] and arr[start] == arr[pivot]
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
        if start != pivot:
            arr[start], arr[pivot] = arr[pivot], arr[start]
        Sorting.qsort(arr, beggining, start-1)
        Sorting.qsort(arr, start+1, pivot) 
        return arr


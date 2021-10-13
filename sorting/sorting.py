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


    @classmethod
    def msort(cls, arr):
        """Merge sort implementation."""
        if len(arr) < 2:
            return arr
        med = len(arr) // 2
        m1 = Sorting.msort(arr[0:med])
        m2 = Sorting.msort(arr[med:])
        idx1 = 0; idx2 = 0; ans = []
        while len(ans) < len(arr):
            if idx1 < len(m1) and idx2 < len(m2):
                if m1[idx1] < m2[idx2]:
                    ans.append(m1[idx1])
                    idx1 += 1
                else:
                    ans.append(m2[idx2])
                    idx2 += 1
            elif idx1 < len(m1):
                ans.append(m1[idx1])
                idx1 += 1
            else:
                ans.append(m2[idx2])
                idx2 += 1
        return ans


    @classmethod
    def ssort(cls, arr):
        """Selection sort implementation."""
        if len(arr) < 2:
            return arr
        
        curr = 0; target = len(arr) - 1
        while target > 0:
            while curr < target:
                if arr[curr] > arr[target]:
                    arr[curr], arr[target] = arr[target], arr[curr]
                curr += 1
            target -= 1
            curr = 0
        return arr

    @classmethod
    def isort(cls, arr):
        """Insertion sort implementation."""
        if len(arr) < 2:
            return arr
        i = 0; j = 1
        while j < len(arr):
            while arr[j] > arr[i]:
                i += 1; j += 1; break
            while arr[j] < arr[i] and i >= 0:
                i -= 1
            last_ord = j
            while j - i > 1:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            i = last_ord
            j = i + 1
        return arr


    @classmethod
    def slow_isort(cls, arr):
        """Attempted implementation of insertio sort, turned out to be very slow."""
        if len(arr) < 2:
            return arr
        
        i = 0; j = 1
        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                j = i if i > 0 else 1
                i = 0
            elif j - i == 1:
                i += 1
                j += 1
            else:
                i += 1
        return arr
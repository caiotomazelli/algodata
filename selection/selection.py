class Selection:
    """Groups different selection algorithms."""

    @classmethod
    def quickselect(cls, arr, k) -> int:
        def inc_start(target):
            if cls.start < target:
                cls.start += 1

        def dec_end(target):
            if cls.end > target:
                cls.end -= 1 

        if k > len(arr) or k < 1:
            return None
        target = k - 1
        cls.start = 0
        cls.end = len(arr) - 1
        while cls.start < cls.end:
            if arr[cls.start]<=arr[target] and arr[cls.end]>=arr[target]:
                inc_start(target)
                dec_end(target)
            elif arr[cls.start] > arr[target] and arr[cls.end] >= arr[target]:
                arr[cls.start], arr[target] = arr[target], arr[cls.start]
                inc_start(target)
            elif arr[cls.start] <= arr[target] and arr[cls.end] < arr[target]:
                arr[cls.end], arr[target] = arr[target], arr[cls.end]
                dec_end(target)
            else:
                arr[cls.start], arr[cls.end] = arr[cls.end], arr[cls.start]
                inc_start(target)
                dec_end(target)
        return arr[target]

def find_max(arr):
    if len(arr) == 0:
        return None 
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2 
    left_half = arr[:mid]
    right_half = arr[mid:]
    max_left = find_max(left_half)
    max_right = find_max(right_half)
    if max_left > max_right:
        return max_left
    else:
        return max_right
numbers = [3, 7, 1, 9, 4, 2]
print(find_max(numbers))
print(find_max([5]))
print(find_max([8, 3]))
print(find_max([1, 2, 3]))
print(find_max([10, 5, 8, 12]))
print(find_max([]))

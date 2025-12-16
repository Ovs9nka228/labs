def binary_search(arr, target):
    def search_helper(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return search_helper(left, mid - 1)
        else:
            return search_helper(mid + 1, right)
    return search_helper(0, len(arr) - 1)
my_list = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(my_list, 40))
print(binary_search(my_list, 20))
print(binary_search(my_list, 70))
print(binary_search(my_list, 10))
print(binary_search(my_list, 99))

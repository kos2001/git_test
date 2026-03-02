"""다양한 정렬 알고리즘 구현"""


def bubble_sort(arr):
    """버블 정렬: O(n^2)"""
    n = len(arr)
    result = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(arr):
    """선택 정렬: O(n^2)"""
    n = len(arr)
    result = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


def insertion_sort(arr):
    """삽입 정렬: O(n^2)"""
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def quick_sort(arr):
    """퀵 정렬: O(n log n) 평균"""
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """병합 정렬: O(n log n)"""
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """두 정렬된 배열을 병합"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"원본 데이터: {test_data}")
    print(f"버블 정렬:   {bubble_sort(test_data)}")
    print(f"선택 정렬:   {selection_sort(test_data)}")
    print(f"삽입 정렬:   {insertion_sort(test_data)}")
    print(f"퀵 정렬:     {quick_sort(test_data)}")
    print(f"병합 정렬:   {merge_sort(test_data)}")

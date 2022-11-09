def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)-2):
        min: int = i
        for j in range(i+1, len(arr)):
            if (arr[min] > arr[j]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr


# def selection_sort(arr):
#     n = len(arr)
#     # perulangan list elemen
#     for i in range(n):
#         # cari nilai elemen terendah
#         # yang masih tersedia
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j

#         # tukar dengan nilai elemen ke-i
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr


arr = [100, 343, 342, 754, 875, 564, 643]

print(selection_sort(arr))


def insertion_sort(arr: list[int]):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(insertion_sort(arr))

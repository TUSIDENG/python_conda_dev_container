arr: list[int] = [0] * 5  # [ 0, 0, 0, 0, 0 ]
arr[2] = 10
print(arr)  # [ 0, 0, 10, 0, 0 ]

arr.extend([1, 2, 3])
print(arr)  # [ 0, 0, 10, 0, 0, 1, 2, 3 ]

arr.append(8)
print(arr)  # [ 0, 0, 10, 0, 0, 1, 2, 3, 8 ]

arr.insert(1, 9)
print(arr)  # [ 0, 9, 0, 10, 0, 0, 1, 2, 3, 8 ]

arr.pop(3)
print(arr)  # [ 0, 9, 0, 0, 0, 1, 2, 3, 8 ]

arr.sort()
print(arr)  # [0, 0, 0, 0, 1, 2, 3, 8, 9]

arr2 = [[5]] * 5
arr2[0][0] = 10
print(arr2)  # [[10], [10], [10], [10], [10]]

arr3 = [[5] for _ in range(5)]
arr3[0][0] = 10
print(arr3)  # [[10], [5], [5], [5], [5]]
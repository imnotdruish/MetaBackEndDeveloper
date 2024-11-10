# O(1) - Contant Time
def accessElement(arr, index):
  return arr[index]

# O(n) - Linear Time
def linearSearch(arr, target):
  for item in arr:
    if item == target:
      return True
    return False
  
# O(n^2) - Quadratic Time
def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1] :
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

# O(log n) - Logarithmic Time
def binarySearch(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1
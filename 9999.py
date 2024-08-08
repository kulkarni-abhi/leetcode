"""
Find Minimum number of swap operations required to sort an array in an increasing order

"""

def min_sort_required(arr):
  min = arr[0]
  max = arr[0]
  hashmap = dict()

  # Find min,max and create index-value map
  for i in range(len(arr)):
    if arr[i] > max:
      max = arr[i]
    if arr[i] < min:
      min = arr[i]
    hashmap[arr[i]] = i

  # Generate sorted hashmap
  count = 0
  sorted_map = list()
  for i in range(min, max+1):
    if i in hashmap:
      sorted_map.append([i, hashmap[i], False])
      count += 1

  swaps = 0
  for i in range(len(arr)):
    # ignore visited node or if index is unchanged.
    if sorted_map[i][2] or sorted_map[i][1] == i:
      continue

    moves = 0
    j = i
    # repeat until node is visited
    while not sorted_map[j][2]:
      # mark node visited.
      sorted_map[j][2] = True

      # goto next node in arr
      j = sorted_map[j][1]
      moves += 1

    if moves > 0:
      # if n-1 values are swapped/sorted,
      # nth value will be auto-sorted
      swaps += moves - 1

  return swaps
print(min_sort_required([2, 1, 4, 3]))
print(min_sort_required([2, 1, 3, 4]))

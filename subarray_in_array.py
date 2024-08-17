# Starting index for every occurrence of given array B in array A
# A = [0,1,2,3,4,5,6,7,8,9,3,4,5,6,7,8]
# B = [3,4,5,6]
#
# Array B appears in Array A at starting indices 3 and 11


def find_subarray(A, B):
  result = list()
  start = None
  j = 0

  for i in range(len(A)):
    if A[i] == B[j]:
      if j < len(B) - 1:
        if j == 0:
          start = i
        j += 1
      else:
        result.append(start)
        j = 0
    else:
      j = 0
  return result

class Solution(object):
  def divide_simple(self, dividend, divisor):
    i = 0
    if dividend > 0 and divisor > 0:
      base = 0
      while True:
        base += divisor
        if base > dividend:
          break
        i += 1
    elif dividend > 0 and divisor < 0:
      base = 0
      while True:
        base -= divisor
        if base > dividend:
          break
        i -= 1
    elif dividend < 0 and divisor > 0:
      base = 0
      while True:
        base -= divisor
        if base < dividend:
          break
        i -= 1
    elif dividend < 0 and divisor < 0:
      base = 0
      while True:
        base += divisor
        if base < dividend:
          break
        i += 1
    return i

  def divide_complex(self, dividend, divisor):
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
          sign = -1
        else:
          sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)
        return result

  def divide(self,dividend, divisor):
    i = 0
    if dividend < 0:
      method = "subtract"
      if divisor < 0:
        method = "add"

      base = 0
      while True:
        base = getattr(self, method)(base, divisor)
        if base < dividend:
          break
        i = getattr(self, method)(i, 1)
    elif dividend > 0:
      base = 0
      method = "subtract"
      if divisor > 0:
        method = "add"
      while True:
        base = getattr(self, method)(base, divisor)
        if base > dividend:
          break
        i = getattr(self, method)(i, 1)
    return i

  def add(self, a, b):
    return a + b

  def subtract(self, a, b):
    return a - b

solution = Solution()
print(solution.divide_simple(-7, 2))
print(solution.divide_complex(-7, 2))
print(solution.divide(-7, 2))
print(solution.divide_simple(7, -2))
print(solution.divide_complex(7, -2))
print(solution.divide(7, -2))
print(solution.divide_simple(-7, -2))
print(solution.divide_complex(-7, -2))
print(solution.divide(-7, -2))
print(solution.divide_simple(7, 2))
print(solution.divide_complex(7, 2))
print(solution.divide(7, 2))

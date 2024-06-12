class Solution:
    def trap(self, height: List[int]) -> int:
        # Faster
        i = 0
        left_max = height[0]
        sum = 0
        j = len(height) - 1
        right_max = height[j]
        while i < j:
            if left_max <= right_max:
                sum += left_max - height[i]
                i += 1
                left_max = max(left_max, height[i])
            else:
                sum += right_max - height[j]
                j -= 1
                right_max = max(right_max, height[j])
        return sum

    def trap1(self, height: List[int]) -> int:
        total_trapped = 0

        for index in range(1, len(height) - 1):
            left_max = max(height[:index])
            right_max = max(height[index:])

            if left_max < 0 or right_max < 0:
                continue

            ht = height[index]
            water_level = min(left_max, right_max) - ht
            if water_level < 0:
                continue

            total_trapped += water_level
        return total_trapped

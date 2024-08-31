from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or out of bounds
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                if prev_empty and next_empty:
                    # Plant a flower here
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True

        return count >= n

# Example usage:
solution = Solution()

# Example 1
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(solution.canPlaceFlowers(flowerbed1, n1))  # Output: True

# Example 2
flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(solution.canPlaceFlowers(flowerbed2, n2))  # Output: False

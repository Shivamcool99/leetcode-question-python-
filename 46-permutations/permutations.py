class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current):
    
            # Base case: if the current permutation is complete
            if len(current) == len(nums):
                result.append(current[:])  # Make a copy of current and add to results
                return
            
            # Recursive case: try adding each number that hasn't been used yet
            for num in nums:
                if num not in current:
                    current.append(num)  # Add num to current permutation
                    backtrack(current)  # Recursively permute the remaining nums
                    current.pop()       # Backtrack: remove num for the next iteration
        
        result = []
        backtrack([])
        return result

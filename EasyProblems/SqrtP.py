class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x 
        result = 0 
        while left <= right:
            mid = (left + right) // 2 
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1 
                result = mid 
            else: 
                right = mid - 1 
                
        return result

solution = Solution()
x = 24
print(solution.mySqrt(x))
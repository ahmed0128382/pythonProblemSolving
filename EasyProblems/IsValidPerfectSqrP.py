class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r =0, num 
        mid = 0
        result = 0
        while l < r :
            mid = (l + r) // 2 
            print (f"mid in loop : {mid}")
            if ( mid * mid == num ) :
                print (f"l and r in loop : {l} and {r}")
                return True
            elif (mid * mid > num) :
                print (f"r in loop :{r}")
                r = mid - 1
                print (f"r in loop :{r}")
            else :
                print (f"l in loop: {l}")
                l = mid + 1
                result = l
                print (f"l in loop :{l}")
        if (result * result == num) :
            print (f"l and r out loop : {l} and {r}")
            return True
        else :
            return False 

solution = Solution()
x = 16
print(solution.isPerfectSquare(x))
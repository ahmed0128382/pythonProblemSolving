from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        end = len(digits)
        if (digits[end-1] != 9 ):
            digits[end -1]+=1
            return digits
        while (digits[end - 1] == 9):
            digits[end - 1] =  0 
            end -= 1
        dig=[1]
        if(end <= 0): dig.extend(digits)
        else:
             digits[end -1]+=1
             dig = digits
        return dig


solution = Solution()
DigitsEx = [9,9,9]
print(solution.plusOne(DigitsEx))
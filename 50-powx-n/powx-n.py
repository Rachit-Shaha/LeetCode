class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1.0
        copy = n 
        if copy < 0:
            copy = copy * -1
        while copy:
            if copy % 2:
                result = result * x
                copy = copy - 1
            else:
                x = x * x
                copy = copy // 2
        if n < 0:
            result = 1.0/result
        return result
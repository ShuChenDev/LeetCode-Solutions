"""
9/19/2024
Set
"""

class Solution(object):
    def isHappy(self, n):
        setList = set()
        
        sum = 0
        while True:
            while n > 0:
                sum += (n % 10) * (n % 10)
                n = n // 10

            if sum in setList:
                return False
            elif sum == 1:
                return True
            
            setList.add(sum)
            n = sum
            sum = 0

        return False

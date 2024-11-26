# https://leetcode.com/problems/climbing-stairs/description/

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

"""
This is a special case of fib seq where n starts from 1

when n=1, then we have 1 ways to climb
when n=2, then we have 2 ways to climb ((1), (2))
when n=3, then we have 3 ways to climb ((1,1,1), (1,2), (2,1))
when n=4, the way we can reach to 4th step is from n=3 or n=2 because
 we can take only 1 or 2 steps at a  time, 
 from n=2, there are 2 ways
 from n=3, there are 1 ways
 so total we have 5 ways
when n=5, we can reach n=3 in 3 ways and n=4 in 5 ways so we can reach n=5 in 8 ways
"""

# solution-1 (recursion)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        
# solution-2 (memoization)
class Solution:
    def climbStairs(self, n: int) -> int:
        mem_dict = {1:1, 2:2}

        def f(x):
            if x in mem_dict:
                return mem_dict[x]
            else:
                mem_dict[x] = f(x-1) + f(x-2)
                return mem_dict[x]
        return f(n)
    
# solution-3 (tabulation)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 :
            return 1
        if n==2:
            return 2
        arr = [0] * (n+1)
        arr[1] = 1
        arr[2] = 2

        for i in range(3, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]
    
# solution-3 (tabulation - memoization)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 :
            return 1
        if n == 2 :
            return 2
        
        curr = 2
        prev = 1
        for i in range(3, n+1):
            temp = curr
            curr = curr + prev
            prev = temp
        return curr

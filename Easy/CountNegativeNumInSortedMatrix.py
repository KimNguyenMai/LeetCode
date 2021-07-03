#1351. 

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for r in row:
                if r < 0:
                    count += 1
                    
        return count
                    
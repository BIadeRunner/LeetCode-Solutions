class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * k for k in range(1, 102)]
        tower[0][0] = poured
        for r in range(100):
            for c in range(r + 1):
                if tower[r][c] > 1:
                    excess = (tower[r][c] - 1) / 2.0
                    tower[r][c] = 1
                    tower[r+1][c] += excess
                    tower[r+1][c+1] += excess
        return min(1, tower[query_row][query_glass])
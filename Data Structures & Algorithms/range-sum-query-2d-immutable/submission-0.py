class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.prefixSums = [[0] * self.COLS for _ in range(self.ROWS)]

        for r in range(self.ROWS):
            rowSum = 0
            for c in range(self.COLS):
                rowSum += matrix[r][c]
                aboveSum = self.prefixSums[r-1][c] if r > 0 else 0
                self.prefixSums[r][c] = rowSum + aboveSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        wholeRegionSum = self.prefixSums[row2][col2]
        rowSumToSubtract = self.prefixSums[row1-1][col2] if row1 > 0 else 0
        colSumToSubtract = self.prefixSums[row2][col1-1] if col1 > 0 else 0
        regionToReAdd = self.prefixSums[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return wholeRegionSum - rowSumToSubtract - colSumToSubtract + regionToReAdd
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
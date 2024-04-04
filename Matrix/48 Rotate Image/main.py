class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r-l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l+i]
                
                # move bottomLeft to topLeft
                matrix[top][l+i] = matrix[bottom-i][l]

                # move bottomRight into bottomLeft
                matrix[bottom-i][l] = matrix[bottom][r-i]

                # move topRight to bottomRight
                matrix[bottom][r-i] = matrix[top+i][r]

                # move topLeft into topRight
                matrix[top+i][r] = topLeft
            
            r -= 1
            l += 1

        
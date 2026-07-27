class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        newArray = [row[0] for row in matrix]

        if target in newArray:
            return True
        else:
            newArray.append(target)

            newArray = sorted(newArray)

            i = newArray.index(target) - 1

            if 0<=i<len(matrix):
                for num in matrix[i]:
                    if num == target:
                        return True

        return False
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    #print(matrix)

def reverse(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
    #print(matrix)

def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    transpose(matrix)
    reverse(matrix)
    return matrix

m=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
m1 = [[1,2],[3,4]]
print(rotate(m))
print(rotate(m1))

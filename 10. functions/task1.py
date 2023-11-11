def matrix(n=1, m=None, value=0):
    if m == None:
        m = n
    matrix = [[value] * m for _ in range(n)]
    return matrix

col, row =map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

    
for i in range(col):
    for j in range(row):
        if matrix[i][j]=='.':
            matrix[i][j] = 0

for i in range(col):
    for j in range(row):
        if matrix[i][j] == 0:
            
            if i>0 and i<col-1 and j>0 and j<row-1:
                for k in range(i-1, i+2):
                    for kk in range(j-1, j+2):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1



            elif i==0 and j==0:
                for k in range(i, i+2):
                    for kk in range(j, j+2):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1

            elif i==0 and j==col-1:
                for k in range(i, i+2):
                    for kk in range(j-1, j+1):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1

            elif i==0 and j!=0 and j!=col-1:
                for k in range(i, i+2):
                    for kk in range(j-1, j+2):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1



            elif i==row-1 and j==0:
                for k in range(i-1, i+1):
                    for kk in range(j, j+2):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1

            elif i==row-1 and j==col-1:
                for k in range(i-1, i+1):
                    for kk in range(j-1, j+1):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1

            elif i==row-1 and j!=0 and j!=col-1:
                for k in range(i-1, i+1):
                    for kk in range(j-1, j+2):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1

            elif i==row-1 and j==0:
                for k in range(i-1, i+1):
                    for kk in range(j, j+2):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1



            elif j==0 and i!=0 and i!=row-1:
                for k in range(i-1, i+2):
                    for kk in range(j, j+2):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1

            elif j==col-1 and i!=0 and i!=row-1:
                for k in range(i-1, i+2):
                    for kk in range(j-1, j+1):
                        if matrix[k][kk]=='*':
                            matrix[i][j]+=1

for i in range(col):
    for j in range(row):
        print(matrix[i][j],end='')
    print()    

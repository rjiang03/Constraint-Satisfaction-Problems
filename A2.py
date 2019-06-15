#define a point class here
#the point class will record its position, value and any possible choice in the next step
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.available = []
        self.value = 0


#check what number has been used in the same row
def row(p, SUDOKU):
    row = set(SUDOKU[p.x])#collect same number for once
    row.remove(0)#delete 0 from the set
    return row

#check what number has been used in the same col
def col(p, SUDOKU):
    l = []#creat a list to record number current
    for i in range(9):
        l.append(SUDOKU[i][p.y])
    col = set(l)#collect same number for once
    col.remove(0)#delete 0 from the set
    return col

#check what number has been used in the same block
def block(p, SUDOKU):
    l = []
    x_s = p.x // 3#calculate the begin x for current block
    y_s = p.y // 3#calculate the begin y for current block
    for i in range(x_s*3, x_s*3 + 3):
        for j in range(y_s*3, y_s*3 + 3):
            # search in each block
            l.append(SUDOKU[i][j])
    block = set(l)#collect same number for once
    block.remove(0)#delete 0 from the set
    return block


#use recursive function to realize Forward checking
def recursive_fun(p, points, SUDOKU):
    for m in p.available:
        p.value = m

        # check if the point can satisfy the SUDOKU
        if p.value not in row(p, SUDOKU) and p.value not in col(p, SUDOKU) and p.value not in block(p, SUDOKU):

            #assume this position is a certain number
            SUDOKU[p.x][p.y] = p.value

            #if there is no point in the points list, return the solution, and print the SUDOKU
            if len(points) == 0:
                for i in range(9):
                    for j in range(9):
                        print(SUDOKU[i][j], end=' ')
                    print('')
                break

            #if it is not end, doing recursive
            else:
                p2 = points.pop()
                recursive_fun(p2, points, SUDOKU)
                #if the function did not find the answer in this branch
                #it will come back to the most recent situation
                SUDOKU[p.x][p.y] = 0
                SUDOKU[p2.x][p2.y] = 0
                p2.value = 0
                #because did not find the solution, add the point back to the points list
                points.append(p2)


#initialize all the point we need to solve
def solution(SUDOKU):
    #create a list to store all the points
    points = []
    for i in range(9):
        for j in range(9):

            # if this position is 0, record it as a point, and put it into the points
            if SUDOKU[i][j] == 0:
                p = point(i, j)
                for k in range(1, 10):

                    # check if k can be used, if it can be used, store it
                    if k not in row(p, SUDOKU) and k not in col(p, SUDOKU) and k not in block(p, SUDOKU):
                        p.available.append(k)
                points.append(p)
    p = points.pop()
    recursive_fun(p, points, SUDOKU)
    return points




'''
The sudo ku must be a list which has 9 rows and 9 cols
'''

sudoku = [
        [0, 7, 0, 0, 4, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 6, 1, 0],
        [3, 9, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 4, 0, 0, 9],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
        [5, 0, 0, 1, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 7, 6],
        [0, 5, 4, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 1, 0, 0, 5, 0]
]

solution(sudoku)

print('\n')


sudoku2 = [
        [6, 0, 8, 7, 0, 2, 1, 0, 0],
        [4, 0, 0, 0, 1, 0, 0, 0, 2],
        [0, 2, 5, 4, 0, 0, 0, 0, 0],
        [7, 0, 1, 0, 8, 0, 4, 0, 5],
        [0, 8, 0, 0, 0, 0, 0, 7, 0],
        [5, 0, 9, 0, 6, 0, 3, 0, 1],
        [0, 0, 0, 0, 0, 6, 7, 5, 0],
        [2, 0, 0, 0, 9, 0, 0, 0, 8],
        [0, 0, 6, 8, 0, 5, 2, 0, 3]
]
solution(sudoku2)

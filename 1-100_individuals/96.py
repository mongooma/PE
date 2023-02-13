# leetcode 37


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.

        backtracking;

        monitor the sets of row, col and 3*3 boxes, 
        row, col indexed by i, j
        box indexed by the left corner (i, j)

        for each node at (i1, j1)
        assign it to the above sets by
        i1 -> row i1
        j1 -> row j1
        i1, j1 -> box i1 // 3, j1 // 3

        optimize:
        at each try, select the set with the largest size < 9 to fill

        """
        rows = [set([int(n) for n in board[i] if n != '0']) for i in range(len(board))]
        cols = [set([int(r[j]) for r in board if r[j] != '0']) for j in range(len(board))]
        boxes = dict([((i, j), set()) for i in range(3) for j in range(3)])
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '0':
                    boxes[(i//3, j//3)].add(int(board[i][j]))

        def check_valid(i_0, j_0, n_0):
            # print("check", i_0, j_0, "for", n_0)
            if n_0 in rows[i_0] or \
               n_0 in cols[j_0] or \
               n_0 in boxes[(i_0//3, j_0//3)]: # conflict
                # print("not valid")
                return False

            # print("valid")
            return True
        
        def fill(i_0, j_0, n_0):
            # print("fill board", i_0, j_0, n_0)
            board[i_0][j_0] = str(n_0)
            rows[i_0].add(n_0)
            cols[j_0].add(n_0)
            boxes[(i_0//3, j_0//3)].add(n_0)
            return

        def erase(i_0, j_0, n_0):
            # print("erase board", i_0, j_0, n_0)
            board[i_0][j_0] = '0'
            rows[i_0].remove(n_0)
            cols[j_0].remove(n_0)
            boxes[(i_0//3, j_0//3)].remove(n_0)
            return

        def choose_next_fill():
            # optimization step
            # choose the next cell to fill
            fillcnt_max = 0
            max_s = (0, 0, 0)
            for i, r in enumerate(rows):
                if 9 > len(r) > fillcnt_max:
                    fillcnt_max = len(r)
                    max_s = ('row', i)

            for j, col in enumerate(cols):
                if 9 > len(col) > fillcnt_max:
                    fillcnt_max = len(col)
                    max_s = ('col', j)

            for (i, j), box in boxes.items():
                if 9 > len(box) > fillcnt_max:
                    fillcnt_max = len(box)
                    max_s = ('box', i, j)

            #
            if max_s[0] == 'row':
                i = max_s[-1]
                j = 0
                while j < len(board):
                    if board[i][j] == '0':
                        break
                    j += 1
                unfilled = list(set(range(1, 10)) - rows[i])
            elif max_s[0] == 'col':
                j = max_s[-1]
                i = 0
                while i < len(board):
                    if board[i][j] == '0':
                        break
                    i += 1
                unfilled = list(set(range(1, 10)) - cols[j])
            elif max_s[0] == 'box':
                i_, j_ = max_s[1], max_s[2]
                i, j = 0, 0
                found = 0
                for i in range(i_*3, i_*3 + 3):
                    for j in range(j_*3, j_*3 + 3):
                        if board[i][j] == '0':
                            found = 1
                            break
                    if found:
                        break
                unfilled = list(set(range(1, 10)) - boxes[(i_, j_)])
            else:
                # print("board all filled")
                return -1, -1, [] # no unfilled

            # print("next to fill at", i, j, unfilled)
            return i, j, unfilled


        def valid():
            """
            
            """
            # print("current board", board)
            i, j, unfilled = choose_next_fill()
            if not unfilled:
                return 1
                
            found = 0        
            for n_next in unfilled:
                # check if valid for all three sets
                if check_valid(i, j, n_next):
                    fill(i, j, n_next)
                    success = valid()
                    if not success:
                        erase(i, j, n_next) # try next in unfilled 
                    else:
                        found = 1
                        break   

            if found:
                return 1
            else:
                return 0 # deadend


        print(valid())

        
def p96():
    # parse the problems
    problems = []
    with open('sudoku') as f:
        lines = f.readlines()
        i = 0
        
        while i < len(lines):
            if i % 10 == 0:
                problem = []
            else:
                problem.append(list(lines[i].strip('\n')))
                if i % 10 == 9:
                    problems.append(problem)
            i += 1

    """
    By solving all fifty puzzles find the sum of the 3-digit numbers 
    (i, j ->[0, 0], [0, 1], [0, 2]) 
    found in the top left corner of each solution grid; 
    """

    solver = Solution()
    totalSum = 0
    for problem in problems:
        print(problem)
        solver.solveSudoku(problem)
        totalSum += int(problem[0][0])*100 + int(problem[0][1])*10 + int(problem[0][2])
        print("solved")


    return totalSum

if __name__ == "__main__":
    print(p96())











                    





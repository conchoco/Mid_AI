from collections import deque

class Graph:
    def __init__(self, row, col, graph):
        self.R = row
        self.C = col
        self.G = graph


    def isSafe(self, i, j, vis):

        return ((i >= 0) and (i < self.R) and
                (j >= 0) and (j < self.C) and
            (self.G[i][j] and (not vis[i][j])))

    def BFS(self, vis, si, sj):


        row = [-1, -1, -1, 0, 0, 1, 1, 1]
        col = [-1, 0, 1, -1, 1, -1, 0, 1]

        q = deque()
        q.append([si, sj])
        vis[si][sj] = True


        while (len(q) > 0):
            temp = q.popleft()

            i = temp[0]
            j = temp[1]

            for k in range(8):
                if (self.isSafe(i + row[k], j + col[k], vis)):
                    vis[i + row[k]][j + col[k]] = True
                    q.append([i + row[k], j + col[k]])


    def countIslands(self):

        vis = [[False for i in range(self.C)]
                for i in range(self.R)]

        res = 0

        for i in range(self.R):
            for j in range(self.C):
                if (self.G[i][j] and not vis[i][j]):
                    self.BFS(vis, i, j)
                    res += 1

        return res

if __name__ == '__main__':

    mat = [ [ 1, 1, 0, 0, 0, 1 ],
            [ 0, 1, 0, 0, 0, 0 ],
            [ 1, 0, 0, 1, 1, 0 ],
            [ 0, 0, 0, 0, 0, 0 ],
            [ 1, 0, 1, 0, 1, 0 ],
            [ 1, 0, 1, 0, 1, 0 ],
            [ 1, 0, 1, 0, 1, 0 ]]
    g = Graph(len(mat),len(mat[0]),mat)
    print (g.countIslands())
from queue import PriorityQueue

class Graph:
    def __init__(self, row, col, graph):
        self.R = row
        self.C = col
        self.G = graph


    def isIsland(self, i, j, vis):

        return ((i >= 0) and (i < self.R) and
                (j >= 0) and (j < self.C) and
            (self.G[i][j] and (not vis[i][j])))

    def countIslands(self):
        count = 0
        for i in range(self.R):
            for j in range(self.C):
                if self.G[i][j] != 0:
                    count+=1

        vis = [[False for i in range(self.C)]
                for i in range(self.R)]

        for i in range(self.R):
            for j in range(self.C):
                if (self.G[i][j] and not vis[i][j]):
                    count = self.UCS(vis, i, j, count)

        return count

    def UCS(self, vis, si, sj, count):

        row = [-1, -1, -1, 0, 0, 1, 1, 1]
        col = [-1, 0, 1, -1, 1, -1, 0, 1]

        pq = PriorityQueue()
        pq.put((self.G[si][sj], si, sj))
        vis[si][sj] = True

        while not pq.empty():
            temp = pq.get();

            cost = temp[0];
            i = temp[1];
            j = temp[2];

            for k in range(8):
                if (self.isIsland(i + row[k], j + col[k], vis)):
                    vis[i + row[k]][j + col[k]] = True
                    count-=1
                    pq.put((self.G[i + row[k]][j + col[k]] + cost, i + row[k], j + col[k]))

        return count

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
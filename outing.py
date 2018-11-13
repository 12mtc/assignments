

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = []
        for i in range(V):
            row = []
            for j in range(V):
                row.append(0)
            self.graph.append(row)

    def grouping(self, src):
        groupNum = [-1]*self.V
        groupNum[src] = 1

        list = []
        list.append(src)

        while list:
            temp = list.pop()

            if self.graph[temp][temp] == 1:
                return False

            for i in range(self.V):
                if self.graph[temp][i] == 1 and groupNum[i] == -1:
                    groupNum[i] = 1 - groupNum[temp]
                    list.append(i)

                elif self.graph[temp][i] == 1 and groupNum[temp] == groupNum[i]:
                    return False
        return groupNum

    def groupUp(self,src):
        groupNum = []
        for i in range(self.V):
            groupNum.append(0)

        groupNum[src] = 2

        list = []
        list.append(src)

        while list:
            temp = list.pop()

            for i in range(self.V):
                if self.graph[temp][i] == 0 and groupNum[i] == 0:
                    if groupNum[i] == 1:
                        groupNum[i] = 2
                    else:
                        groupNUm[i] = 1
                    list.append(i)

                elif self.graph[temp][i] == 0 and groupNum[temp] == groupNum[i]:
                    return False
        return groupNum




def main():
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]
               ]

    print (g.graph)
    print(g.grouping(0))

    g = Graph(4)
    g.graph = [[1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1]
               ]

    print(g.graph)
    print(g.groupUp(0))

if __name__ == '__main__':
    main()
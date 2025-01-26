# Graph representation
v=4
edges=[(0,1),(0,2),(1,2),(1,3)]

# adjacency matrix 
# 0 1 1 0
# 1 0 1 1
# 1 1 0 0
# 0 1 0 0

def adjacencyMatrix(v,edges):
    matrix=[[0 for i in range(v)] for j in range(v)]
    for src,dest in edges:
        matrix[src][dest]=1
        matrix[dest][src]=1
    # return matrix/
    for row in matrix:
        # print(row)
        print(" ".join(map(str,row)))


adjacencyMatrix(v,edges)

# adjacency list representation of a graph
# [1,2],[0,2,3],[0,1],[1]

def adjacencyList(v,edges):
    adjList=[[] for i in range(v)]
    for src,dest in edges:
        adjList[src].append(dest)
        adjList[dest].append(src)

    for i in range(v):
        print(f"Vertex {i} --> {adjList[i]}")

adjacencyList(v,edges)

# map adjacency list representation of a graph
# {0:[1,2],1:[0,2,3],2:[0,1],3:[1]}

def adjacencyListMap(v,edges):
    adjList={}
    for src,dest in edges:
        if src in adjList:
            adjList[src].append(dest)
        else:
            adjList[src]=[dest]
        if dest in adjList:
            adjList[dest].append(src)
        else:
            adjList[dest]=[src]
    for key,value in adjList.items():
        print(f"Vertex {key} --> {value}")

adjacencyListMap(v,edges)
def bfs(graph,start):
    visited = set()
    queue = inst-queue([start])
    visited.add(start)
    tr_ordwr = []
    while queue:
        vertex = queue.pop()
        tr_order.append(vertex)
        for ne in graph [vertex]
            if ne not in visited :
                visited.append(ne)
                queue.append(ne)
    return tr_order



def rec_DFS(graph,start,visited=None):
    if visited is None:
        visited=[]
    visited.add(start)
    for ne in graph[start]:
       if ne not in visited:
         rec_DFS(graph,ne,visited)
    return visited


def sort-1 (A):
   s = len(A)
   B = [] * s
   for i in rang(s):
       min=A[0]
       k=0
       for j in range (1,s):
           if A[j]<min :
              min=A[j]
              k=j 
        B[i]=min
        A[k]=float('inf')
    return B 




def Bubbie(A):
   s=len(A)
   for i in range(s-1):
      for j in range(s-1):
         if A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
            
      
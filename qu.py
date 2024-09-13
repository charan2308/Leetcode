from queue import Queue
def bfsOfGraph( V: int, adj: list[list[int]]) -> list[int]:
        # code here
        visited=[0]*V
        visited[0]=1
        queue=Queue()
        queue.put(0)
        result=[]
        while not queue.empty():
            x=queue.get()
            result.append(x)
            visited[x]=1
            if adj[x]!=[]:
                for i in adj[x]:
                    if not visited[i]:
                        print(i)
                        queue.put(i)
                
        return result

print(bfsOfGraph(5,[[1,2,3],[],[4],[],[]]))
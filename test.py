def find_paths(nodes,graph_from,graph_to,weights,source,destination):
    d={}
    for i in range(nodes):
        d[i]=[]
    for i in range(len(graph_from)):
       d[graph_from[i]].append((graph_to[i],weights[i]))
       d[graph_to[i]].append((graph_from[i],weights[i]))
    print(d)
    path=[]
    fin_paths=[]
    visited=set()
    minmum=float('inf')
    result=[]
    def rec(nodes,source,destination,dict,path,fin_paths,visited,minmum,result,w):
        path.append(source)
        visited.add(source)
        if source==destination:
            if w<=minmum:
                minmum=w
                result.append(list(path))
            fin_paths.append([list(path),w])
        else:
            for node,weight in dict[source]:
                if node not in visited:
                    rec(nodes,node,destination,dict,path,fin_paths,visited,minmum,result,w+weight)
        path.pop()
        visited.remove(source)    
        
            
    rec(nodes,source,destination,d,path,fin_paths,visited,minmum,result,w=0)
    print(fin_paths)
    return (fin_paths,result,minmum)
# Example usage (assuming `neighbors`, `source`, and `destination` are defined):
nodes=5
graph_from = [0, 0, 1, 1, 2, 3]
graph_to = [1, 2, 2, 3, 3, 4]
weights = [4, 2, 5, 10, 3, 1]
source = 0
destination = 2

fin_paths=find_paths(nodes,graph_from,graph_to,weights,source,destination)

print(f"All possible paths from {source} to {destination}:")
for p,weight in fin_paths[0]:
    print(" -> ".join(map(str, p)),weight)
print(fin_paths[1],fin_paths[2])

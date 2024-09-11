edges = [ (0, 2), (1, 2),  (3, 4)]
n = len(edges)
source = 4
destination = 3
number=5
neighbors={}
for x in range(0,number):
    neighbors[x] =[]
for x in edges:
    neighbors[x[0]].append(x[1])
    neighbors[x[1]].append(x[0])
print(neighbors)
final_paths=[]

def find_paths(neighbors,current,destination,visited,path,final_paths):
    visited.add(current)
    path.append(current)
    if current==destination:
        print("destination found",path)
        final_paths.append(list(path))
        print("final_paths found",final_paths)
    for x in neighbors[current]:
        if x not in visited:
            find_paths(neighbors,x,destination,visited,path,final_paths)
    print("path to be popped: " , path)
    path.pop()
    visited.remove(current)
    
visited = set()
path=[]

find_paths(neighbors, source, destination,visited,path,final_paths)
print(f"All possible paths from {source} to {destination}:")
print(final_paths)
if len(final_paths)==0:
    print(f"No paths from {source} to {destination}")
else:
    for path in final_paths:
        print(" -> ".join(map(str, path)))
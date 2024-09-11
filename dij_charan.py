import heapq
def dij(neighbors,source, destination):
    queue=[(0,source,[])]
    visited=set()

    while queue:
        total_cost,current_node,current_path=heapq.heappop(queue)
        visited.add(current_node)
        current_path=current_path+[current_node]

        if current_node==destination:
            return total_cost,current_path      

        for neighbor,weight in neighbors[current_node]:
            if neighbor not in visited:
                heapq.heappush(queue,(total_cost+weight,neighbor,current_path))
       
    return (-1,[])  


source = 1
destination = 3

neighbors={
    0: [(1, 4), (2, 2)],
    1: [(2, 5), (3, 10)],
    2: [(3, 3)],
    3: [(4,6)],
    4: []
}
cost,path=dij(neighbors,source,destination)
print(cost,path)
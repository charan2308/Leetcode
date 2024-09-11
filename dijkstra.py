import heapq


import math

def print_heap(heap, index=0, indent=0):
    # If the index is out of range, return
    if index >= len(heap):
        return
    
    # Recursively print the right child (with increased indentation)
    print_heap(heap, 2 * index + 2, indent + 4)
    
    # Print the current node with indentation
    print(" " * indent + str(heap[index]))
    
    # Recursively print the left child (with increased indentation)
    print_heap(heap, 2 * index + 1, indent + 4)

    
def dijkstra_min_cost(neighbors, source, destination):
    # Priority queue stores (cost, current_node, path_to_current_node)
    queue = [(0, source, [])]  # (cumulative cost, node, path to that node)
    visited = set()
    # print_heap(queue)
    while queue:
        # Get the node with the lowest cost
        cost, current_node, path = heapq.heappop(queue)
        # If the node is visited, skip it
        if current_node in visited:
            continue
        
        # Mark the node as visited
        visited.add(current_node)
        
        # Add the current node to the path
        path = path + [current_node]
        print(f"\ncost to go to node {current_node} = {cost}, and the path taken=", path)

        # If we have reached the destination, return the cost and the path
        if current_node == destination:
            return cost, path
        
        # Explore neighbors
        print(f"\nexploring neighbors of node {current_node} and these are the neighbors: {neighbors[current_node]}")
        for neighbor, weight in neighbors[current_node]:
            if neighbor not in visited:
                # Add the neighbor to the priority queue with updated cumulative cost
                heapq.heappush(queue, (cost + weight, neighbor, path))
                # print_heap(queue)
    return float('inf'), []  # Return infinity if there is no path to destination

# Use the graph built from `graph_from`, `graph_to`, and `weights`
source = 0
destination = 4

neighbors={
    0: [(1, 4), (2, 2)],
    1: [(2, 5), (3, 10)],
    2: [(3, 3)],
    3: [(4, 1)],
    4: []
}
min_cost, min_path = dijkstra_min_cost(neighbors, source, destination)
print(f"Minimum cost to reach {destination} from {source}: {min_cost}")
print(f"Path: {' -> '.join(map(str, min_path))}")

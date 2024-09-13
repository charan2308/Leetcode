def find_min_value_added(N, A, G):
    # Compute the sums of A and G
    N=input1
    A=input2
    G= input3
    sum_A = sum(A)
    sum_G = sum(G)
    
    sum_diff = sum_A - sum_G
    
    A.sort()
    G.sort()
    # Find the minimum value x by comparing sorted arrays
    for i in range(N - 2):  # N - 2 because 2 elements are removed
        # The potential value of x
        x = G[i] - A[i]
        if x > 0:
            # Create the transformed A array with added x
            transformed_A = [a + x for a in A if a + x in G]
            transformed_A.sort()
            if transformed_A == G:
                return x
    
    return -1  # If no valid x is found, which theoretically shouldn't happen

# Example usage
N = 5
A = [1, 2, 3, 4, 5]
G = [3, 4, 5, 6, 7]
print(find_min_value_added(N, A, G))  # Output: 2

def max_separations(N, arr, k):
    # Step 1: Calculate the cumulative count of odd and even numbers
    odd_count = [0] * (N + 1)
    even_count = [0] * (N + 1)

    for i in range(1, N + 1):
        odd_count[i] = odd_count[i - 1] + (1 if arr[i - 1] % 2 != 0 else 0)
        even_count[i] = even_count[i - 1] + (1 if arr[i - 1] % 2 == 0 else 0)

    # Step 2: Identify valid separation points and their costs
    valid_separations = []
    for i in range(1, N):
        if odd_count[i] == even_count[i] and odd_count[N] - odd_count[i] == even_count[N] - even_count[i]:
            cost = abs(arr[i] - arr[i - 1])
            valid_separations.append((cost, i))

    # Step 3: Sort valid separations by cost
    valid_separations.sort()

    # Step 4: Use dynamic programming to find the maximum number of separations within the given cost k
    dp = [0] * (k + 1)

    for cost, _ in valid_separations:
        for j in range(k, cost - 1, -1):
            dp[j] = max(dp[j], dp[j - cost] + 1)

    # The answer is the maximum number of separations we can achieve within cost k
    return max(dp)

# Example usage:
N = 6
arr = [1, 3, 2, 4, 6, 5]
k = 4

result = max_separations(N, arr, k)
print(result)  # Output: 2 (assuming optimal separations can be made with the given k)
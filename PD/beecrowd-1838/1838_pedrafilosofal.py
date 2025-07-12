import bisect

def binary_search(requests, idx):
    """Encontra o último intervalo que termina antes de requests[idx][0]."""
    low, high = 0, idx - 1
    while low <= high:
        mid = (low + high) // 2
        if requests[mid][1] <= requests[idx][0]:
            if requests[mid + 1][1] <= requests[idx][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

n = int(input())
requests = []

for _ in range(n):
    i, j = map(int, input().split())
    requests.append((i, j))

# Ordenar por tempo de término
requests.sort(key=lambda x: x[1])

# dp[i] = melhor tempo acumulado até o i-ésimo intervalo
dp = [0] * n
dp[0] = requests[0][1] - requests[0][0]

for i in range(1, n):
    incl = requests[i][1] - requests[i][0]
    prev = binary_search(requests, i)
    if prev != -1:
        incl += dp[prev]
    dp[i] = max(dp[i - 1], incl)

print(dp[-1])


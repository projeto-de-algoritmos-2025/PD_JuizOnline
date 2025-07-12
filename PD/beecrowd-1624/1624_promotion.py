def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # dp[i][w] representa o valor máximo usando os i primeiros itens com capacidade w
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Se puder levar o item, escolhe o máximo entre levar e não levar
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Não pode levar o item, mantém o valor anterior
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


while True:
    try:
        N = int(input())
        if N == 0:
            break

        values = []
        weights = []

        for _ in range(N):
            p, w = map(int, input().split())
            values.append(p)
            weights.append(w)

        max_weight = int(input())
        result = knapsack(values, weights, max_weight)
        print(result)

    except EOFError:
        break

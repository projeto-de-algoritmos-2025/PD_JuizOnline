def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    
    while ptr < len(input):
        N = int(input[ptr])
        M = int(input[ptr + 1])
        ptr += 2
        B = list(map(int, input[ptr:ptr + M]))
        ptr += M
        
        # Inicialização da DP
        dp = [-1] * N
        dp[0] = 0  # Caso base: zero pacotes, resto zero
        
        for candy in B:
            new_dp = dp.copy()
            candy_mod = candy % N
            for r in range(N):
                if dp[r] != -1:
                    new_r = (r + candy_mod) % N
                    if new_dp[new_r] < dp[r] + 1:
                        new_dp[new_r] = dp[r] + 1
            dp = new_dp
        
        print(dp[0])

solve()

https://judge.beecrowd.com/en/problems/view/2524
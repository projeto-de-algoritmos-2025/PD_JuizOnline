import sys

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    N = int(line)
    if N == 0:
        break
    P_line = sys.stdin.readline().strip()
    while P_line == "":  # pula possíveis linhas vazias
        P_line = sys.stdin.readline().strip()
    P = int(P_line)
    orders = []
    for _ in range(N):
        t_p_line = sys.stdin.readline().strip()
        while t_p_line == "":  # pula linhas vazias se houver
            t_p_line = sys.stdin.readline().strip()
        time_str, pizzas_str = t_p_line.split()
        tempo = int(time_str); pizzas = int(pizzas_str)
        orders.append((tempo, pizzas))
    dp = [0] * (P + 1)
    for tempo, pizzas in orders:
        for cap in range(P, pizzas - 1, -1):
            if dp[cap - pizzas] + tempo > dp[cap]:
                dp[cap] = dp[cap - pizzas] + tempo
    # Imprime resultado no formato "X min."
    print(f"{dp[P]} min.")
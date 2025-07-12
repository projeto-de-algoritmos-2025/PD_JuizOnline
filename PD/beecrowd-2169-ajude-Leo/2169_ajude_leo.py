import sys

# Multiplicamos todas as potências por 10 para evitar float
weapon_power = {
    "HANDGUN": 20,
    "RED9": 35,
    "BLACKTAIL": 35,
    "MATILDA": 20,
    "HANDCANNON": 600,
    "STRIKER": 120,
    "TMP": 12,
    "RIFLE": 120,
    "GATLINGGUN": 50,
}

monster_life = {
    "GANADOS": 50,
    "COBRAS": 40,
    "ZEALOT": 75,
    "COLMILLOS": 60,
    "GARRADOR": 125,
    "GATLINGMAN": 150,
    "LASPLAGAS": 100,
    "REGENERATOR": 250,
    "ELGIGANTE": 500,
    "DR.SALVADOR": 350,
}

def solve_case(armas, monstros, limite_balas):
    dp = [0] * (limite_balas + 1)
    
    for arma, qtd in armas:
        dano = weapon_power[arma] * qtd
        for b in range(limite_balas, qtd - 1, -1):
            dp[b] = max(dp[b], dp[b - qtd] + dano)
    
    dano_necessario = sum(monster_life[m] * q for m, q in monstros) * 10

    for dano in dp:
        if dano >= dano_necessario:
            return "Missao completada com sucesso"
    return "You Are Dead"

def main():
    lines = sys.stdin.read().splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip() == "":
            i += 1
            continue

        QA = int(lines[i])
        i += 1
        armas = []
        for _ in range(QA):
            nome, qtd = lines[i].split()
            armas.append((nome, int(qtd)))
            i += 1

        QM = int(lines[i])
        i += 1
        monstros = []
        for _ in range(QM):
            nome, qtd = lines[i].split()
            monstros.append((nome, int(qtd)))
            i += 1

        QB = int(lines[i])
        i += 1

        print(solve_case(armas, monstros, QB))

if __name__ == "__main__":
    main()

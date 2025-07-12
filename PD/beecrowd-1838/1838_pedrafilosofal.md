# A questão

![1838 Questão](../../assets/1838-pedra/1838_The_Philosophers_Stone_question.png)

# Estratégia:

Neste problema, temos uma situação que envolve a alocação de um recurso limitado (a Pedra Filosofal) entre diversas solicitações de uso. O objetivo é atender ao máximo de solicitações possível, de forma que o tempo de uso da pedra seja o maior possível, sem sobreposição entre os intervalos.

Esse tipo de problema é conhecido como **Interval Scheduling**, e mais especificamente, a versão ponderada conhecida como **Weighted Interval Scheduling** — pois cada intervalo (solicitação) tem um valor associado, que neste caso é o número de minutos de uso.

1. Cada solicitação tem um tempo de início e fim.  
2. O tempo total de uso da solicitação é o "peso" (ou valor) que queremos maximizar.  
3. Não é permitido que duas solicitações se sobreponham.  
4. O objetivo é maximizar o tempo total de uso da pedra durante a semana.

# Algoritmo utilizado

Foi implementada uma solução com **Programação Dinâmica** combinada com **Busca Binária**.

As solicitações foram ordenadas pelo tempo de término. Para cada uma delas, procuramos a última solicitação que termina antes da atual começar, utilizando busca binária. Isso permite montar uma relação de recorrência eficiente.

A fórmula usada foi:

dp[i] = max(dp[i-1], dp[último_compatível] + duração_da_atual)


Ao final, o maior valor encontrado em `dp` representa o maior tempo de uso contínuo possível da pedra.

# Resultado

O algoritmo alcançou o resultado esperado e foi aceito pela plataforma. A imagem a seguir confirma a submissão correta:

![1838 Accepted](../../assets/1838-pedra/1838_The_Philosophers_Stone_accepted.png)
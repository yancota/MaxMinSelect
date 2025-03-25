# Max Min Select

Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select) em Python. Esse algoritmo utiliza a abordagem de divisão e conquista, com o objetivo de encontrar o maior e o menor elemento de um vetor, de forma recursiva.

## Como rodar o projeto

Instalar a última versão do python disponível em: https://www.python.org/downloads/

Necessário rodar o seguinte comando no terminal:
```bash
https://github.com/yancota/Karatsuba.git
```

Rodar o seguinte comando no terminal:
```bash
python main.py
```

## Versão do Python
Este projeto foi desenvolvido na versão 3.13.2 do Python.


## Explicação das funções

### Arquivo: main.py

- **Objetivo:** Este arquivo principal permite ao usuário inserir números de forma interativa. Após inserir os números, o algoritmo MaxMin Select encontra o menor e o maior número da lista usando um método recursivo

- **Descrição das funções:**

#### `max_min_select(numeros, primeiro, ultimo)`
- Determinar o menor e o maior valor de uma lista usando divisão e conquista.
- **Parâmetros:**
  - `numeros`: lista de números inteiros;
  - `primeiro`: índice inicial do intervalo analisado;
  - `ultimo`: índice final do intervalo analisado.
- **Lógica:**
  - Caso base: Se houver apenas um elemento, ele é o menor e o maior.
  - Caso base: Se houver dois elementos, compara e retorna o menor e o maior.
  - Passo 1 – Divisão: O array é dividido ao meio.
  - Passo 2 – Conquista: A função é chamada recursivamente para as duas metades.
  - Passo 3 – Combinação: O menor e o maior valores de cada metade são comparados para encontrar o menor e o maior valores globais.
- **Retorno:**
  - O menor e o maior número da lista.
- **Entrada:**
  - Usuário insere um número por vez.
  - Ao digitar "OK" o sistema faz a análise e devolve o maior e menor elemento que o usuário inseriu.

## Saída da Execução

```
Insira um número. Digite 'OK' para concluir.
Digite um número: 1
Digite um número: 5
Digite um número: 6
Digite um número: 20
Digite um número: 0
Digite um número: 4
Digite um número: OK

Menor elemento: 0
Maior elemento: 20
```

## Análise Ciclomática por Contagem de Operação
 def max_min_select(numeros, primeiro, ultimo):
    if primeiro == ultimo:                             -- 1 (verificação if)
        return arr[primeiro], arr[primeiro]            -- 1 (retorno método)
    
    if ultimo == primeiro + 1:                         -- 1 (verificação if)
        if arr[primeiro] < arr[ultimo]:                -- 1 (retorno método)
            return arr[primeiro], arr[ultimo]
        else:
            return arr[ultimo], arr[primeiro]          -- 1 (retorno método)

    mid = (primeiro + ultimo) // 2                     -- 1 (atribuição de variável)
    min1, max1 = max_min_select(arr, primeiro, mid)    -- 1 (atribuição subvetor)
    min2, max2 = max_min_select(arr, mid + 1, ultimo)  -- 2 (atribuição subvetor)

    return min(min1, min2), max(max1, max2)            -- (n - 1) * 2 (2 chamadas recursiva)

 - Pode-se concluir que devido ao maior fator ser a recursividade do final (2n), a complexidade do método é O(n)

## Aplicação do Teorema Mestre
  A recorrência do MaxMin Select é:
   - T(n)=2T(n/2)+O(1)
  Comparando com a fórmula geral do Teorema Mestre:
   - T(n)=aT(n/b)+f(n)
  Temos:
   - a = 2
   - b = 2
   - f(n) = O(1)
   - p = log na base b de a = log na base de 2 de 2 = 1
  De acordo com o Teorema Mestre:
   - f(n) = O(1) = O(n^c), onde c = 0
   - c < p, então usamos T(n) = O(n^p)
  Solução Assintótica:
   - T(n)=O(n)










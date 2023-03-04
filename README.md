# Trabalho - Algoritmos e Estruturas de Dados 2

## 8 puzzle (quebra-cabeças de 8 peças)

Um tabuleiro com 8 peças numeradas de 1 a 8 está disposto em um grid de 3 linhas e 3 colunas. Existe uma posição em branco e as peças podem ser movimentadas para ocupar essa posição.

![puzzle](https://i.stack.imgur.com/So6k6.png)

O objetivo do jogo é encontrar a sequência de transições mais curta até o estado em que as peças estão todas em ordem e a posição vazia está no canto superior esquerdo.

## Objetivo do Trabalho

Resolver o 8 puzzle usando fila de prioridade. 

## Requisitos

1. Ao abrir a interface, deve-se mostrar o tabuleiro no estado final.
2. Deve ser possível mover as peças manualmente.
3. Deve ser possível gerar uma configuração aleatoriamente.
4. Deve haver uma opção para resolver o problema a partir do estado que estiver sendo exibido no momento. O programa deve mostrar a sequência de passos para sair do estado atual e chegar ao estado final.

## Fila de prioridade

### A* Estratégia de pesquisa
O algoritmo de busca A* é uma versão do algoritmo de Dijkstra que executa melhor do que buscas exaustivas em certas situações devido ao seu uso de heurísticas para orientar a pesquisa.
À medida que o algoritmo de busca está em execução, A* determina o próximo nó a ser expandir determinando a estimativa do custo ou peso para atingir
o estado objetivo. Isso é feito usando a seguinte equação:

    f(n) = g(n) + h(n)

Onde n é o nó no caminho, g(n) é o custo desde o início
nó ao n dado, e h(n) é o valor heurístico que estima
o custo restante de n para o estado objetivo.

### Heurística

A heurística pode ser o número de peças em posições incorretas.

O estado final é f=(0,1,2,3,4,5,6,7,8)
.

Então dado um estado x=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
, a heurística pode ser calculada como a soma

h(x)=∑i=08I(xi,i)

Sendo que I(xi,i)=1
 se e somente se i≠0
 e xi≠i
 e I(xi,i)=0
 caso contrário.

Por exemplo, se o estado for x=(6,2,8,4,0,1,5,3,7)
, então calcula-se h(x)=8
, pois todas as peças estão em posições incorretas. Note que o espaço em branco não conta.

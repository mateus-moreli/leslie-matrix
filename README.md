# leslie-matrix
An algorithmic approach to a known mathematical/biological problem. This project was done as part of a PIBIC project at UFMS.

Este trabalho de iniciação científica foca no estudo e implementação do Modelo de Leslie para resolver problemas de previsão do comportamento de populações. 
Modelo de Leslie é um modelo matemático que encontra sua aplicação na ecologia populacional uma vez que descreve como a influência de fatores como taxa de fecundidade e sobrevivência afetam uma população, permitindo que sejam tomadas decisões mais acertadas. 

O modelo matricial de Leslie, segundo Anton(2001), consiste no sistema X^k = L*X^(k-1),  para k natural, onde L é chamada de matriz de Leslie, x^s, s>0 para inteiro, chamado de vetor de distribuição etária, e X0 de vetor de distribuição etária inicial e as entradas da matriz L são formados por constantes reais  chamadas de parâmetros demográficos. 

Para fazer o algoritmo da maneira mais eficiente, pesquisei diversas propriedades de equações de diferenças lineares associadas ao modelo matricial de Leslie de forma a estabelecer diversas fórmulas como para entrada de vetor de distribuição etária, bem como seu comportamento assintótico, como mostrado por Ben-Taher(2021). Além disso, investiguei fórmulas explícitas para as entradas das potências da matriz de Leslie utilizando um processo recursivo semelhante a Fibonacci, conforme indicado por Ben-Taher, Naassi e Rachidi (2017).

Projeto de 2022/2023

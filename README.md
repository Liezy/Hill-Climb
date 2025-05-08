# Hill Climbing Optimization

Um exemplo simples de implementação do algoritmo **Hill Climbing** em Python para maximização da função  
\`f(x) = -x^2 + 4x\` no intervalo discreto \`x ∈ {0,…,10}\`.

---

## Descrição  
Este repositório apresenta uma abordagem passo a passo do Hill Climbing, um método de busca local que inicia de uma solução aleatória e explora vizinhanças para encontrar um ótimo local :contentReference[oaicite:0]{index=0}. O código exemplifica:  
1. Escolha de estado inicial aleatório.  
2. Geração de vizinhos (incremento/decremento de 1).  
3. Avaliação da função objetivo e movimentação para o melhor vizinho.  
4. Parada ao alcançar estagnação ou limite de iterações :contentReference[oaicite:1]{index=1}.

---
### Membros do Grupo

- Cássio Coutinho

- Eliézer Alencar

- Júlia Leal
---

## Sumário  
- [Instalação](#instalação)  
- [Uso](#uso)  
- [Explicação do Algoritmo](#explicação-do-algoritmo)  
- [Exemplo de Execução](#exemplo-de-execução)  
- [Boas Práticas de README](#boas-práticas-de-readme)  
- [Contribuição](#contribuição)  
- [Licença](#licença)  
- [Contato](#contato)

---

## Instalação  
1. Clone este repositório:  
   ```bash
   git clone https://github.com/liezy/hill-climbing.git
   ```
(Opcional) Crie e ative um ambiente virtual:

```bash
Copiar
Editar
python3 -m venv venv  
source venv/bin/activate 
``` 
Instale dependências (nenhuma além da biblioteca padrão do Python):

```bash
pip install --upgrade pip  
```

## Uso
Execute o script principal:

```bash
python hill_climbing.py
```
Isso iniciará o algoritmo, exibindo no console a melhor solução encontrada e o valor de f(x) 
Learn R, Python & Data Science Online
.

## Explicação do Algoritmo
Estado Inicial
Seleciona aleatoriamente um x ∈ [0,10].

Vizinhanças
Gera x-1 e x+1 (quando válidos) como candidatos.

Avaliação
Calcula f(n) para cada vizinho n.

Movimento
Adota o vizinho com maior valor se for melhor que o atual; caso contrário, encerra (óptimo local) 
GitHub
.

Parada
Para quando não há melhora ou ao atingir o número máximo de iterações.

## Exemplo de Execução
```bash
python hill_climbing.py  
Melhor solução encontrada: x = 2, f(x) = 4
```
Nesse caso, o algoritmo encontrou o pico da parábola em x=2, onde f(2)=0 
MachineLearningMastery.com
.
import random

def f(x):
    """Função objetivo: f(x) = -x^2 + 4x."""
    return -x**2 + 4*x

def hill_climbing(max_iter=100):
    # 1. Estado inicial: ponto aleatório em 0–10
    current = random.randint(0, 10)
    current_value = f(current)

    for i in range(max_iter):
        # 2. Geração de vizinhanças
        neighbors = []
        if current > 0:
            neighbors.append(current - 1)
        if current < 10:
            neighbors.append(current + 1)

        # 3. Avaliação de cada vizinho
        neighbor_values = [(n, f(n)) for n in neighbors]

        # 4. Escolhe o melhor vizinho
        best_neighbor, best_value = max(neighbor_values, key=lambda p: p[1])

        # 5. Se não houver melhora, para
        if best_value <= current_value:
            break

        # 6. Caso contrário, atualiza estado atual
        current, current_value = best_neighbor, best_value

    return current, current_value

if __name__ == "__main__":
    solution, value = hill_climbing()
    print(f"Melhor solução encontrada: x = {solution}, f(x) = {value}")

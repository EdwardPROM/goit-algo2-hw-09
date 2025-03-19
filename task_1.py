import random
import math

# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Функція для генерації випадкової точки в межах bounds
def random_point(bounds):
    return [random.uniform(bound[0], bound[1]) for bound in bounds]

# Функція для обмеження координат в межах bounds
def clip_bounds(point, bounds):
    return [max(min(point[i], bounds[i][1]), bounds[i][0]) for i in range(len(point))]

# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6, step_size=0.1):
    current_point = random_point(bounds)
    current_value = func(current_point)

    for iteration in range(iterations):
        candidate = [xi + random.uniform(-step_size, step_size) for xi in current_point]
        candidate = clip_bounds(candidate, bounds)
        candidate_value = func(candidate)

        if candidate_value < current_value:
            current_point, current_value = candidate, candidate_value

        if candidate_value - current_value < epsilon:
            break

    return current_point, current_value

# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_point = random_point(bounds)
    best_value = func(best_point)

    for iteration in range(iterations):
        candidate = random_point(bounds)
        candidate_value = func(candidate)

        if candidate_value < best_value:
            if abs(candidate_value - best_value) < epsilon:
                break
            best_point, best_value = candidate, candidate_value

    return best_point, best_value

# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current_point = random_point(bounds)
    current_value = func(current_point)
    best_point, best_value = current_point, current_value
    current_temp = temp

    for iteration in range(iterations):
        candidate = [xi + random.uniform(-1, 1) for xi in current_point]
        candidate = clip_bounds(candidate, bounds)
        candidate_value = func(candidate)

        delta = candidate_value - current_value

        if delta < 0 or random.random() < math.exp(-delta / current_temp):
            current_point, current_value = candidate, candidate_value

        if current_value < best_value:
            best_point, best_value = current_point, current_value

        current_temp *= cooling_rate

        if current_temp < epsilon:
            break

    return best_point, best_value

if __name__ == "__main__":
    # Межі для функції (2D)
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds, iterations=1000)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds, iterations=1000)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds, iterations=1000, temp=1000, cooling_rate=0.95)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)

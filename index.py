from decorators.benchmark import benchmark
from decorators.counter import counter
from decorators.logging import logging
from decorators.memo import memo


@benchmark
@logging
@counter
@memo
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Расчет чисел Фибоначчи для n = 35 без декоратора memo
def fibonacci_no_memo(n):
    if n <= 1:
        return n
    return fibonacci_no_memo(n - 1) + fibonacci_no_memo(n - 2)

import time

n = 35

# Измеряем время выполнения без мемоизации
start_time = time.time()
print(f"Результат: {fibonacci_no_memo(n)}")
end_time = time.time()
print(f"Время выполнения без мемоизации: {end_time - start_time:.4f} секунд")

print("\nС мемоизацией:")

# С мемоизацией
start_time = time.time()
print(f"Результат: {fibonacci(n)}")
end_time = time.time()
print(f"Время выполнения с мемоизацией: {end_time - start_time:.4f} секунд")

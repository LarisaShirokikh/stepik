import time

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()  # Начало измерения времени
        result = func(*args, **kwargs)  # Вызов декорируемой функции
        end_time = time.time()  # Конец измерения времени
        elapsed_time = end_time - start_time  # Вычисление затраченного времени
        print(f"Время выполнения функции '{func.__name__}': {elapsed_time:.4f} секунд")
        return result  # Возвращение результата выполнения функции

    return wrapper
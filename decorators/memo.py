def memo(func):
    """
    Декоратор, запоминающий результаты исполнения функции (мемоизация).
    Аргументы *args должны быть хешируемыми.
    """

    cache = {}  # Хранилище для кэширования результатов

    def wrapper(*args):
        if args in cache:  # Проверка, если результат уже в кэше
            return cache[args]  # Возвращаем сохраненный результат
        result = func(*args)  # Вызываем функцию и сохраняем результат
        cache[args] = result
        return result

    return wrapper

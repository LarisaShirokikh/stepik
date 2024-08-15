def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции.
    """


    def wrapper(*args, **kwargs):
        wrapper.call_count += 1  # Увеличение счетчика вызовов
        print(f"Функция '{func.__name__}' была вызвана {wrapper.call_count} раз(а)")
        return func(*args, **kwargs)
    wrapper.call_count = 0  # Инициализация счетчика

    return wrapper

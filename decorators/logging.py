def logging(func):
    """
    Декоратор, который выводит параметры, с которыми была вызвана функция.
    """

    def wrapper(*args, **kwargs):
        print(f"Вызов функции '{func.__name__}' с аргументами: args = {args}, kwargs = {kwargs}")
        return func(*args, **kwargs)

    return wrapper
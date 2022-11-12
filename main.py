import timeit
import sys
from collections import namedtuple, defaultdict, deque, Counter


def test_iterating(iterable):
    for i in iterable:
        pass


def test_lookups(iterable):
    for i in range(1000):
        if i in iterable:
            pass


class Student:
    pass


def test1_2_iter():
    """
    (неактуальная функция) Запускает 4 теста на итерируемость для 4 типов данных, размер структур указывается в sizik
    :return: None
    """
    sizik = 100_000

    listik = [i for i in range(sizik)]
    tuplik = tuple(listik)
    setik = set(listik)
    frzsetik = frozenset(listik)

    start_time = timeit.default_timer()
    test_iterating(listik)
    print(f'list iterations: {timeit.default_timer() - start_time}')

    start_time = timeit.default_timer()
    test_iterating(tuplik)
    print(f'tuple iterations: {timeit.default_timer() - start_time}')

    start_time = timeit.default_timer()
    test_iterating(setik)
    print(f'set iterations: {timeit.default_timer() - start_time}')

    start_time = timeit.default_timer()
    test_iterating(frzsetik)
    print(f'frozenset iterations: {timeit.default_timer() - start_time}')

    pass


def test1_helper_iter(function, iterable, struct_size, iterations):
    """
    Отдельная функция для тестировки iterable, понижение точности из-за этого не замечено
    :param function: функция, которую нужно запустить в тесте
    :param iterable: обьект, по которому можно проитерироваться
    :param struct_size: размер обьекта (используется только для print'а)
    :param iterations: кол-во прогонов теста
    :return: None
    """
    times = []
    for i in range(iterations):
        start_time = timeit.default_timer()
        function(iterable)
        times.append(timeit.default_timer() - start_time)
    avg = sum(times) / iterations
    print(
        'Среднее значение для {0:20} размером {1}:\t{2:.10f}, кол-во итераций: {3}'.format(
            str(type(iterable)), struct_size, avg, iterations))
    pass


def test1_iter():
    """
    Запускает серию тестов для 4 типов данных, с заданием размера самих структур и кол-вом повторений тестов
    :return: None
    """
    sizik = 100_000
    data_types = []

    listik = [i for i in range(sizik)]
    tuplik = tuple(listik)
    setik = set(listik)
    frzsetik = frozenset(listik)

    data_types.append(listik)
    data_types.append(tuplik)
    data_types.append(setik)
    data_types.append(frzsetik)

    iterations = 1000
    print(
        'Для таких подряд идущих тестов (1000 итераций, размер структур 100_000), на моём ПК, погрешность составляет '
        '~ +-10^-5 ')

    print('\nТестирование на итерируемость:')
    f = test_iterating
    for dtype in data_types:
        test1_helper_iter(f, dtype, sizik, iterations)

    print('\nТестирование на поиск элемента:')
    f = test_lookups
    for dtype in data_types:
        test1_helper_iter(f, dtype, sizik, iterations)

    print('\nРазмеры для каждого обьекта (в байтах):')
    for dtype in data_types:
        print(type(dtype), ': ', sys.getsizeof(dtype))

    pass


if __name__ == '__main__':
    test1_iter()
    # test1_2_iter()

    # Выводы:
    # итерироваться по set и frozenset слегка медленнее;
    # Поиск элемента в set и frozenset существенно быстрее (на 2 порядка для моей конфигурации)
    # Обьем памяти, занятой set и frozenset, существенно больше, чем у list и tuple (в 5 раз для моей конфигурации)

    # Для ручного тестирования:
    # sizik = 100_000

    # listik = [i for i in range(sizik)]
    # test1_helper_iter(listik, sizik, 1000)
    pass

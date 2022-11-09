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
    Запускает 4 теста для 4 типов данных, размер структур указывается в sizik
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


def dcrtor_test1(function):
    def _wrapper(iterable, struct_size, iterations):
        times = []
        for i in range(iterations):
            start_time = timeit.default_timer()
            test_iterating(iterable)
            function(iterable, struct_size, iterations)
            times.append(timeit.default_timer() - start_time)
        avg = sum(times) / iterations
        print(
            'Среднее значение для {0:20} размером {1}:\t{2}, кол-во итераций: {3}'.format(
                str(type(iterable)), struct_size, avg, iterations))


    return _wrapper


@dcrtor_test1
def test1_helper_iter(iterable, struct_size, iterations):
    """
    Отдельная функция для тестировки iterable, понижение точности из-за этого не замечено
    :param iterable: обьект, по которому можно проитерироваться
    :param struct_size: размер обьекта (используется только для print'а)
    :param iterations: кол-во прогонов теста
    :return: None
    """

    pass


def test1_iter():
    """
    Запускает серию тестов для 4 типов данных, с заданием размера самих структур и кол-ва повторений тестов
    :return: None
    """
    sizik = 100_000

    listik = [i for i in range(sizik)]
    tuplik = tuple(listik)
    setik = set(listik)
    frzsetik = frozenset(listik)

    iterations = 1000
    print(
        'Для таких подряд идущих тестов (1000 итераций, размер структур 100_000), на моём ПК, погрешность составляет '
        '~ +-10^-5 ')

    test1_helper_iter(listik, sizik, iterations)
    test1_helper_iter(tuplik, sizik, iterations)
    test1_helper_iter(setik, sizik, iterations)
    test1_helper_iter(frzsetik, sizik, iterations)

    pass


if __name__ == '__main__':
    test1_iter()
    # test1_2_iter()
    # Вывод: итерироваться по set и frozenset слегка медленнее
    # sizik = 100_000

    # listik = [i for i in range(sizik)]
    # test1_helper_iter(listik, sizik, 1000)
    pass

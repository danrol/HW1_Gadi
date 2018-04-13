import heapq
import functools


def upper_half(matrix):
    if matrix is []:
        return []
    for i_index, i in enumerate(matrix):
        for j_index, j in enumerate(i):
            if j_index < i_index:
                matrix[i_index][j_index] = None
                continue
            break
    return matrix


def encrypt(string, key=1):
    size_alphabet = 26
    encrypted = ''
    for i in string:
        encrypted += chr(ord('a') + (((ord(i) + (key % size_alphabet)) - ord('a')) % size_alphabet))
    return encrypted


def assure_positive(num):
    if num < 0:
        return num * -1
    else:
        return num


def sum_digits1(n):
    sum_n = 0
    n = assure_positive(n)

    while n != 0:
        sum_n += n % 10
        n //= 10
    return sum_n


def sum_digits2(n):
    n = assure_positive(n)

    return sum(int(ch) for ch in str(n))


def flatten(alist):
    reduced_list = functools.reduce(list.__add__, alist)
    return reduced_list


def dijkstra(graph, weights, source):
    pass


# start tests


def test_upper_half():
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 'spam'], [11, 12, 13, 14, 15], [16, 'stam', 18, 19, 20]]
    assert (upper_half([]) == [])
    assert (upper_half(matrix) ==
            [[1, 2, 3, 4, 5], [None, 7, 8, 9, 'spam'], [None, None, 13, 14, 15], [None, None, None, 19, 20]])


def test_encrypt():
    assert (encrypt("spam") == "tqbn")
    assert (encrypt("spaz") == "tqba")
    assert (encrypt("spam", 3) == "vsdp")


def test_sum_digits1():
    assert (sum_digits1(-1492) == 16)
    assert (sum_digits1(1493) == 17)
    assert (sum_digits1(0) == 0)


def test_sumdigits2():
    test_sum_digits1()


def test_flatten():
    assert (flatten([[1, 2, 3], ['foo', 'bar'], [], [[1, 2], [3]]]) == [1, 2, 3, 'foo', 'bar', [1, 2], [3]])


def test_dijkstra():
    graph = {'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': ['c', 'e'], 'e': [], 'f': ['e']}
    weights = {('a', 'b'): 2, ('a', 'c'): 10, ('b', 'd'): 3, ('d', 'c'): 1, ('d', 'e'): 12, ('f', 'e'): 0}
    # assert (dijkstra(graph, weights, 'a') == {'a': 0, 'b': 2, 'c': 6, 'd': 5, 'e': 17, 'f': 'infinity'})
    pass
    # TODO Complete 5 and remove comments


if __name__ == "__main__":
    test_upper_half()
    test_encrypt()
    test_sum_digits1()
    test_sumdigits2()
    test_flatten()
    test_dijkstra()

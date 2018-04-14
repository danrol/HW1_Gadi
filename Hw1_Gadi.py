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
    INFINITY = 1000000
    weights_from_source = init_heap(graph)
    for node in graph.keys():
        node_tuple = weights_from_source.remove(node)
        node_tuple.weight = shortest_path_from_source(find_all_paths(graph, source, node), weights)
        weights_from_source.

    return weights_from_source


def shortest_path_from_source(path_list, weights):
    INFINITY = 1000000
    min_path = INFINITY
    for path in path_list:
        current_path_length = 0
        for index in (len(path)-1):
            current_path_length += weights.get((path(index), path(index+1)))
        if current_path_length < min_path:
            min_path = current_path_length
    if min_path >= 1000000:
        return 'infinity'
    return min_path


def init_heap(graph):
    init_list = []
    for node in graph:
        init_list.append((node, 0))
    heapq.heapify(init_list)
    return init_list


def find_all_paths(self, graph, start_vertex, end_vertex):
    """ find all paths from start_vertex to
        end_vertex in graph """
    path = []
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return [path]
    if start_vertex not in graph.keys():
        return []
    paths = []
    for next_nodes in graph[start_vertex]:
        for vertex in next_nodes:
            if vertex not in path:
                extended_paths = self.find_all_paths(graph, vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
    return paths


# start tests


def test_upper_half():
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 'spam'], [11, 12, 13, 14, 15], [16, 'stam', 18, 19, 20]]
    assert (upper_half([]) == [])
    assert (upper_half(matrix) == [[1, 2, 3, 4, 5], [None, 7, 8, 9, 'spam'], [None, None, 13, 14, 15], [None, None, None, 19, 20]])


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
    assert (dijkstra(graph, weights, 'a') == {'a': 0, 'b': 2, 'c': 6, 'd': 5, 'e': 17, 'f': 'infinity'})


if __name__ == "__main__":
    test_upper_half()
    test_encrypt()
    test_sum_digits1()
    test_sumdigits2()
    test_flatten()
    test_dijkstra()

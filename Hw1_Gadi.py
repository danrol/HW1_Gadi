import heapq

def upper_half(matrix):
    if matrix == []:
        return []
    for i_index, i in enumerate(matrix):
        for j_index, j in enumerate(i):
            if j_index<i_index:
                matrix[i_index][j_index] = None
                continue
            break
    return matrix

def encrypt(string, key=1):
    sizeAlphabet = 26
    encrypted = ''
    for i in string:
        encrypted += chr(ord('a') + (((ord(i)+(key % sizeAlphabet)) - ord('a')) % sizeAlphabet))
    return encrypted

def assure_positive(num):
    if num < 0:
        return num*-1
    else:
        return num

def sum_digits1(n):
    sum = 0
    n = assure_positive(n)

    while n != 0:
        sum += n%10
        n //= 10
    return sum

def sum_digits2(n):
    n = assure_positive()

    return sum(int(ch) for ch in str(n))

def dijkstra(graph, weights, source):
    pass


def test_upper_half():
    matrix = [[1,2,3,4,5], [6,7,8,9,'spam'], [11,12,13,14,15], [16,'stam', 18, 19, 20]]
    assert(upper_half([]) == [])
    assert(upper_half(matrix) ==
           [[1, 2, 3, 4, 5], [None, 7, 8, 9, 'spam'], [None, None, 13, 14, 15], [None, None, None, 19, 20]])

def test_encrypt():
    assert (encrypt("spam") == "tqbn")
    assert (encrypt("spaz") == "tqba")
    assert (encrypt("spam", 3) == "vsdp")

def test_sum_digits1():
    assert(sum_digits1(-1492) == 16)
    assert(sum_digits1(1493) == 17)
    assert(sum_digits1(0) == 0)

def test_sumdigits2():
    test_sum_digits1()

if __name__ == "__main__":
    test_upper_half()
    test_encrypt()
    test_sum_digits1()
    test_sumdigits2()

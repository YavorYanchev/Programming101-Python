# from firstday import to_digits, palindrome,char_histogram
# --------------------------


def to_digits(n):
    new_list = []
    for index in str(n):
        new_list.append(int(index))
    return new_list


def palindrome(obj):
    return str(obj) == str(obj)[::-1]


def char_histogram(string):
    new_dict = {}
    for x in string:
        if x not in new_dict:
            new_dict[x] = string.count(x)
    return new_dict
# --------------------------


def is_number_balanced(n):
    digits = to_digits(n)
    middle = len(digits) // 2
    left_digits = digits[0:middle]
    if len(digits) % 2:
        right_digits = digits[middle + 1:]
    else:
        right_digits = digits[middle:]
    return sum(left_digits) == sum(right_digits)


def is_increasing(seq):
    for x in range(0, len(seq) - 1):
        if seq[x] >= seq[x+1]:
            return False
    return True


def is_decreasing(seq):
    for x in range(0, len(seq) - 1):
        if seq[x] <= seq[x+1]:
            return False
    return True


def get_largest_palindrome(n):
    n -= 1
    while palindrome(n) is not True:
        n = n - 1
    return n


def prime_numbers(n):
    primes = [x for x in range(2, n+1)]
    number = 2
    while number < n:
        for x in range(2, n+1):
            if number * x in primes:
                primes.remove(number * x)
        number += 1
    return primes


def is_anagram(a, b):
    a, b = a.lower(), b.lower()
    return (char_histogram(a) == char_histogram(b))


def birthday_ranges(birthdays, ranges):
    result = []
    for tuples in ranges:
        count = 0
        for birthday in birthdays:
            if birthday >= tuples[0] and birthday <= tuples[1]:
                count += 1
        result.append(count)
    return result


def sum_matrix(m):
    total = 0
    for rows in m:
        total += sum(rows)
    return total


def check_matrix(matrix_length, i, j):
    if i < 0:
        return False
    if j < 0:
        return False
    if i >= matrix_length:
        return False
    if j >= matrix_length:
        return False
    return True


def neighbours(i, j):
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list_neighbours = []
    matrix_length = len(m)
    if(check_matrix(matrix_length, i-1, j-1)):
        list_neighbours.append(m[i-1][j-1])
    if(check_matrix(matrix_length, i-1, j)):
        list_neighbours.append(m[i-1][j])
    if(check_matrix(matrix_length, i-1, j+1)):
        list_neighbours.append(m[i-1][j+1])
    if(check_matrix(matrix_length, i, j-1)):
        list_neighbours.append(m[i][j-1])
    if(check_matrix(matrix_length, i, j+1)):
        list_neighbours.append(m[i][j+1])
    if(check_matrix(matrix_length, i+1, j-1)):
        list_neighbours.append(m[i+1][j-1])
    if(check_matrix(matrix_length, i+1, j)):
        list_neighbours.append(m[i+1][j])
    if(check_matrix(matrix_length, i+1, j+1)):
        list_neighbours.append(m[i+1][j+1])
    return list_neighbours

def neighbours_after_bomb(neigh_arr, index_bomb):
    after_bomb = []
    for i in neigh_arr:
        if i <= index_bomb:
            after_bomb.append(0)
        else:
            after_bomb.append(i - index_bomb)
    return sum(after_bomb)


def matrix_bombing_plan(m):
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    coordinates = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    dict_pos = {}
    dict_bomb = {}
    br = 0
    for index in coordinates:
        matrix_sum = 0
        br += 1
        dict_pos[index] = br
        matrix_sum = sum_matrix(m)
        row_index = index[0]
        col_index = index[1]
        neigh_list = neighbours(row_index, col_index)
        neigh_list_bomb = neighbours_after_bomb(neigh_list, br)
        dict_bomb[index] = matrix_sum -sum(neigh_list) + neigh_list_bomb
    return(dict_bomb)


# print(matrix_bombing_plan(2))


def is_transversal(transversal, family):
    family_copy = [False for el in family]
    for x in transversal:
        grp_num = -1
        for group in family:
            grp_num += 1
            for i in group:
                if i == x:
                    family_copy[grp_num] = True
    return all(family_copy)

# print(is_transversal([4, 5, 6], [[5, 7, 9], [1, 4, 3], [2, 6]]))
# print(is_transversal([1, 2], [[1, 5], [2, 3], [4, 7]]))
# print(is_transversal([2, 3, 4], [[1, 7], [2, 3, 5], [4, 8]]))

def sum_of_digits(n):
    return sum([int(i) for i in str(n) if i != "-"])


def to_digits(n):
    return [int(i) for i in str(n)]


def to_number(digits):
    return int(''.join(map(str, digits)))


def fact_digits(n):
    total = 0
    for index in str(n):
        fact = 1
        for x in range(1, int(index)+1):
            fact *= x
        total += fact

    return total


def fibonacci(n):
    fib_list = []
    first_elem, second_elem = 1, 1
    while(len(fib_list) < n):
        fib_list.append(first_elem)
        first_elem, second_elem = second_elem, first_elem + second_elem
    return fib_list


def fib_number(n):
    return to_number(fibonacci(n))


def palindrome(n):
    return (str(n) == str(n)[::-1])


def count_vowels(string):
    total = 0
    for x in string.lower():
        if x in "aeyuio":
            total += 1
    return total


def count_consonants(string):
    total = 0
    for x in string.lower():
        if x in "bcdfghjklmnpqrstvwxz":
            total += 1
    return total


def char_histogram(string):
    new_dict = {}
    for x in string:
        if x not in new_dict:
            new_dict[x] = string.count(x)
    return new_dict

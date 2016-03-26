def count_words(arr):
    dct = {}
    for x in arr:
        dct[x] = arr.count(x) 
    return dct


def nan_expand(n):
    not_a = "Not a "
    str_not_a = ""
    for x in range(n):
        str_not_a += not_a
    if str_not_a == '':
        return str_not_a
    return str_not_a + "NaN"
# print(nan_expand(0))


def iterations_of_nan_expand(text):
    not_a = "Not a "
    nan = "NaN"
    str_not_a = ""
    iterations = text.count(not_a)
    if not_a not in text or nan not in text:
        return False
    return iterations

counter = 0
list_count = []


def take_same(items):
    first = items[0]
    counter = 0
    index = 1
    n = len(items)
    result = [first]
    while index < n and first == items[index]:
        result.append(items[index])
        index += 1
        counter += 1
    list_count.append(counter)
    return result


def group(items):
    total = []
    while(len(items) != 0):
        current_group = take_same(items)
        total.append(current_group)
        items = items[len(current_group):]
    # print(len(list_count))
    return total

# print(group([1, 2, 3, 3, 3, 3, 4, 3, 3]))


def max_consecutive(items):
    grouped = group(items)
    return max([len(x) for x in grouped])

# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))


def sum_of_numbers(string):
    arr_numbers = string
    for index in arr_numbers:
        if index not in "1234567890":
            arr_numbers = arr_numbers.replace(index, " ")
    arr_numbers = arr_numbers.split()
    for index in range(0, len(arr_numbers)):
        arr_numbers[index] = int(arr_numbers[index])
    return sum(arr_numbers)


def gas_stations(distance, tank_size, stations):
    smart_stations = []
    current_distance = 0
    while current_distance < distance:
        current_distance += tank_size
        for x in reversed(stations):
             if current_distance > x:
                smart_stations.append(x)
                current_distance = x
                # print(current_distance)
                if current_distance == stations[-1]:
                    if current_distance + tank_size > distance:
                        return smart_stations
                break

# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))


NUMBERS = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " "
}


def numbers_to_message(pressed_sequence):
    result = ""
    upper_case = False
    grouped_sequence = group(pressed_sequence)
    for grp in grouped_sequence:
        if grp[0] == 1:
            upper_case = True
            continue
        if grp[0] == -1:
            continue
        times_pressed = len(grp)
        number_letters = NUMBERS[grp[0]]
        selected_letter_index = times_pressed % len(number_letters) - 1
        letter = number_letters[selected_letter_index]
        if upper_case:
            result += letter.upper()
            upper_case = False
        else:
            result += letter
    return result

# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def message_to_numbers(message):
    numbers = []
    numbers_sequence = []
    num_seq_index = -1

    for i in message:
        if i.isupper():
            numbers.append(1)
        if i is " ":
            numbers.append(0)
            continue
        for key in NUMBERS:
            i = i.lower()
            if i in NUMBERS[key]:
                times_to_press = NUMBERS[key].index(i) + 1
                keys_to_hit = [key] * times_to_press
                num_seq_index += 1
                numbers_sequence += [key]
                if (num_seq_index > 0 and (numbers_sequence[num_seq_index - 1] == numbers_sequence[num_seq_index])):
                     numbers.append(-1)
                numbers += keys_to_hit
    return numbers

# print(message_to_numbers("abc"))
# print(message_to_numbers("Ivo e Panda"))

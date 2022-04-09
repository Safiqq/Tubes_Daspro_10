def length(var):
    count = 0
    for i in var:
        count += 1
    return count

# def replace(sentence, word):
#     new_word = ""
#     count = 0
#     count_2 = 0
#     for i in sentence:
#         if i == word[0]:
#             if length(word) + count <= length(sentence):
#                 count_2 += 1
#         else:
#             print(i, count_2)
#             if count_2 < length(word):
#                 new_word += i
#             elif count_2 == length(word):
#                 count_2 = 0
#         count += 1
#     return new_word

def maximum(array):
    # Asumsi length(array) > 0
    # Definisi value
    value = 0
    for i in range(length(array)):
        if i == 0:
            value = array[i]
        else:
            if value < array[i]:
                value = array[i]
    return value

def minimum(array):
    # Asumsi length(array) > 0
    # Definisi value
    value = 0
    for i in range(length(array)):
        if i == 0:
            value = array[i]
        else:
            if value > array[i]:
                value = array[i]
    return value

# Array
def konkat(array_1, array_2):
    count = length(array_1) + length(array_2)
    new_array = ["" for i in range(count)]
    for i in range(length(array_1)):
        new_array[i] = array_1[i]
    for j in range(length(array_2)):
        new_array[j + length(array_1)] = array_2[j]
    return new_array

def append(array, elements):
    count = length(array)
    new_array = ["" for i in range(count + 1)]
    try:
        for i in range(count):
            new_array[i] = array[i]
        new_array[count] = elements
        return new_array
    except:
        count_2 = length(elements)
        new_array[count] = ["" for i in range(count_2)]
        for i in range(count):
            new_array[i] = array[i]
        for j in range(count_2):
            new_array[count][j] = elements[j]
        return new_array

def copy(array):
    return array

def reverse(array):
    count = length(array)
    new_array = ["" for i in range(count)]
    for i in range(count):
        new_array[count-i-1] = array[i]
    return new_array

def remove(array, element, number=1):
    count = length(array)
    new_array = []
    for i in range(count):
        if array[i] != element:
            new_array = append(new_array, array[i])
        else:
            if number > 0:
                number = number - 1
            else:
                new_array = append(new_array, array[i])
    return new_array

def split(string, element):
    new_array = []
    new_word = ""
    string = string + element
    for i in string:
        if i == element:
            new_array = append(new_array, new_word)
            new_word = ""
        else:
            new_word += i
    return new_array

def sort(array, x="a"):
    # a : ascending
    # d : descending
    count = length(array)
    new_array = ["" for i in range(count)]
    if x == "a":
        for i in range(count):
            element = minimum(array)
            array = remove(array, element)
            new_array[i] = element
        return new_array
    elif x == "d":
        for i in range(count):
            element = maximum(array)
            array = remove(array, element)
            new_array[i] = element
        return new_array

# a = sort([5,6,2,3,4,2], "d")
# print(a)
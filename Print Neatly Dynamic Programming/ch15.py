import math
INFINITY = float('inf')

cost_matrix = []
cost_array = []
word_length = []
path_array = []
maxWidth = 0
noofwords = 0
words_array = []


def calculate_word_length(words):
    for word in words:
        word_length.append(len(word))


def print_neatly(words, M):
    global noofwords
    global maxWidth
    global cost_matrix
    global cost_array
    global word_length
    global path_array
    global words_array

    noofwords = len(words)
    maxWidth = M
    cost_matrix = [[0 for j in range(noofwords)]for i in range(noofwords)]
    cost_array = [0 for j in range(noofwords)]
    word_length = []
    path_array = [0 for j in range(noofwords)]
    words_array = words

    calculate_word_length(words)
    build_cost_matrix()

    i = j = noofwords-1

    for i in reversed(range(noofwords)):
        j = noofwords - 1
        min_cost = cost_matrix[i][j]
        min_index = j
        if cost_matrix[i][j] is not INFINITY:
            cost_array[i] = cost_matrix[i][j]
            path_array[i] = j + 1
        else:
            while j > i:
                if cost_matrix[i][j-1] is not INFINITY:
                    temp_cost = cost_array[j] + cost_matrix[i][j-1]

                    if min_cost > temp_cost:
                        min_cost = temp_cost
                        min_index = j
                    j -= 1
                else:
                    j -= 1

            cost_array[i] = min_cost
            path_array[i] = min_index
    string_text = string_builder()
    return cost_array, string_text


def build_cost_matrix():
    for i in range(noofwords):
        for j in range(i, noofwords):
            if i != j:
                if cost_matrix[i][j-1] != INFINITY:
                    sub_total_length = maxWidth - int(math.sqrt(cost_matrix[i][j-1]))
                    total_length = word_length[j] + sub_total_length + 1
                    empty_space = maxWidth - total_length
                else:
                    empty_space = -1
            else:
                total_length = word_length[j]
                empty_space = maxWidth - total_length

            if empty_space < 0:
                cost_matrix[i][j] = INFINITY
            else:
                cost_matrix[i][j] = empty_space * empty_space


def string_builder():
    stringer = ''
    i = 0
    while i < noofwords:
        end_index = path_array[i]
        for j in range(i, end_index):
            stringer += words_array[j]
            if j < end_index-1:
                stringer += ' '
        i = path_array[i]
        if i < noofwords:
            stringer += '\n'
    return stringer

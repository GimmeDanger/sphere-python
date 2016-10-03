import math
import string
import pandas as pd
import numpy as np


def tf(word, text):
    # text - list of strings
    return text.count(word) / float(len(text))


def idf(word, text_list):
    # text_list - list of lists
    n = 0
    for text in text_list:
        if word in text:
            n += 1
    if n:
        return math.log10(1 + len(text_list) / float(n))
    else:
        return math.log10(len(text_list))


def tf_idf(string_list, stop_words):
    text_list = []
    words_set = set()
    for line in string_list:
        text = string.split(line, ' ')
        for word in text:
            if word in stop_words:
                text.remove(word)
        text_list.append(text)
        words_set.update(text)

    result = np.zeros((len(words_set), len(text_list)))

    i = 0

    for word in words_set:
        word_idf = idf(word, text_list)
        j = 0
        for text in text_list:
            word_tf = tf(word, text)
            result[i][j] = word_tf * word_idf
            j += 1
        i += 1

    list_of_text_names = []
    for i in range(len(text_list)):
        list_of_text_names.append('text{0}'.format(i + 1))


    res_df = pd.DataFrame(result, index=list(words_set), columns=list_of_text_names)

    print result
    print res_df
    return result


tf_idf(['why is hello world the first program', 'because hello hello hello'], [])
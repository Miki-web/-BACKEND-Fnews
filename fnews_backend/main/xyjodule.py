import re
import string
import pandas as pd


csv_files = {'politic': 'main/politics_key_words.csv',
             'sport': 'main/sport_key_words.csv',
             'economic': 'main/economic_key_words.csv',
             'culture': 'main/culture_key_words.csv'}

politics_df = pd.read_csv(csv_files['politic'], index_col=0)
sport_df = pd.read_csv(csv_files['sport'], index_col=0)
economic_df = pd.read_csv(csv_files['economic'], index_col=0)
culture_df = pd.read_csv(csv_files['culture'], index_col=0)


def clean_sentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]
    sentence = [word for word in sentence if len(word) > 2]
    return sentence


def clean_input(content):
    content = re.sub('\n|\.|,', '', content)
    sentences = content.split('. ')
    foo = []
    for sentence in sentences:
        foo += clean_sentence(sentence)
    return foo


def get_words_freq(words):
    foo = {}
    for word in words:
        if word in foo:
            foo[word] += 1
        else:
            foo[word] = 1
    sorted1 = {k: v for k, v in sorted(foo.items(), key=lambda item: item[1], reverse=True)}
    return sorted1


def get_words(text):
    key_words = {}
    content = clean_input(text.lower())
    words_freq = get_words_freq(content)
    for i in range(len(words_freq.keys())):
        if list(words_freq.keys())[i] not in key_words:
            key_words[list(words_freq.keys())[i]] = words_freq[list(words_freq.keys())[i]]
        else:
            key_words[list(words_freq.keys())[i]] += words_freq[list(words_freq.keys())[i]]
    key_words = {k: v for k, v in sorted(key_words.items(), key=lambda item: item[1], reverse=True)}
    return key_words


def predict(text):
    cat = 'Інше'
    words = get_words(text)
    for t in words.keys():
        if t in politics_df.index:
            cat = 'Політика'
            break
        if t in sport_df.index:
            cat = 'Спорт'
            break
        if t in economic_df:
            cat = 'Економіка'
            break
        if t in culture_df.index:
            cat = 'Культура'
            break
    return cat

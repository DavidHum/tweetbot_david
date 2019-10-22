"""
Modulo que toma un libro de project guttenber y remueve las primeras lineas
para su posterior uso.

Tomato de: https://inzaniak.github.io/pybistuffblog/posts/2017/04/26/python-markovify.html

"""
import markovify

PATH_DATA = '/home/david/tweetbot/data/El Gaucho Martín Fierro.txt'

def get_index(in_list, in_string):
    """
    funcion para tomar los indices de palabras especificas en un texto

    """
    for num, row in enumerate(in_list):
        if in_string in row:
            return num

def clean_book(path):
    """
    funcion para tomar limpiar textos de guttenberg

    """
    book = open(path, 'r').read()
    rows = book.split('\n')
    start_idx = get_index(rows, '*** START')
    end_idx = get_index(rows, '*** END')
    rows = rows[start_idx + 1:end_idx]
    text = '\n'.join([r for r in rows if r != ''])
    return text

TEXTO = clean_book(PATH_DATA)

# modelo markov

GAUCHO_MODEL = markovify.Text(TEXTO)

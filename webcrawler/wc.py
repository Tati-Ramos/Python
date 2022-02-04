import requests #requisação HTTP
from bs4 import BeautifulSoup #extração de dados de arquivos HTML e XML
import operator #+ - * / not, and, or, etc
from collections import Counter #tuplas, dicionários e listas

def start(url):  #start um url

    wordlist = [] #lista vazia #armazena o conteudo da url
    source_code = requests.get(url).text


    soup = BeautifulSoup(source_code, 'html.parser') # requisição do dados da url e transforma em html


    # Text in given web-page is stored under
    # The <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text # transforma em string

        words = content.lower().split() # letras minusculas e cortar o conteúdo

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist): #vai remover simbolos
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%¨¨&*(){}/*+><:<:<%'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}
    # vai fazer uma contagem de palavras mais recorrentes
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    for key, value in sorted(word_count.items(),
                            key = operator.itemgetter(1)):
        print ("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10) # top 10 com as palavras mais usadas
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")

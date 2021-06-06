import re
import unidecode
import bs4
import requests
from bs4 import BeautifulSoup as soup

#-------------questão 1
#a
def count_digits(lista):
    count = 0;
    for y in lista:
        for g in str(y):
            count = count +1
    return count        

#b

def id_palindrome(word):
    word = unidecode.unidecode(word)
    s = re.sub(r' ','',word)
    s = re.sub(r'[^a-zA-Z0-9]+','',word)
    s = s.lower()
    i = 0;
    j = len(s)-1
    while i <= j:
        if s[i]!=s[j]:
            return False
        i = i+1
        j = j-1    
    return True

#--------------Questão 2

def words_tag(text):
    g = text.split(' ')
    p = dict()
    
    for j in g:
        k = j.split('/')
        if p.get(k[0],0) == 0:
            f = dict()
            f["Numero"] = p.get(k[0],0) +1
        else: 
            f=p[k[0]]    
            f["Numero"] += 1
        i = 1;
        for h in k:
            if i%2==0:
                f[h] = f.get(h,0)+1 
            i += 1   
        p[k[0]] = f  
    for l in p:
        ss = ""
        for f,d in p[l].items():
            if ss == "":
                ss += l +" ("+str(d)+"):"
            else :
                ss += f +" ("+str(d)+"),"   
        
        print(ss[:-1]+"\n")

#--------------Questão 3

#a
def calc_trigrams(text):
    text = text.lower()
    trigrams = [text[i:i+3] for i in range(len(text)-(2))]
    print(len(trigrams))
    return(len(trigrams))
#b

def fix_word(word):
    print(word)   


##-------------questão 6


def previsaoSemanal(distrito, concelho):

    requestLink = "https://www.ipma.pt/pt/otempo/prev.localidade.hora/#" + distrito + "&" + concelho

    response = requests.get(requestLink).content

    soup_page = soup(response, 'html.parser')
    div = soup_page.find('div',id='daily')
    print(div)


if __name__ == "__main__":
    #print(count_digits([1,5,14,28,1000]))  
    #print(id_palindrome("SPLN"))  
    #calc_trigrams('univer%idade')
    previsaoSemanal("Braga","Vila Verde")
    #words_tag("Eu/PROPESS nunca/ADV almoço/V almoço/V à/PREP+ART hora/N do/KS almoço/N ./.")
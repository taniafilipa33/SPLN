
import unidecode
import re
#----------Questão 1
#a
def sum_next_is_10(lista):
    i = 0
    p = []
    while i <len(lista) -1:
        if(lista[i]+lista[i+1] == 10):
            p.append(lista[i])
        i += 1    
    print(p)        
#b

def is_pangram(frase1,alfabeto):
    text = unidecode.unidecode(frase1)   
    h =  text.lower()
    j = h.replace(' ','')
    g = re.sub('[^A-Za-z0-9]+', '', j)
    print(g)
    for f in g:
        print(f)
        if f not in alfabeto:
            return False
    return True

#------------ Questão 2
def 

if __name__ == "__main__" :
    #sum_next_is_10([1, 5, 7, 3, 6, 4, 8, 2, 10, 0, 3])    
    #print(is_pangram("Blitz prênde ex-vesgo com cheque fajuto.","akibjhjgf"))
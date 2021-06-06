import re


# teste de 18 de janeiro de 2019

#------------------- questão 1
#a
def max_diff(list):
    guarda=-1
    for i in list:
        for j in list:
            guarda = max(guarda , i-j)

    return guarda        
#b
def dic(strg):
    di = dict()
    for caract in strg:
        di[caract] = di.get(caract,0) +1
    return di    

#-----------------Questao 2

def fix_lines(strg):
    text = re.sub(r"\n(?!\n)", r" ", strg)
    return text

#-----------------Questão 3

def fix_sent_start(a):
  
    return '. '.join(map(lambda s: s.strip().capitalize(), a.split('.')))
    
#-----------------Questão 4
#a
def qes4(nome,dic,lista):
    palavras = []
    for g in lista:
        j =g.split(' ')
        i=0
        while i<len(j):
            if j[i]==nome:
                h = i-5
                n= 0
                st = ""
                while n < 10 & h<len(j):                    
                    if h> 0:
                        st = st +" "+ j[h]
                        n=n+1
                        h=h+1
                    else: 
                        h=0 
                        st = st +" "+ j[h]
                        n=n+1
                        h=h+1 
                print("st: "+st)         
                palavras.append(st)          
            i=i+1  

    return palavras

#--------------questao 5

def find_corresp(t1,t2):
    i = 0;
    dic = dict()
    g = t1.split(' ')
    h = t2.split(' ')
    while i < min(len(g),len(h)):
        if g[i] != h[i]:
            dic[g[i]] = h[i]
        i = i+1    
    return dic


if __name__ == "__main__":
    #print(max_diff([1,1,3,5,3]))
    #print(dic("TESTE DE SPLN"))
    print(fix_sent_start("ele mesmo costumava dizer que \n era simplesmente um egoísta: mas \n nunca, como agora na velhice, as \n generosidades do seu coração ti- \n nham sido tão profundas e largas. \n\n parte do seu rendimento ia-se- \n -lhe por entre os dedos, espar- \n samente. numa caridade enterne- \n cida."))
    #print(qes4("carlos",{},["isto esta minado O carlos foi à venda. AI foi?", " a Ana maria não quer nada com ele , mas visto que o carlos até tenta pode ser que tenha sorte"] ))
    #print(find_corresp("As inundações provocaram graves damnos na pharmácia. [...]", "As inundações provocaram graves danos na farmácia. [...]" ))
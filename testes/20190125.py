#------------questão 1

#b

def f(lis1,lis2):
    i =0 
    p = []
    while i<min(len(lis1),len(lis2)):
        t1 = (lis1[i],lis2[i],lis2[i]+lis1[i])
        p.append(t1)
        i = i+1
    return p

#c
def dic(strg):
    di = dict()
    i = 0
    while i < len(strg)-1:
        di[strg[i]+strg[i+1]] = di.get(strg[i]+strg[i+1],0) +1
        i = i+1
    return di   


if __name__ == "__main__":
    #print(f([1,3,5],[3,4,5]))
    #print(dic('TESTE DE SPLN'))

#c'est pour l'exercice 53 de hachage ça
def hachage53(k):
    return k%9

def chaine53(m):
    Chaine=[]
    for k in range(m):
        Chaine.append([])
    return Chaine


def ajout53(k,chaine):
    chaine[hachage53(k)].append(k)

table53=chaine53(9)
Listetest53=[5,28,19,15,20,33,12,17,10]
#for k in range(9):
#    ajout53(Listetest53[k],table53)
#print(table53)


#maintenant l'exercice 54

Liste54=[10,22,31,4,15,28,17,88,59]

def sondagelin54(k,i,m):
    return (k+i)%m
def sondagequad54(k,i,m):
    return (k+i+3*i*i)%m
def sondagedoubl54(k,i,m):
    return (k+ i*(1+(k%(m-1))))%m

def hachage54(k,m):      #dans l'exercice le prof ne spécifie pas
    return k%m           #une fonction de hachage précise, sorry

def chaine54(m):
    resultat=[]
    for k in range(m):
        resultat.append(-1)
    return resultat

def ajout54lin(k,m,table):
    r=hachage54(k,m)
    i=0
    if table[r]==-1:
        table[r]=k
    else:
        l=sondagelin54(k,0,m)
        while(table[l]!=-1 ):
            l=sondagelin54(k,i,m)
            i+=1
        table[l]=k
def ajout54doubl(k,m,table):
    r=hachage54(k,m)
    i=0
    if table[r]==-1:
        table[r]=k
    else:
        l=sondagedoubl54(k,0,m)
        while(table[l]!=-1 ):
            l=sondagedoubl54(k,i,m)
            i+=1
        table[l]=k

def ajout54quad(k,m,table):
    r=hachage54(k,m)
    i=0
    if table[r]==-1:
        table[r]=k
    else:
        l=sondagequad54(k,0,m)
        while(table[l]!=-1 ):
            l=sondagequad54(k,i,m)
            i+=1
        table[l]=k




table54lin=chaine54(11)
table54doubl=chaine54(11)
table54quad=chaine54(11)

#for k in range(9):
#    ajout54lin(Liste54[k],11,table54lin)
#    ajout54doubl(Liste54[k],11,table54doubl)
#    ajout54quad(Liste54[k],11,table54quad)
#print(table54lin)
#print(table54quad)
#print(table54doubl)

#maintenant c'est pour l'exercice 55


def sansaccent(lettre):
    if lettre=='é' or lettre=='è' or lettre=='ê':
        return 'e'
    if lettre=='à':
        return 'a'
    else:
        return lettre

def correspondant(lettre):
    return ord(sansaccent(lettre))-ord('a')

def hachage55_1(nom):
    n=nom.lower()
    return correspondant(n[0])

def hachage55_2(nom):
    n=nom.lower()
    return ( correspondant(n[0]) + correspondant(n[2]) )%26

nomspasfaits=["Jean-Marie","Joachim","John","José","Klaus-Dieter"]
for nom in nomspasfaits:
    print( nom + " h1:"+ str(hachage55_1(nom)) + " h2:"+ str(hachage55_2(nom)))

touslesnoms=["Alfio","Amel","Amin","Anthony","Antoine","Bernard","Boris","Charles","Denis","Diego","Dominique","Erik","Eva","Gérard","Hichem","Ian","Jacques","Jean-François","Jean-Marie","Joachim","John","José","Klaus-Dieter","Manuel","Marco","Michel","Otto","Peter","Philippe","Robert","Sacha","Stefan","Sylvain","Thomas","Todor"]

def chaine55(m):
    chaine=[]
    for k in range(m):
        chaine.append([])
    return chaine

def ajout55h1(nom,table):
    k=hachage55_1(nom)
    table[k].append(nom)

def ajout55h2(nom,table):
    k=hachage55_2(nom)
    table[k].append(nom)

table55h1=chaine55(26)
table55h2=chaine55(26)

for k in range(35):
    ajout55h1(touslesnoms[k],table55h1)
    ajout55h2(touslesnoms[k],table55h2)

print("La table de hachage en fonction de h1")
print(table55h1)
print()
print("La table de hachage en fonction de h2")
print(table55h2)

#erxrcice 
con=1
while con:
     n=int(input("donner num positif: ")) #demande a l'utilisateur un nomber positif
     if n>0 :
         con=0
n+=1 #pour inclure n dans la liste
#creation de la liste
l=list(range(n))
#affichage
print("touts: ",l) #affiche la liste
print("touts pire: ",l[0:-1:2]) #affiche les numbres paires
print("touts impaire: ",l[1:len(l):2]) #affiche les numbres impaires
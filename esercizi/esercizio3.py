controllo = True
lista = []


while controllo:
    rispostanumero=int(input("richiedi numero")) 
    lista.append(rispostanumero)
    risposta=input("vuoi continuare?")
    if(risposta=="si"):
         controllo=False
else: 
     controllo=False


    


for numeri in lista:
     print(numeri*2)
    
    
    
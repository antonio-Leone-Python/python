controllo = True
while controllo:
    numeroutente= int(input("richiedi numero"))
    for i in range(numeroutente,-1,-1):
        print(i)
    x=input("vuoi ricominciare?")
    if(x=="si"):
        controllo=True
    else:
        controllo=False




        
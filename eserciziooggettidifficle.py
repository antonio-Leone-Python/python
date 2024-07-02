import datetime
class Ristorante:                             #creo la classe ristorante
    menu={"pasta al pomodoro":"23 euro",
          "spaghetti allo scoglio":"22 euro",
          "ragu di anatra":"45 euro",
          "bistecca di vitello":"103 euro"}    
    
    def __init__(self,nome,cucina):  #il costruttore accetta due attributi
        self.nome=nome
        self.tipo_cucina=cucina
        

    def descrivi_ristorante(self):  #metodo che stampa una frase di presentazione del ristorante
        print(f"{self.nome}, {self.tipo_cucina} e non solo!")

    def stato_apetura(self): #metodo che stampa se il ristorante è aperto attualmente
        print("il ristorante è attualmente chiuso,riaprirà alle 20:00")    

    def apri_ristorante(self):      #indica se il ristorante è aperto o chiuso
        self.aperto=False
        if self.aperto == True:
            print("il ristorante è aperto") 
        else:
            print("il ristorante è chiuso")


    def aggiungi_al_menu(self):           #metodo che fa aggiungere prezzo e piatto al menu
        food=input("che piatto vuoi aggiungere?")
        cash=input("scrivi prezzo")
        self.menu[food]=cash


    def elimina_piatto(self):         # metodo che fa eliminare un piatto dal menu
        x=input("quale piatto vuoi eliminare")
        self.menu.pop(x)
        print("piatto rimosso con successo")


    def stampa_menu(self):     #fa stampare il menu
        print (self.menu)
            

x= Ristorante("da antonio","cucina mediterranea")    #ristorante 

x.aggiungi_al_menu()
x.descrivi_ristorante()
x.stato_apetura()
x.stampa_menu()
x.apri_ristorante()
x.elimina_piatto() 



class Cliente:
    
   

    def __initi__(self,ordine):
        self.ordine=ordine
       
    def ordine_cliente():
        lista=[]
        ord_cliente=input("seleziona cosa mangiare dal menu")
        menu2=Ristorante.menu
        lista.append(ord_cliente)
        print(lista)




Cliente.ordine_cliente()   

        





                   
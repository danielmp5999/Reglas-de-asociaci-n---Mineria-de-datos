def soporte(indice1, indice2, item1, item2):
    resul=item1/item2
    print("soporte(",palabras[indice1],"=>",palabras[indice2],") = " ,item1 ,"/",item2,"=","{:.2f}".format(resul),"\t",end=" ")

def confianza(indice1, indice2, item1, item2):
    resul=item1/item2
    print("confianza(",palabras[indice1],"=>",palabras[indice2],") = " ,item1 ,"/",item2,"=","{:.2f}".format(resul))

palabras = ["huevo", "aceite", "panales", "vino", "leche","manteq","soda"]

lista = [("huevo", "vino", "manteq","soda"),
        ("aceite","leche"),
        ("panales","leche"),
        ("aceite", "panales", "leche"),
        ("huevo", "aceite", "manteq"),
        ("panales", "soda"),
        ("huevo", "aceite", "leche","manteq","soda")]
cont = 0
item1 = 0
item2 = 0
conti = 0
contj = 0
contk = 0
elije = 0
con = 0
while(elije<len(palabras)):
    while(con < len(palabras)):
        cont = 0
        item1 = 0
        item2 = 0
        confianza1 = 0
        confianza2 = 0
        conti = 0
        contj = 0
        contk = 0
        if(elije != con):

            for i in lista:
                contj=0
                for j in lista[cont]:
                    
                    if(palabras[elije]==lista[conti][contj]):
                        confianza2 += 1
                        contk=0
                        for k in lista[cont]:
                            if(palabras[con] == lista[conti][contk]):
                                item1 += 1
                            contk += 1
                    contj += 1
                conti += 1
                cont += 1
            item2 = len(lista)
            soporte(elije,con,item1,item2)
            confianza(elije,con,item1,confianza2)
        con += 1
    con = 0
    elije += 1

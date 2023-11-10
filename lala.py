diccio={}
with open ("transacciones_simple.txt", "r", encoding="utf8") as archivo:
    entero=archivo.read()
    lineas=entero.split("\n")
    inqui=lineas.pop(0)
    inquilinos=inqui.split(" ")
    x=0
    n=len(lineas)-1
    print(n)
    for i in lineas:
        anali=lineas.pop(x)
        #print(anali)
        partes=anali.split(" ")
        print(partes)
        if partes[1]=="*":
            inquilinos.append(partes[2])
        else:
            if partes[1] not in diccio:
                diccio[partes[1]] = [[partes[0], partes[2]]]
            else:
                diccio[partes[1]].append([partes[0], partes[2]])
            #fin if  
        #fin if
        x+=1
        #print(diccio)
    #fin while

#if partes[1] not in diccio:
#                    diccio={partes[1]:[[partes[0],partes[2]]]}
#                else:
#                    diccio[partes[1]]=partes[1]
#                #fin if
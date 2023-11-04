l_inquilinos=[]
archivo_entero=[]
archivo_lineas=[]
inqui=[]
orden={}
def inquilinos (nombre):
    with open (nombre, "r", encoding="utf8") as archivo:
        archivo_entero= archivo.read()
        archivo_lineas= archivo_entero.split("\n")
        inqui=archivo_lineas.pop(0)
        l_inquilinos=inqui.split(" ")
    return l_inquilinos

var1=input("Ingrese el nombre del archivo a analizar: ")
inquilinos (var1)
with open (var1, "r", encoding="utf8") as archivo:
        archivo_entero= archivo.read()
        archivo_lineas= archivo_entero.split("\n")
        inqui=archivo_lineas.pop(0)

print (archivo_lineas)

def interpretacion (archivo_lineas):
    for i in archivo_lineas:
        paso=archivo_lineas.pop(i)
        caso=paso.split(" ")
        fecha=caso.pop(0)
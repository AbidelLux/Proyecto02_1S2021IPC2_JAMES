from archivoLectura import lista
from matrizOctagonal import matriz_Ortogonal
from matrizOctagonal import graficar_matriz
name=""
fila=0
columna=0
def matriz(nombre):
    global fila,columna,name,matrizOriginal
    matrizOriginal=matriz_Ortogonal()
    picture=""
    for dato in lista.iterar():
        if dato[0].upper() == nombre.upper():
            name=dato[0]
            fila=int(dato[1])
            columna=int(dato[2])
            picture=dato[3]
    #picture=picture.replace("-\n","- \n")
    #picture=picture.replace("*\n","* \n")
    #picture=picture.replace("\n","")
    picture= picture.split("\n")
    picture.pop(0)
    numero=int(len(picture))
    picture.pop(numero-1)
    #picture=picture.remove("")
    for x in range(fila):
        for y in range(columna):
            if picture[x][y]=="*":
                matrizOriginal.insertar(x,y,picture[x+1][y+1])
    graficar_matriz(matrizOriginal)
def horizontal(dato):
    matriz(dato)
    print()
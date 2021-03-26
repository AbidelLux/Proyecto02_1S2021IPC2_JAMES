from archivoLectura import lista
from listaSimpleAuxiliar import listaEnlazadaMatriz
from matrizOctagonal import matriz_Ortogonal
from matrizOctagonal import graficar_matriz
from graficoGraphviz import crearDot
name=""
fila=0
columna=0
sizeMatriz=0
def matriz(nombre):
    global fila,columna,name,sizeMatriz
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
                matrizOriginal.insertar(x+1,y+1,picture[x][y])
    sizeMatriz=int(len(picture))+2                
    #graficar_matriz(matrizOriginal,"Matriz_Original")
    crearDot(matrizOriginal,fila,columna,sizeMatriz,"Original")
    return matrizOriginal

def horizontal(dato):
    global fila,columna,name,sizeMatriz
    Original=matriz(dato)
    prueba0=voltearMatriz(Original)
    prueba1=rotarMatriz(prueba0)
    prueba2=rotarMatriz(prueba1)
    #crearDot(prueba0,fila,columna,sizeMatriz,"Resultado1")
    crearDot(prueba2,fila,columna,sizeMatriz,"Resultado")

def traspuesta(dato):
    global fila,columna,name,sizeMatriz
    Original=matriz(dato)
    prueba0=voltearMatriz(Original)
    prueba1=rotarMatriz(prueba0)
    #crearDot(prueba0,fila,columna,sizeMatriz,"Resultado1")
    crearDot(prueba1,fila,columna,sizeMatriz,"Resultado")  

def vertical(dato):
    global fila,columna,name,sizeMatriz
    Original=matriz(dato)
    prueba0=voltearMatriz(Original)   
    crearDot(prueba0,fila,columna,sizeMatriz,"Resultado")        
def voltearMatriz(lista):
    global fila,columna,sizeMatriz
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()   
    for i in range(1,fila+1):
        for j in range(1,columna+1):
            if lista.buscar(i,j)==True:
                listaAux2.add(i,((sizeMatriz-1)-j),"*")
            else:
                continue
    
    for x in range(1,fila+1):
        for y in range(1,columna+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")
    #graficar_matriz(matrizPrueba,"matrizPrueba")  
    #crearDot(matrizPrueba,fila,columna,sizeMatriz,"vuelta")  
    return matrizPrueba
    
def rotarMatriz(lista): 
    global fila,columna,sizeMatriz
    listaAux=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()   
    for i in range(1,fila+1):
        for j in range(1,columna+1):
            if lista.buscar(i,j)==True:
                listaAux.add(((sizeMatriz-1)-j),(i),"*")
            else:
                continue
    
    for x in range(1,fila+1):
        for y in range(1,columna+1):
            if listaAux.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")
    #graficar_matriz(matrizPrueba,"matrizPrueba")    
    return matrizPrueba

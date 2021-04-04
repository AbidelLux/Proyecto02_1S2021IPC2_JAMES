from archivoLectura import lista,fechaHora
from listaSimpleAuxiliar import listaEnlazadaMatriz
from matrizOctagonal import matriz_Ortogonal
from matrizOctagonal import graficar_matriz
from graficoGraphviz import crearDot, crearDot3,crearDot6
from graficoGraphviz import crearDot2,crearDot4,crearDot5
from inicio import report
name=""
fila=0
columna=0
sizeMatriz=0
resultado=""
def matriz(nombre,bandera):
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
    if bandera==True:
        report.add(''+str(fechaHora())+'Generanado matriz Original - matriz Usada: '+nombre+'')
        crearDot(matrizOriginal,fila,columna,sizeMatriz,"Original")
    return matrizOriginal

def horizontal(dato):
    global fila,columna,name,sizeMatriz,resultado
    Original=matriz(dato,True)
    report.add(''+str(fechaHora())+'Rotacion Horizontal - matriz Usada: '+dato+'')
    prueba0=voltearMatriz(Original)
    prueba1=rotarMatriz(prueba0)
    prueba2=rotarMatriz(prueba1)
    resultado=prueba2
    #crearDot(prueba0,fila,columna,sizeMatriz,"Resultado1")
    crearDot(prueba2,fila,columna,sizeMatriz,"Resultado")

def traspuesta(dato):
    global fila,columna,name,sizeMatriz,resultado
    Original=matriz(dato,True)
    report.add(''+str(fechaHora())+'Traspuesta - matriz Usada: '+dato+'')
    prueba0=voltearMatriz(Original)
    prueba1=rotarMatriz(prueba0)
    resultado=prueba1
    #crearDot(prueba0,fila,columna,sizeMatriz,"Resultado1")
    crearDot(prueba1,fila,columna,sizeMatriz,"Resultado")  

def vertical(dato):
    global fila,columna,name,sizeMatriz,resultado
    Original=matriz(dato,True)
    report.add(''+str(fechaHora())+'Rotacion vertical - matriz Usada: '+dato+'')
    prueba0=voltearMatriz(Original)  
    resultado=prueba0 
    crearDot(prueba0,fila,columna,sizeMatriz,"Resultado")        
def deletMatriz(dato,x1,y1,x2,y2):
    global fila,columna,name,sizeMatriz,resultado
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()
    Original=matriz(dato,True)
    report.add(''+str(fechaHora())+'Limpiar Area - matriz Usada: '+dato+'')
    for i in range(1,fila+1):
        for j in range(1,columna+1):
            if Original.buscar(i,j)==True:
                if i>=int(x1) and  i<=int(x2) and j>=int(y1) and j<=int(y2):
                    continue
                #elif i<=int(x2)
                else:
                    listaAux2.add(i,j,"*")
    for x in range(1,fila+1):
        for y in range(1,columna+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")    
    resultado=matrizPrueba
    crearDot2(matrizPrueba,fila,columna,sizeMatriz,"Resultado",x1,y1,x2,y2)  

def agregar_H(dato,x1,y1,x2,y2):
    global fila,columna,name,sizeMatriz,resultado
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()
    Original=matriz(dato,True)
    report.add(''+str(fechaHora())+'Agregar Linea Horizontal - matriz Usada: '+dato+'')
    for i in range(1,fila+1):
        for j in range(1,columna+1):
            if Original.buscar(i,j)==True:
                    listaAux2.add(i,j,"*")
            else:
                if i>=int(x1) and  i<=int(x2) and j>=int(y1) and j<=int(y2):
                    listaAux2.add(i,j,"*")
                else:
                    continue
    for x in range(1,fila+1):
        for y in range(1,columna+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")   
    resultado=matrizPrueba
    #crearDot(matrizPrueba,fila,columna,sizeMatriz,"Resultado") 
    crearDot3(matrizPrueba,fila,columna,sizeMatriz,"Resultado",x1,y1,x2,y2)      
def agregar_V(dato,x1,y1,x2,y2):
    global fila,columna,name,sizeMatriz,resultado
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()
    Original=matriz(dato,True)
    report.add(''+str(fechaHora())+'Agregar Linea Vertical - matriz Usada: '+dato+'')
    for i in range(1,fila+1):
        for j in range(1,columna+1):
            if Original.buscar(i,j)==True:
                    listaAux2.add(i,j,"*")
            else:
                if i>=int(x1) and  i<=int(x2) and j>=int(y1) and j<=int(y2):
                    listaAux2.add(i,j,"*")
                else:
                    continue
    for x in range(1,fila+1):
        for y in range(1,columna+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")   
    resultado=matrizPrueba
    #crearDot(matrizPrueba,fila,columna,sizeMatriz,"Resultado") 
    crearDot3(matrizPrueba,fila,columna,sizeMatriz,"Resultado",x1,y1,x2,y2)
def agregar_R(dato,x1,y1,x2,y2):
    global fila,columna,name,sizeMatriz,resultado
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()
    Original=matriz(dato,True)
    report.add(''+str(fechaHora())+'Agregar Rectangulo - matriz Usada: '+dato+'')
    for i in range(1,fila+1):
        for j in range(1,columna+1):
            if Original.buscar(i,j)==True:
                    listaAux2.add(i,j,"*")
            else:
                if i==int(x1) and j>=int(y1) and j<=int(y2):
                    listaAux2.add(i,j,"*")
                elif j==int(y1) and i>=int(x1) and i<=int(x2):
                    listaAux2.add(i,j,"*")
                elif j==int(y2) and i>=int(x1) and i<=int(x2):
                    listaAux2.add(i,j,"*")
                elif i==int(x2) and j>=int(y1) and j<=int(y2):
                    listaAux2.add(i,j,"*")
                else:
                    continue
    for x in range(1,fila+1):
        for y in range(1,columna+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")   
    resultado=matrizPrueba
    #crearDot(matrizPrueba,fila,columna,sizeMatriz,"Resultado") 
    crearDot4(matrizPrueba,fila,columna,sizeMatriz,"Resultado",x1,y1,x2,y2)    
    
def agregar_T(dato,x1,y1,x2,y2):
    global fila,columna,name,sizeMatriz,resultado
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()
    Original=matriz(dato,True)
    report.add(''+str(fechaHora())+'Agregar Triangulo Rectangulo - matriz Usada: '+dato+'')
    n=1
    for i in range(1,fila+1):
        bandera=False
        for j in range(1,columna+1):
            if Original.buscar(i,j)==True:
                if j==(int(y1)+n) and j<int(y2) and i>int(x1) and i<int(x2) and bandera==False:
                    listaAux2.add(i,j,"*")
                    bandera=True
                    n+=1
                else:                
                    listaAux2.add(i,j,"*")
            else:
                if i==int(x1) and j==int(y1):
                    listaAux2.add(i,j,"*")
                elif j==int(y1)  and i>int(x1) and i<int(x2):
                    listaAux2.add(i,j,"*")
                elif j==(int(y1)+n) and j<int(y2) and i>int(x1) and i<int(x2) and bandera == False:
                    listaAux2.add(i,j,"*")
                    bandera=True
                    n+=1
                elif i==int(x2) and j>=int(y1) and j<=int(y2):
                    listaAux2.add(i,j,"*")
                else:
                    continue 
    for x in range(1,fila+1):
        for y in range(1,columna+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")   
    resultado=matrizPrueba
    #crearDot(matrizPrueba,fila,columna,sizeMatriz,"Resultado") 
    crearDot5(matrizPrueba,fila,columna,sizeMatriz,"Resultado",x1,y1,x2,y2)         

def Union(dato1, dato2, fila1,columna1,x1,y1,x2,y2):
    global sizeMatriz,resultado,fila,columna
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()
    Original1=matriz(dato1,False) 
    Original2=matriz(dato2,False)
    report.add(''+str(fechaHora())+'Union - matrices Usadas: ('+dato1+','+dato2+')')
    name=''+str(dato1)+' Union '+str(dato2)
    crearDot6(Original1,Original2,x1,y1,x2,y2,name,"Original")    
    for i in range(1,fila1+1):
        for j in range(1,columna1+1):
            if Original1.buscar(i,j)==False and Original2.buscar(i,j)==False:
                continue
            else:
                listaAux2.add(i,j,"*")
    for x in range(1,fila1+1):
        for y in range(1,columna1+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")   
    
    resultado=matrizPrueba
    fila=fila1
    columna=columna1
    crearDot(matrizPrueba,fila1,columna1,sizeMatriz,"Resultado")        

def intersection(dato1, dato2, fila1,columna1,x1,y1,x2,y2):
    global sizeMatriz,resultado,fila,columna
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()
    Original1=matriz(dato1,False) 
    Original2=matriz(dato2,False)
    report.add(''+str(fechaHora())+'Interseccion - matrices Usadas: ('+dato1+','+dato2+')')
    name=''+str(dato1)+' Intersección '+str(dato2)
    crearDot6(Original1,Original2,x1,y1,x2,y2,name,"Original")    
    for i in range(1,fila1+1):
        for j in range(1,columna1+1):
            if Original1.buscar(i,j)==True and Original2.buscar(i,j)==True:
                listaAux2.add(i,j,"*")
            else:
                continue
    for x in range(1,fila1+1):
        for y in range(1,columna1+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")   
    resultado=matrizPrueba
    fila=fila1
    columna=columna1
    crearDot(matrizPrueba,fila1,columna1,sizeMatriz,"Resultado")      

def dif(dato1, dato2, fila1,columna1,x1,y1,x2,y2):
    global sizeMatriz,resultado,fila,columna
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()
    Original1=matriz(dato1,False) 
    Original2=matriz(dato2,False)
    report.add(''+str(fechaHora())+'Diferencia - matrices Usadas: ('+dato1+','+dato2+')')
    name=''+str(dato1)+' - '+str(dato2)
    crearDot6(Original1,Original2,x1,y1,x2,y2,name,"Original")    
    for i in range(1,fila1+1):
        for j in range(1,columna1+1):
            if Original1.buscar(i,j)==True and Original2.buscar(i,j)==True:
                continue
            else:
                if Original1.buscar(i,j)==True and Original2.buscar(i,j)==False:
                    listaAux2.add(i,j,"*")
                else:
                    continue
    for x in range(1,fila1+1):
        for y in range(1,columna1+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")  
    resultado=matrizPrueba
    fila=fila1
    columna=columna1 
    crearDot(matrizPrueba,fila1,columna1,sizeMatriz,"Resultado")  
    
def simetria(dato1, dato2, fila1,columna1,x1,y1,x2,y2):
    global sizeMatriz,resultado,fila,columna
    listaAux2=listaEnlazadaMatriz()
    matrizPrueba=matriz_Ortogonal()
    Original1=matriz(dato1,False) 
    Original2=matriz(dato2,False)
    report.add(''+str(fechaHora())+'Diferencia Simetrica - matrices Usadas: ('+dato1+','+dato2+')')
    name=''+str(dato1)+' - '+str(dato2)
    crearDot6(Original1,Original2,x1,y1,x2,y2,name,"Original")    
    for i in range(1,fila1+1):
        for j in range(1,columna1+1):
            if Original1.buscar(i,j)==True and Original2.buscar(i,j)==True:
                continue
            else:
                if Original1.buscar(i,j)==True and Original2.buscar(i,j)==False:
                    listaAux2.add(i,j,"*")
                elif Original1.buscar(i,j)==False and Original2.buscar(i,j)==True:
                    listaAux2.add(i,j,"*")
                else:
                    continue
    for x in range(1,fila1+1):
        for y in range(1,columna1+1):
            if listaAux2.buscar2(x,y)==True:
                matrizPrueba.insertar(x,y,"*")   
    resultado=matrizPrueba
    fila=fila1
    columna=columna1
    crearDot(matrizPrueba,fila1,columna1,sizeMatriz,"Resultado")  
        
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

def modificar(nombre):
    global fila,columna,resultado
    image=""
    for i in range(1,fila+1):
        image+='\n'
        for j in range(1,columna+1):
            if resultado.buscar(i,j)==True:
                image+="*"
            else:
                image+="-"
    image+="\n"
    print(image)
    lista.modificar(nombre,image)
def guardar(nombre):
    global fila,columna,resultado
    image=""
    for i in range(1,fila+1):
        image+='\n'
        for j in range(1,columna+1):
            if resultado.buscar(i,j)==True:
                image+="*"
            else:
                image+="-"
    image+="\n"
    print(image)
    lista.add(nombre,fila,columna,image)
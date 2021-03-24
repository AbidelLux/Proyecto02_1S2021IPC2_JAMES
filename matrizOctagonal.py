class NodoMatrizOcta:
    def __init__(self,x,y,dato):
        self.x=x
        self.y=y
        self.dato=dato
        self.arriba=None
        self.abajo=None
        self.izquierda=None
        self.derecha=None
class NodoCabecera:
    def __init__(self,tipo=None,indice=None,siguiente=None,derecha=None,abajo=None):
        self.tipo=tipo
        self.indice=indice
        self.siguiente=siguiente
        self.derecha=derecha
        self.abajo=abajo
class NodoRaiz:
    def __init__(self):
        self.NodoFilas=None
        self.NodoColumnas=None
class matriz_Ortogonal:
    def __init__(self):
        self.NodoRaiz=None
    def insertar_nodoFila(self,nodo):
        filaTemporal=self.NodoRaiz.NodoFilas
        while(filaTemporal.indice!=nodo.y):
            filaTemporal=filaTemporal.siguiente
        if filaTemporal.derecha is None:
            nodo.derecha=filaTemporal.derecha
            filaTemporal.derecha=nodo
        elif filaTemporal.derecha.x >= nodo.x:
            nodo.derecha=filaTemporal.derecha
            filaTemporal.derecha=nodo
        else:
            actual=filaTemporal.derecha
            while actual.derecha is not None and actual.derecha.x < nodo.x:
                actual=actual.derecha
            nodo.derecha=actual.derecha
            actual.derecha=nodo
    def insert_nodoColumna(self,nodo):
        columnaTemporal=self.NodoRaiz.NodoColumnas
        while columnaTemporal.indice!=nodo.x:
            columnaTemporal=columnaTemporal.siguiente
        if columnaTemporal.abajo is None:
            nodo.abajo=columnaTemporal.abajo
            columnaTemporal.abajo=nodo
        elif columnaTemporal.abajo.y >= nodo.y:
            nodo.abajo=columnaTemporal.abajo
            columnaTemporal.abajo=nodo
        else:
            actual=columnaTemporal.abajo
            while actual.abajo is not None and actual.abajo.y < nodo.y:
                actual=actual.abajo
            nodo.abajo=actual.abajo
            actual.abajo=nodo
    def insert_cabecera(self,nodo,indice,tipo):
        #NodoRaiz=NodoRaiz()
        filaTemporal=nodo
        if filaTemporal.indice > indice:
            newCabeza=NodoCabecera(tipo=tipo,indice=indice)
            newCabeza.siguiente=self.NodoRaiz.NodoFilas
            self.NodoRaiz.NodoFilas=newCabeza
        else:
            actual=filaTemporal
            while actual.siguiente is not None and actual.siguiente.indice <= indice:
                actual=actual.siguiente
            if actual.indice != indice:
                newCabeza=NodoCabecera(tipo=tipo, indice=indice)
                newCabeza.siguiente=actual.siguiente
                actual.siguiente=newCabeza
    def insertar(self,x,y,dato):
        Nodo=NodoMatrizOcta(x,y,dato)
        if self.NodoRaiz is None:
            self.NodoRaiz=NodoRaiz()
            self.NodoRaiz.NodoColumnas=NodoCabecera(tipo="Columna",indice=x)
            self.NodoRaiz.NodoFilas=NodoCabecera(tipo="Fila",indice=y)
            self.NodoRaiz.NodoColumnas.siguiente=None
            self.NodoRaiz.NodoFilas.siguiente=None
            self.NodoRaiz.NodoColumnas.abajo=Nodo
            self.NodoRaiz.NodoFilas.derecha=Nodo
        else:
            NodoAuxiliar=self.NodoRaiz
            self.insert_cabecera(NodoAuxiliar.NodoFilas,y,"Filas")
            NodoAuxiliar=self.NodoRaiz
            self.insert_cabecera(NodoAuxiliar.NodoColumnas,x,"Columna")
            self.insertar_nodoFila(nodo=Nodo)
            self.insert_nodoColumna(nodo=Nodo)
    def buscar(self,x,y):
        nodo=self.NodoRaiz.NodoColumnas
        while nodo is not None:
            NodoAuxiliar=nodo.abajo
            while NodoAuxiliar is not None:
                if NodoAuxiliar.x==x and NodoAuxiliar.y==y:
                    return True
                NodoAuxiliar=NodoAuxiliar.abajo
            nodo=nodo.siguiente
        return False
    
'''    
import os


nueva_matriz = matriz_Ortogonal()

nueva_matriz.insertar(2,5,"nuevo nodo")
nueva_matriz.insertar(2,3,"nuevo nodo")
nueva_matriz.insertar(2,4,"nuevo nodo")
nueva_matriz.insertar(2,9,"nuevo nodo")
nueva_matriz.insertar(3,7,"nuevo nodo")
nueva_matriz.insertar(3,1,"nuevo nodo")
nueva_matriz.insertar(3,8,"nuevo nodo")
nueva_matriz.insertar(3,9,"nuevo nodo")
nueva_matriz.insertar(6,6,"nuevo nodo")
nueva_matriz.insertar(6,1,"nuevo nodo")
nueva_matriz.insertar(6,5,"nuevo nodo")
nueva_matriz.insertar(6,9,"nuevo nodo")
nueva_matriz.insertar(8,3,"nuevo nodo")
nueva_matriz.insertar(8,4,"nuevo nodo")
nueva_matriz.insertar(9,8,"nuevo nodo")
nueva_matriz.insertar(9,9,"nuevo nodo")
nueva_matriz.insertar(8,1,"nuevo nodo")
nueva_matriz.insertar(10,10,"nuevo nodo")
nueva_matriz.insertar(10,1,"nuevo nodo")
nodo = nueva_matriz.NodoRaiz.NodoColumnas


nodo = nueva_matriz.NodoRaiz.NodoFilas
while(nodo is not None):
    nodo_temp = nodo.derecha
    while(nodo_temp is not None):
        print(str(nodo_temp.x)+str(nodo_temp.y))
        nodo_temp=nodo_temp.derecha
    nodo=nodo.siguiente
    
print("FIN")
nodo = nueva_matriz.NodoRaiz.NodoColumnas
while(nodo is not None):
    nodo_temp = nodo.abajo
    while(nodo_temp is not None):
        print(str(nodo_temp.x)+str(nodo_temp.y))
        nodo_temp=nodo_temp.abajo
    nodo=nodo.siguiente
    
print("FIN")
'''
def graficar_matriz(nueva_matriz,name):
    import os
    grafo = "digraph"
    grafo+=str("{\nnode[shape=record];\n")
    grafo+=str("graph[pencolor=transparent];\n")
    #grafo+=str("rankdir=LR;\n")
    grafo+=str("node [style=filled];\n")
    nodo = nueva_matriz.NodoRaiz.NodoFilas

    for y in range(1, 11):
        nodo_temp = nodo.derecha
        for x in range(1, 11):
            if(nueva_matriz.buscar(x,y)):
                grafo+=str("p"+str(x)+str(y)+"[label=\"{<data>"+str(x)+","+str(y)+"|<next>}\" pos=\""+str(x)+","+str(10-y)+"!\"];\n")
                if(nodo_temp.derecha!=None): 
                    nodo_2=nodo_temp
                    nodo_temp=nodo_temp.derecha
                    grafo+=str("p"+str(nodo_2.x)+str(nodo_2.y)+"->"+"p"+str(nodo_temp.x)+str(nodo_temp.y)+"[dir=both];\n")
            else:
                pass
            if nodo.siguiente!=None:
                if nodo.siguiente.indice==y+1:
                    nodo=nodo.siguiente    
    nodo = nueva_matriz.NodoRaiz.NodoColumnas
    for x in range(1, 11):
        nodo_temp = nodo.abajo
        for y in range(1, 11):
            if(nueva_matriz.buscar(x,y)):
                if(nodo_temp.abajo!=None):
                    nodo_2=nodo_temp
                    nodo_temp=nodo_temp.abajo
                    grafo+=str("p"+str(nodo_2.x)+str(nodo_2.y)+"->"+"p"+str(nodo_temp.x)+str(nodo_temp.y)+"[dir=both];\n")
            else:
                pass
            if nodo.siguiente!=None:
                if nodo.siguiente.indice==x+1:
                    nodo=nodo.siguiente         
    grafo+=str("}\n")
    f= open(name+".dot","w+")
    f.write(grafo)
    f.close()   
    os.system("fdp -Tpng -o "+name+".png "+name+".dot")


#graficar_matriz()
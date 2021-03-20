class NodoMatrizOcta:
    def __init__(self,x,y,dato,arriba,abajo,izquierda,derecha):
        self.x=x
        self.y=y
        self.dato=dato
        self.arriba=arriba
        self.abajo=abajo
        self.izquierda=izquierda
class NodoCabecera:
    def __init__(self,tipo,indice,siguiente,derecha,abajo):
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
            newCabeza=NodoCabecera(tipo,indice)
            newCabeza.siguiente=self.NodoRaiz.NodoFilas
            self.NodoRaiz.NodoFilas=newCabeza
        else:
            actual=filaTemporal
            while actual.siguiente is not None and actual.siguiente.indice <= indice:
                actual=actual.siguiente
            if actual.indice != indice:
                newCabeza=NodoCabecera(tipo, indice)
                newCabeza.siguiente=actual.siguiente
                actual.siguiente=newCabeza
    def insertar(self,x,y,dato):
        nodo=NodoMatrizOcta(x,y,dato)
        if self.NodoRaiz is None:
            self.NodoRaiz=NodoRaiz()
            self.NodoRaiz.NodoColumnas=NodoCabecera("Columna",x)
            self.NodoRaiz.NodoFilas=NodoCabecera("Fila",y)
            self.NodoRaiz.NodoColumnas.siguiente=None
            self.NodoRaiz.NodoFilas.siguiente=None
            self.NodoRaiz.NodoColumnas.abajo=nodo
            self.NodoRaiz.NodoFilas.derecha=nodo
        else:
            NodoAuxiliar=self.NodoRaiz
            self.insert_cabecera(NodoAuxiliar.NodoFilas,y,"Filas")
            NodoAuxiliar=self.NodoRaiz
            self.insert_cabecera(NodoAuxiliar.NodoColumnas,x,"Columna")
            self.insertar_nodoFila(nodo)
            self.insert_nodoColumna(nodo)
            
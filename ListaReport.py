class Nodo:
    def __init__ (self,dato):
        #self.nombre=nombre
        self.dato=dato
        self.Siguiente=None


class listaEnlazadaMatriz:
    def __init__(self):
        self.inicio=None
        self.cola=None
        self.tamaño=0
        
    def add(self,dato):
        nodo=Nodo(dato)
        self.tamaño +=1
        
        if self.inicio:
            self.inicio.Siguiente=nodo
            self.inicio=nodo
        else:
            self.inicio=nodo
            self.cola=nodo
            
    def iterar(self):
        actual = self.cola

        while actual:
            #nombre = actual.nombre
            #x=actual.CoorX
           # y=actual.CoorY
            dato=actual.dato
            actual = actual.Siguiente
            yield dato
    '''
    def crearlista(self,b,v):
        dato=""
        for x in range(b):
            for y in range(v):
               for n in self.iterar():
                    if x+1==int(n[0]) and y+1==int(n[1]): 
                        if y+1==1:
                            dato+="["+str(n[2])+","
                        elif y+1==v and (x+1)!=b:
                            dato+=str(n[2])+"]/"
                        elif x+1==b and y+1==v:
                            dato+=str(n[2])+"]"
                        else:
                            dato+=str(n[2])+","
        dato=dato.split("/")
        return dato  
       '''               
    def buscar(self,x,y):
        for n in self.iterar():
            if x==int(n[0]) and y==int(n[1]):
                return n[2]
    def buscar2(self,x,y):
        for n in self.iterar():
            if x==n[0] and y==n[1]:
                return True
        return False
    def eliminar(self,x,y):
        actual=self.cola
        anterior=self.cola
        
        while actual:
            if int(actual.CoorX)==x and int(actual.CoorY)==y:
                if actual==self.cola:
                    self.cola=actual.Siguiente
                else:
                    # suponermos que tengo [1]->[2]->[3]
                    #ahora quiero eliminar [2]
                    #mi resultado [1]->[3]
                    anterior.Siguiente=actual.Siguiente
                self.tamaño-=1
                return
            anterior=actual
            actual=actual.Siguiente
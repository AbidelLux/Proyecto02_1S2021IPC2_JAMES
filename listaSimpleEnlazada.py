class Nodo:
    def __init__ (self,nombre,fila,columna,image):
        self.nombre=nombre
        self.CoorX=fila
        self.CoorY=columna
        self.image=image
        self.Siguiente=None


class listaEnlazadaMatriz:
    def __init__(self):
        self.inicio=None
        self.cola=None
        self.tamaño=0
        
    def add(self,nombre,fila,columna,image):
        nodo=Nodo(nombre,fila,columna,image)
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
            nombre = actual.nombre
            x=actual.CoorX
            y=actual.CoorY
            pic=actual.image
            actual = actual.Siguiente
            yield nombre,x,y,pic
    def modificar(self,nombre,imagen):
        actual=self.cola
        while actual:
            if nombre==actual.nombre:
                actual.image=imagen
            actual=actual.Siguiente
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
    def crearlist(self):
        names=""
        for count,n in enumerate(self.iterar()):
            if count==0:
                names+=''+str(n[0])+','
            elif (self.tamaño-1)==count:
                names+=str(n[0])+''
            else:
                names+=str(n[0])+','  
        names=names.split(",")  
        return names          
    def buscar(self,x,y):
        for n in self.iterar():
            if x==int(n[0]) and y==int(n[1]):
                return n[2]
    def buscar2(self,name):
        for n in self.iterar():
            if n[0].upper()==name.upper():
                return True
        return False
    def buscar3(self,name):
        for n in self.iterar():
            if n[0].upper()==name.upper():
                return n

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
#    def deletCola(self):
#        actual=self.cola
        
#        if not actual:
#           anterior=actual.Siguiente
#           actual=actual.Siguiente
#           self.tamaño-=1
#           return True
#        else:
#            return False
#        return False        
#def prueba(x,y,dato):
   # lista=listaEnlazadaMatriz()
   # lista.add(0,0,1)
   # lista.add(0,1,5)


#def imprimir():
    #lista=listaEnlazadaMatriz()
   # for d in lista.iterar():
    #    print(d[2])
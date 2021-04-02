from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf
#REPORT=""
respuesta=""
letra=""
bandera=False
Archivo=False
tipoL=""
def menus():
    global letra, bandera, Archivo
    def lectura():
        global bandera,Archivo
        from archivoLectura import lecturaM
        root.destroy()
        lecturaM()
        Archivo=True
        bandera=False
        menus()
        #print("hola mundo")
    def rotacionH():
        global bandera,letra
        from archivoLectura import lista
        from operacionalMatriz import horizontal
        root.destroy()
        busca()
        
        horizontal(respuesta)
        bandera=True
        letra="Rotacion Horizontal"
        menus()
    def rotacionV():
        global bandera,letra
        from archivoLectura import lista
        from operacionalMatriz import vertical
        root.destroy()
        busca()
        vertical(respuesta)
        bandera=True
        letra="Rotacion Vertical"
        menus()
    def transpuesta():
        global bandera,letra
        from archivoLectura import lista
        from operacionalMatriz import traspuesta
        root.destroy()
        busca()
        traspuesta(respuesta)
        bandera=True
        letra="Traspuesta"
        menus()
    def agregarH():
        global tipoL,bandera
        tipoL="horizontal"
        bandera=True
        agregarL_Ven()
        #print("Agregar Linea Horizontal")
    def agregarV():
        global tipoL,bandera
        tipoL="vertical"
        bandera=True
        agregarL_Ven()
        #print("Agregar Linea Vertical")
    def agregarRec():
        global tipoL,bandera
        #tipoL="Rectangulo"
        bandera=True
        venCuadraTri()
        #print("Agregar Linea Vertical")
        #print("Agregar Rectangulo")
    def agregarTRec():
        global tipoL,bandera
        #tipoL="Triangulo"
        bandera=True
        agregarT_Ven()
        #print("Agregar Triangulo Rectangulo")
    def imagenSize(dato):
        imagen=PhotoImage(file=dato)
        imagen=imagen.zoom(1)
        imagen=imagen.subsample(1)
        return imagen
        #labelImage1['image']=imagen
    def busca():
        global Archivo
        from archivoLectura import lista
        venP=Tk()
        def cerrar_app():
            venP.destroy()
            menus()
            
        venP.protocol("WM_DELETE_WINDOW", cerrar_app)   
        label=Label(venP,text="Ingrese el nombre  de la Matriz")
        label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        label.config(justify="center" , state="normal",font=("Verdana",12))

        if Archivo==True:   
            dato=lista.crearlist()
        else:
            dato=""

        #creando la caja de texto 
        entry=ttk.Combobox(venP,state="readonly",values=dato)
        entry.grid(row=3,column=0,padx=5,pady=10)
        entry.config(font=("Verdana",12))

        def ok():
            from archivoLectura import lista
            global respuesta
            #entry.focus_set()
            respuesta=entry.get()
            if lista.buscar2(respuesta)==True:
                venP.destroy() 
            elif respuesta=="":
                messagebox.showerror(message="Por favor llene el Cuadro de Texto")
            else:
                messagebox.showerror(message="El nombre de la matriz no existe")
        #
        boton=Button(venP,text="Buscar", command=ok)
        boton.grid(row=4, column=0, padx=5,pady=15)
        #venP.destroy()    
        venP.mainloop()
    
        #for a in lista.iterar():
        #print("rotacion Horizontal")
    def limpiarVen():
        from archivoLectura import lista
        root.destroy()
        VenLimpiar=Tk()
        VenLimpiar.title("Ingrese Coordenada")
        VenLimpiar.geometry("320x320")
        
        def cerrar_app():
            VenLimpiar.destroy()
            menus()
            
        VenLimpiar.protocol("WM_DELETE_WINDOW", cerrar_app)   
        #VenLimpiar.config(bg="#ffffff")
        #ingresando los label de las coordenadas
        label=Label(VenLimpiar,text="Buscar Matriz:")
        label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        label.config(justify="center" , state="normal",font=("Verdana",12))
        
        if Archivo==True:   
            dato=lista.crearlist()
        else:
            dato=""    
                
        entry=ttk.Combobox(VenLimpiar,state="readonly",values=dato)
        entry.grid(row=0,column=1,padx="5",pady="3")
        entry.config(justify="center",state="normal",font=("Verdana",12))   
        entry.place(relx=0.4,relwidth=0.5, relheight=0.10)     
        
        labelX1=Label(VenLimpiar,text="X1")
        labelX1.config(font=("verdana",12))
        labelX1.place(relx=0.25,rely=0.15)
        
        dato1=Entry(VenLimpiar)
        dato1.place(relx=0.2,rely=0.25,relwidth=0.2,relheight=0.10)
        dato1.config(justify="center",state="normal",font=("Verdana",12))
        
        coma1=Label(VenLimpiar,text=",")
        coma1.config(font=("verdana",12))
        coma1.place(relx=0.48,rely=0.30)
        
        parentesis1=Label(VenLimpiar,text="(")
        parentesis1.config(font=("verdana",32))
        parentesis1.place(relx=0.10,rely=0.20)

        parentesis2=Label(VenLimpiar,text=")")
        parentesis2.config(font=("verdana",32))
        parentesis2.place(relx=0.83,rely=0.20)
    
        vocalM=Label(VenLimpiar,text="A")
        vocalM.config(font=("verdana",18))
        vocalM.place(relx=0.45,rely=0.38)
            
        dato2=Entry(VenLimpiar)
        dato2.place(relx=0.6,rely=0.25,relwidth=0.2,relheight=0.10)
        dato2.config(justify="center",state="normal",font=("Verdana",12))
                        
        labelY1=Label(VenLimpiar,text="Y1")
        labelY1.config(font=("verdana",12))
        labelY1.place(relx=0.65,rely=0.15)
                
        labelX2=Label(VenLimpiar,text="X2")
        labelX2.config(font=("verdana",12))
        labelX2.place(relx=0.25,rely=0.5)

        coma2=Label(VenLimpiar,text=",")
        coma2.config(font=("verdana",12))
        coma2.place(relx=0.48,rely=0.6)
        
        labelY2=Label(VenLimpiar,text="Y2")
        labelY2.config(font=("verdana",12))
        labelY2.place(relx=0.65,rely=0.5)
        
        parentesis3=Label(VenLimpiar,text="(")
        parentesis3.config(font=("verdana",32))
        parentesis3.place(relx=0.10,rely=0.55)

        parentesis4=Label(VenLimpiar,text=")")
        parentesis4.config(font=("verdana",32))
        parentesis4.place(relx=0.83,rely=0.55)
                
        dato3=Entry(VenLimpiar)
        dato3.place(relx=0.2,rely=0.6,relwidth=0.2,relheight=0.10)
        dato3.config(justify="center",state="normal",font=("Verdana",12))
        
        dato4=Entry(VenLimpiar)
        dato4.place(relx=0.6,rely=0.6,relwidth=0.2,relheight=0.10)
        dato4.config(justify="center",state="normal",font=("Verdana",12))      
        
        def ok2():
            global bandera,letra
            from operacionalMatriz import deletMatriz
            from archivoLectura import lista
            #entry.focus_set()
            dato1.focus_set()
            dato2.focus_set()
            dato3.focus_set()
            dato4.focus_set()
            nombre=entry.get()#respuesta nombre 
            respuesta=dato1.get()#respuesta de X1
            respuesta1=dato2.get()#respuesta de Y1
            respuesta2=dato3.get()#respuesta de X2
            respuesta3=dato4.get()#respuesta de Y2
            
            if lista.buscar2(nombre)==True:
                if respuesta !="" and respuesta1 !="" and respuesta2 !="" and respuesta3 !="" and nombre !="":
                    VenLimpiar.destroy() 
                    deletMatriz(nombre,respuesta,respuesta1,respuesta2,respuesta3)
                    bandera=True
                    letra="Limpiar Zona "+str(respuesta)+","+str(respuesta1)+" "
                    letra+=""+str(respuesta2)+","+str(respuesta3)
                    menus()
                else:
                    messagebox.showerror(message="Por favor llene todos los cuadros de texto")
                    #limpiarVen()
            else:
                messagebox.showerror(message="El nombre la matriz no existe")
        boton=Button(VenLimpiar,text="Eliminar", command=ok2)
        boton.place(relx=0.35,rely=0.8,relwidth=0.3,relheight=0.1)
        boton.config(font=("verdana",12))        
    def venCuadraTri():
        from archivoLectura import lista
        root.destroy()
        VenLimpiar=Tk()
        VenLimpiar.title("Ingrese Los datos")
        VenLimpiar.geometry("320x320")

        def cerrar_app():
            VenLimpiar.destroy()
            menus()
            
        VenLimpiar.protocol("WM_DELETE_WINDOW", cerrar_app)           
        
        #VenLimpiar.config(bg="#ffffff")
        #ingresando los label de las coordenadas
        label=Label(VenLimpiar,text="Buscar Matriz:")
        label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        label.config(justify="center" , state="normal",font=("Verdana",12))

        if Archivo==True:   
            dato=lista.crearlist()
        else:
            dato=""
        
        entry=ttk.Combobox(VenLimpiar,state="readonly",values=dato)
        entry.grid(row=0,column=1,padx="5",pady="3")
        entry.config(justify="center",state="normal",font=("Verdana",12))   
        entry.place(relx=0.4,relwidth=0.5, relheight=0.10)     
        
        labelX1=Label(VenLimpiar,text="X1")
        labelX1.config(font=("verdana",12))
        labelX1.place(relx=0.25,rely=0.15)
        
        dato1=Entry(VenLimpiar)
        dato1.place(relx=0.2,rely=0.25,relwidth=0.2,relheight=0.10)
        dato1.config(justify="center",state="normal",font=("Verdana",12))
        
        coma1=Label(VenLimpiar,text=",")
        coma1.config(font=("verdana",12))
        coma1.place(relx=0.48,rely=0.30)
        
        parentesis1=Label(VenLimpiar,text="(")
        parentesis1.config(font=("verdana",32))
        parentesis1.place(relx=0.10,rely=0.20)

        parentesis2=Label(VenLimpiar,text=")")
        parentesis2.config(font=("verdana",32))
        parentesis2.place(relx=0.83,rely=0.20)
    
        #vocalM=Label(VenLimpiar,text="A")
        #vocalM.config(font=("verdana",18))
        #vocalM.place(relx=0.45,rely=0.38)
            
        dato2=Entry(VenLimpiar)
        dato2.place(relx=0.6,rely=0.25,relwidth=0.2,relheight=0.10)
        dato2.config(justify="center",state="normal",font=("Verdana",12))
                        
        labelY1=Label(VenLimpiar,text="Y1")
        labelY1.config(font=("verdana",12))
        labelY1.place(relx=0.65,rely=0.15)
            
        labelX2=Label(VenLimpiar,text="Alto")
        labelX2.config(font=("verdana",12))
        labelX2.place(relx=0.25,rely=0.5)
        
        labelY2=Label(VenLimpiar,text="Ancho")
        labelY2.config(font=("verdana",12))
        labelY2.place(relx=0.65,rely=0.5)

        coma2=Label(VenLimpiar,text="X")
        coma2.config(font=("verdana",12))
        coma2.place(relx=0.48,rely=0.6)
                        
        dato3=Entry(VenLimpiar)
        dato3.place(relx=0.2,rely=0.6,relwidth=0.2,relheight=0.10)
        dato3.config(justify="center",state="normal",font=("Verdana",12))
        
        dato4=Entry(VenLimpiar)
        dato4.place(relx=0.6,rely=0.6,relwidth=0.2,relheight=0.10)
        dato4.config(justify="center",state="normal",font=("Verdana",12))      
        
        def ok4():
            global bandera,letra,tipoL
            from archivoLectura import lista
            from operacionalMatriz import agregar_R
            from operacionalMatriz import matriz
            
            #entry.focus_set()
            dato1.focus_set()
            dato2.focus_set()
            dato3.focus_set()
            nombre=entry.get()#respuesta nombre 
            respuesta=dato1.get()#respuesta de X1
            respuesta1=dato2.get()#respuesta de Y1
            respuesta2=dato3.get()#respuesta de Alto
            respuesta3=dato4.get()#respuesta de Ancho
            #matriz(nombre)
            if lista.buscar2(nombre)==True:
                dato=lista.buscar3(nombre)
                fila=(int(respuesta)+int(respuesta3))-1
                columna=(int(respuesta1)+int(respuesta2))-1
                if fila !=columna:
                    if columna<= int(dato[2]) and fila<=int(dato[1]):
                        if respuesta !="" and respuesta1 !="" and respuesta2 !="" and nombre !="":
                                VenLimpiar.destroy() 
                                agregar_R(nombre,respuesta,respuesta1,str(columna),str(fila))
                                bandera=True
                                letra="Agregar Rectangulo "+str(respuesta)+","+str(respuesta1)+" "
                                letra+=""+str(respuesta2)+"x"+str(respuesta3)
                                menus()
                        else:
                                messagebox.showerror(message="Por favor llene todos los cuadros de texto")
                                #limpiarVen()   
                    else:
                            messagebox.showerror(message="La fila o Columuna es mayor de la matriz")    
                else:
                    messagebox.showerror(message="Lo sentimos pero esto es un cuadrado")             
            else:  
                messagebox.showerror(message="El nombre de la matriz no existe")       
        boton=Button(VenLimpiar,text="Agregar", command=ok4)
        boton.place(relx=0.35,rely=0.8,relwidth=0.3,relheight=0.1)
        boton.config(font=("verdana",12))
        #venP.destroy()    
        VenLimpiar.mainloop()                              
    def agregarT_Ven():
        from archivoLectura import lista
        root.destroy()
        VenLimpiar=Tk()
        VenLimpiar.title("Ingrese Coordenada")
        VenLimpiar.geometry("320x320")

        def cerrar_app():
            VenLimpiar.destroy()
            menus()
            
        VenLimpiar.protocol("WM_DELETE_WINDOW", cerrar_app)           
        
        #VenLimpiar.config(bg="#ffffff")
        #ingresando los label de las coordenadas
        label=Label(VenLimpiar,text="Buscar Matriz:")
        label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        label.config(justify="center" , state="normal",font=("Verdana",12))
        label.place(relx=0.03,rely=0.1,)
        
        if Archivo==True:   
            dato=lista.crearlist()
        else:
            dato=""
        
        entry=ttk.Combobox(VenLimpiar,state="readonly",values=dato)
        entry.grid(row=0,column=1,padx="5",pady="3")
        entry.config(justify="center",state="normal",font=("Verdana",12))   
        entry.place(relx=0.45,rely=0.1,relwidth=0.5, relheight=0.10)     
        
        labelX1=Label(VenLimpiar,text="X1")
        labelX1.config(font=("verdana",12))
        labelX1.place(relx=0.25,rely=0.25)
        
        dato1=Entry(VenLimpiar)
        dato1.place(relx=0.2,rely=0.35,relwidth=0.2,relheight=0.10)
        dato1.config(justify="center",state="normal",font=("Verdana",12))
        
        coma1=Label(VenLimpiar,text=",")
        coma1.config(font=("verdana",12))
        coma1.place(relx=0.48,rely=0.4)
        
        parentesis1=Label(VenLimpiar,text="(")
        parentesis1.config(font=("verdana",32))
        parentesis1.place(relx=0.10,rely=0.30)

        parentesis2=Label(VenLimpiar,text=")")
        parentesis2.config(font=("verdana",32))
        parentesis2.place(relx=0.83,rely=0.30)
        
        labelY1=Label(VenLimpiar,text="Y1")
        labelY1.config(font=("verdana",12))
        labelY1.place(relx=0.65,rely=0.25)
        
        vocalM=Label(VenLimpiar,text="Longuitud de Elementos")
        vocalM.config(font=("verdana",12))
        vocalM.place(relx=0.20,rely=0.50)
            
        dato2=Entry(VenLimpiar)
        dato2.place(relx=0.6,rely=0.35,relwidth=0.2,relheight=0.10)
        dato2.config(justify="center",state="normal",font=("Verdana",12))
 
        dato3=Entry(VenLimpiar)
        dato3.place(relx=0.4,rely=0.6,relwidth=0.2,relheight=0.10)
        dato3.config(justify="center",state="normal",font=("Verdana",12))        
        def ok5():
            from archivoLectura import lista
            from operacionalMatriz import agregar_T
            #entry.focus_set()
            dato1.focus_set()
            dato2.focus_set()
            dato3.focus_set()
            nombre=entry.get()#respuesta nombre 
            respuesta=dato1.get()#respuesta de X1
            respuesta1=dato2.get()#respuesta de Y1
            respuesta2=dato3.get()#respuesta de X2
            if lista.buscar2(nombre)==True:
                dato=lista.buscar3(nombre)
                fila=(int(respuesta)+int(respuesta2))-1
                columna=(int(respuesta1)+int(respuesta2))-1
                if columna<= int(dato[2]) and fila<=int(dato[1]):
                    if respuesta !="" and respuesta1 !="" and respuesta2 !="" and nombre !="":
                        VenLimpiar.destroy() 
                        agregar_T(nombre,respuesta,respuesta1,str(fila),str(columna))
                        bandera=True
                        letra="Agregar Triangulo Rectangulo "+str(respuesta)+","+str(respuesta1)+" "
                        letra+=""+str(respuesta2)
                        menus()
                    else:
                        messagebox.showerror(message="Por favor llene todos los cuadros de texto")
                        #limpiarVen()   
                else:
                    messagebox.showerror(message="La fila o Columuna es mayor de la matriz")    
            else:  
                messagebox.showerror(message="El nombre de la matriz no existe")   
            print()
        boton=Button(VenLimpiar,text="Agregar", command=ok5)
        boton.place(relx=0.35,rely=0.8,relwidth=0.3,relheight=0.1)
        boton.config(font=("verdana",12))
        #venP.destroy()    
        VenLimpiar.mainloop()       
    def agregarL_Ven():
        from archivoLectura import lista
        root.destroy()
        VenLimpiar=Tk()
        VenLimpiar.title("Ingrese Coordenada")
        VenLimpiar.geometry("320x320")

        def cerrar_app():
            VenLimpiar.destroy()
            menus()
            
        VenLimpiar.protocol("WM_DELETE_WINDOW", cerrar_app)   
        #VenLimpiar.config(bg="#ffffff")
        #ingresando los label de las coordenadas
        label=Label(VenLimpiar,text="Buscar Matriz:")
        label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        label.config(justify="center" , state="normal",font=("Verdana",12))
        label.place(relx=0.03,rely=0.1,)
        
        if Archivo==True:   
            dato=lista.crearlist()
        else:
            dato=""
        
        entry=ttk.Combobox(VenLimpiar,state="readonly",values=dato)
        entry.grid(row=0,column=1,padx="5",pady="3")
        entry.config(justify="center",state="normal",font=("Verdana",12))   
        entry.place(relx=0.45,rely=0.1,relwidth=0.5, relheight=0.10)     
        
        labelX1=Label(VenLimpiar,text="X1")
        labelX1.config(font=("verdana",12))
        labelX1.place(relx=0.25,rely=0.25)
        
        dato1=Entry(VenLimpiar)
        dato1.place(relx=0.2,rely=0.35,relwidth=0.2,relheight=0.10)
        dato1.config(justify="center",state="normal",font=("Verdana",12))
        
        coma1=Label(VenLimpiar,text=",")
        coma1.config(font=("verdana",12))
        coma1.place(relx=0.48,rely=0.4)
        
        parentesis1=Label(VenLimpiar,text="(")
        parentesis1.config(font=("verdana",32))
        parentesis1.place(relx=0.10,rely=0.30)

        parentesis2=Label(VenLimpiar,text=")")
        parentesis2.config(font=("verdana",32))
        parentesis2.place(relx=0.83,rely=0.30)
        
        labelY1=Label(VenLimpiar,text="Y1")
        labelY1.config(font=("verdana",12))
        labelY1.place(relx=0.65,rely=0.25)
        
        vocalM=Label(VenLimpiar,text="cantidad de Elementos")
        vocalM.config(font=("verdana",12))
        vocalM.place(relx=0.20,rely=0.50)
            
        dato2=Entry(VenLimpiar)
        dato2.place(relx=0.6,rely=0.35,relwidth=0.2,relheight=0.10)
        dato2.config(justify="center",state="normal",font=("Verdana",12))
 
        dato3=Entry(VenLimpiar)
        dato3.place(relx=0.4,rely=0.6,relwidth=0.2,relheight=0.10)
        dato3.config(justify="center",state="normal",font=("Verdana",12))
             
        def ok3(): 
            from archivoLectura import lista
            from operacionalMatriz import agregar_H
            from operacionalMatriz import matriz
            global bandera,tipoL
            #entry.focus_set()
            dato1.focus_set()
            dato2.focus_set()
            dato3.focus_set()
            nombre=entry.get()#respuesta nombre 
            respuesta=dato1.get()#respuesta de X1
            respuesta1=dato2.get()#respuesta de Y1
            respuesta2=dato3.get()#respuesta de X2
            #matriz(nombre)
            if lista.buscar2(nombre)==True:
                dato=lista.buscar3(nombre)
                if tipoL=="horizontal":
                    tamano=(int(respuesta1)+int(respuesta2))-1
                    if tamano <= int(dato[2]):
                        if respuesta !="" and respuesta1 !="" and respuesta2 !="" and nombre !="":
                            VenLimpiar.destroy() 
                            agregar_H(nombre,respuesta,respuesta1,respuesta,str(tamano))
                            bandera=True
                            letra="Agregar Linea Horizontal "+str(respuesta)+","+str(respuesta1)+" "
                            letra+=""+str(respuesta2)
                            menus()
                        else:
                            messagebox.showerror(message="Por favor llene todos los cuadros de texto")
                            #limpiarVen()   
                    else:
                        messagebox.showerror(message="La cantidad de elementos supera el tamaño de la fila de la matriz")         
                elif tipoL=="vertical":
                    tamano=(int(respuesta2)+int(respuesta))-1
                    if tamano <= int(dato[1]):
                        if respuesta !="" and respuesta1 !="" and respuesta2 !="" and nombre !="":
                            VenLimpiar.destroy() 
                            agregar_H(nombre,respuesta,respuesta1,str(tamano),respuesta1)
                            bandera=True
                            letra="Agregar Linea Horizontal "+str(respuesta)+","+str(respuesta1)+" "
                            letra+=""+str(respuesta2)
                            menus()
                        else:
                            messagebox.showerror(message="Por favor llene todos los cuadros de texto")
                            #limpiarVen()   
                    else:
                        messagebox.showerror(message="La cantidad de elementos supera el tamaño de la fila de la matriz")  
            else:  
                messagebox.showerror(message="El nombre de la matriz no existe")            
        boton=Button(VenLimpiar,text="Agregar", command=ok3)
        boton.place(relx=0.35,rely=0.8,relwidth=0.3,relheight=0.1)
        boton.config(font=("verdana",12))
        #venP.destroy()    
        VenLimpiar.mainloop()
    def unioAB():
        global tipoL,bandera,letra
        root.destroy()
        tipoL="union"
        bandera=True
        letra="Resultado Union A,B"
        ventana2()
    def interseccionAB():
        global tipoL,bandera,letra
        root.destroy()
        tipoL="interseccion"
        bandera=True
        letra="Resultado Interseccion A,B"
        ventana2()
    def diferencia():
        global tipoL,bandera,letra
        root.destroy()
        tipoL="diferencia"
        bandera=True
        letra="Resultado Diferencia A,B"
        ventana2()     
    def simetrica():
        global tipoL,bandera,letra
        root.destroy()
        tipoL="simetrica"
        bandera=True
        letra="Resultado Diferencia Simetrica A,B"
        ventana2()                          
    def saberBandera():
        global Archivo
        Archivo=True
    def ventana2():
        global Archivo
        from archivoLectura import lista
        ven=Tk()
        ven.geometry("500x250")  
        ven.title("selecciones Dato")

        def cerrar_app():
            ven.destroy()
            menus()
            
        ven.protocol("WM_DELETE_WINDOW", cerrar_app)            
         
        if Archivo==True:
            dato=lista.crearlist()
        else:
            dato=""
            
        labelA1= Label(ven,text="Elija la Primera Matriz:")
        labelA1.config(font=("verdana",16))
        labelA1.place(relx=0.05,rely=0.10)
        
        combo1= ttk.Combobox(ven,state="readonly", values=dato)
        combo1.config(font=("verdana",12))
        combo1.place(relx=0.07,rely=0.25,relwidth=0.6)
        
        labelA2=Label(ven,text="Elija la Segunda Matriz:")
        labelA2.config(font=("verdana",16))
        labelA2.place(relx=0.05,rely=0.35)
        
        combo2= ttk.Combobox(ven,state="readonly",values=dato)
        combo2.config(font=("verdana",12))
        combo2.place(relx=0.07,rely=0.5,relwidth=0.6)        
        
        def archivoAgregar():
            global Archivo
            from archivoLectura2 import lecturaM
            from archivoLectura import lista
            ven.destroy()
            lecturaM()
            saberBandera()
            ventana2()
            '''
            combo1.set("")
            combo2.set("")
            data=lista.crearlist()
            combo1["values"]=data
            combo2["values"]=data
            '''
            print()
        
        boton=Button(ven,text="Agregar\nnueva\nMatriz", command=archivoAgregar)
        boton.place(relx=0.7,rely=0.30,relwidth=0.25,relheight=0.25)
        boton.config(font=("verdana",12),bg="#b8daba")
        def generarMatriz():
            #global bandera
            from archivoLectura import lista
            from operacionalMatriz import Union,intersection,dif,simetria
            if combo1.get() !="" and combo2.get() !="":
                matriz1=combo1.get()
                matriz2=combo2.get()
                dato1=lista.buscar3(matriz1)
                dato3=int(dato1[1])+int(dato1[2])
                dato2=lista.buscar3(matriz2)
                dato4=int(dato2[1])+int(dato2[2])
                if dato1[1]==dato2[1] and dato1[2]==dato2[2]:
                    fila=int(dato1[1])
                    columna=int(dato1[2])
                elif dato3>dato4:
                    fila=int(dato1[1])
                    columna=int(dato1[2])
                elif dato3<dato4:
                    fila=int(dato2[1])
                    columna=int(dato2[2])
                    
                if tipoL== "union":
                    Union(matriz1,matriz2,fila,columna,dato1[1],dato1[2],dato2[1],dato2[2])
                    ven.destroy()
                    menus()
                elif tipoL=="interseccion":
                    intersection(matriz1,matriz2,fila,columna,dato1[1],dato1[2],dato2[1],dato2[2])
                    ven.destroy()
                    menus()
                elif tipoL=="diferencia":
                    dif(matriz1,matriz2,fila,columna,dato1[1],dato1[2],dato2[1],dato2[2])
                    ven.destroy()
                    menus()  
                elif tipoL=="simetrica":   
                    simetria(matriz1,matriz2,fila,columna,dato1[1],dato1[2],dato2[1],dato2[2])
                    ven.destroy()
                    menus()             
            else:
                messagebox.showerror(message="aun no has selecionado el nombre de las Matrices a Comparar")
        boton1=Button(ven,text="Generar matriz", command=generarMatriz)
        boton1.place(relx=0.17,rely=0.75,relwidth=0.3,relheight=0.15)
        boton1.config(font=("verdana",12),bg="#b8daba")
        
        boton2=Button(ven,text="Cancel", command=archivoAgregar)
        boton2.place(relx=0.50,rely=0.75,relwidth=0.3,relheight=0.15)
        boton2.config(font=("verdana",12),bg="#b8daba")
        ven.mainloop()
    def docPdf():
        root.destroy()
        lector=Tk()
        lector.geometry("1000x700")
        lector.title("Lector de PDF")
        
        def cerrar_app():
            lector.destroy()
            menus()
            
        lector.protocol("WM_DELETE_WINDOW", cerrar_app)
        v1=pdf.ShowPdf().pdf_view(lector,pdf_location="Documentacion/Documentacion_201602983.pdf",width=100,height=100)
        v1.pack()
        v1.place(relx=0.1,rely=0,relwidth=0.75,relheight=1)
        #print()  
        lector.mainloop() 
    def Info():
        panel= Tk()
        panel.geometry("750x320")
        panel.title("Informacion del Estudiante")
        def cerrar_app():
            panel.destroy()
            
        panel.protocol("WM_DELETE_WINDOW", cerrar_app)        
        tile=Label(panel,text="Jaime Alejandro Armira Us\n201602983\nIntroduccion a la Programacion y Computacion 2 Seccion \"D\"\nIngenieria en Ciencias y Sistemas\nPrimer Semestre 2021")
        tile.pack()
        tile.config(font=("Arial",20))
        tile.place(relx=0,rely=0.05,relwidth=1, relheight=1)
        panel.mainloop()
        print()
    def report():
        from HTML import pageweb
        pageweb()
    root=Tk()
    root.geometry('1200x600')
    root.title("Menu Principal")
    menubar=Menu(root)
    menubar.config(font=("verdana",48))
    root.configure(menu=menubar)        

    #creando un frame
    ventana1=Frame(root)
    ventana1.pack()
    ventana1.config(bg="#ffffff",bd=5,borderwidth=1)
    ventana1.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
    ventana1.place(relx=0.02, rely=0.04,relwidth=0.96,relheight=0.92 )
    
    tile=Label(root,text="Panel")
    tile.pack()
    tile.config(font=("Arial",24),bg="#6fa780")
    tile.place(relx=0.05,rely=0.02)
    #crear contenedor de imagen 1
    imageVen1=Frame(ventana1)
    imageVen1.pack()
    imageVen1.config(bg="#646464")
    imageVen1.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
    imageVen1.place(relx=0.05,rely=0.10, relwidth=0.4, relheight=0.8)

    #crear contenedor de imagen 2
    imageVen2=Frame(ventana1)
    imageVen2.pack()
    imageVen2.config(bg="#646464",width=400,height=400)
    imageVen2.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
    imageVen2.place(relx=0.55,rely=0.10, relwidth=0.4, relheight=0.8)  
    
    scroll=Scrollbar(imageVen1,orient='horizontal')
    scroll.pack(side=BOTTOM,fill=X,expand=True)
    scroll.place(relx=0,rely=0.96,relwidth=1,relheight=0.05)

    scroll1=Scrollbar(imageVen2,orient='horizontal')
    scroll1.pack()
    scroll1.place(relx=0,rely=0.96,relwidth=1,relheight=0.05)    

        
    if bandera==True:
        imagen=imagenSize("Original.dot.png")
        labelImage1=Label(imageVen1,image=imagen,bd=0)    
        labelImage1.pack()
        labelImage1.config(bg="#646464")
        labelImage1.place(relx=0,rely=0)
        #width=57, height=27
        
        imagen2=imagenSize("Resultado.dot.png")
        labelImage2=Label(imageVen2,image=imagen2,bd=0)    
        labelImage2.pack()
        labelImage2.config(bg="#646464")
        labelImage2.place(relx=0,rely=0)
        #width=57, height=27
        #label2['text']=letra

    #label para el frame ventana1
    label1=Label(ventana1,text="=")
    label1.pack()
    label1.config(font=("verdana",48),bg="#ffffff")
    label1.place(relx=0.48,rely=0.45)
    
    label2=Label(ventana1,text="Imagen Matriz Original")
    label2.pack()
    label2.config(font=("verdana",18),bg="#ffffff")
    label2.place(relx=0.1,rely=0.9)
    
    labelM2=Label(ventana1,text="Imagen Matriz Resultado")
    labelM2.pack()
    labelM2.config(font=("verdana",18),bg="#ffffff")
    if bandera ==True:
        labelM2['text']=letra
    labelM2.place(relx=0.65,rely=0.9)
    #Creando el menu de operaciones 
    menuArchivo=Menu(menubar, tearoff=0)
    menuArchivo.add_command(label="Rotacion Horizontal de una Imagen",command=rotacionH)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Rotación Vertical de una Imagen",command=rotacionV)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Transpuesta de una Imagen",command=transpuesta)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Limpiar la Zona de una Imagen", command=limpiarVen)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Agregar Línea Horizontal a una Imagen",command=agregarH)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Agregar Línea Vertical a una Imagen",command=agregarV)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Agregar rectangulo",command=agregarRec)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Agregar Triángulo Rectangulo",command=agregarTRec)
    #menuArchivo.geometry("10x300")
    menuArchivo2=Menu(menubar,tearoff=0)
    menuArchivo2.add_command(label="Union A,B",command=unioAB)
    menuArchivo2.add_separator()
    menuArchivo2.add_command(label="Interseccion A,B",command=interseccionAB)
    menuArchivo2.add_separator()
    menuArchivo2.add_command(label="Diferencia A,B",command=diferencia)
    menuArchivo2.add_separator()
    menuArchivo2.add_command(label="Diferencia Simetrica A,B",command=simetrica)
    
    menuAyuda=Menu(menubar, tearoff=0)
    menuAyuda.add_cascade(label="Formacion del Estudiante",command=Info)
    menuAyuda.add_separator()
    menuAyuda.add_cascade(label="Documentacion del Programa",command=docPdf)
    
    menuOperacional=Menu(menubar,tearoff=0)
    menuOperacional.add_cascade(label="Operacion a Una imagen",menu=menuArchivo)
    menuOperacional.add_separator()
    menuOperacional.add_cascade(label="Operacion a Dos Imagenes",menu=menuArchivo2)
    #  Creando los titulos del menu
    menubar.add_cascade(label="Cargar Archivo", command=lectura)
    menubar.add_cascade(label="Operaciones",menu=menuOperacional)
    menubar.add_cascade(label="Reporte", command=report)
    menubar.add_cascade(label="Ayuda", menu=menuAyuda)
    root.mainloop()    

def principal():
    #global REPORT
    from inicio import reporte
    reporte()
    menus()
principal()
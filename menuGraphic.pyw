from tkinter import * 
respuesta=""
letra=""
bandera=False
def menus():
    global letra
    def lectura():
        from archivoLectura import lecturaM
        root.destroy()
        lecturaM()
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

    def limpiar():
        root.destroy
        limpiarVen()
        print("Limpiar")
    def agregarH():
        print("Agregar Linea Horizontal")
    def agregarV():
        print("Agregar Linea Vertical")
    def agregarRec():
        print("Agregar Rectangulo")
    def agregarTRec():
        print("Agregar Triangulo Rectangulo")
    def imagenSize(dato):
        imagen=PhotoImage(file=dato)
        imagen=imagen.zoom(1)
        imagen=imagen.subsample(1)
        return imagen
        #labelImage1['image']=imagen
    def busca():
        venP=Tk()
        label=Label(venP,text="Ingrese el nombre  de la Matriz")
        label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        label.config(justify="center" , state="normal",font=("Verdana",12))

        #creando la caja de texto 
        entry=Entry(venP)
        entry.grid(row=3,column=0,padx=5,pady=10)
        entry.config(justify="center",state="normal",font=("Verdana",12))

        def ok():
            global respuesta
            entry.focus_set()
            respuesta=entry.get()
            venP.destroy() 
        #
        boton=Button(venP,text="Buscar", command=ok)
        boton.grid(row=4, column=0, padx=5,pady=15)
        #venP.destroy()    
        venP.mainloop()
    
        #for a in lista.iterar():
        #print("rotacion Horizontal")
    def limpiarVen():
        VenLimpiar=Tk()
        VenLimpiar.title("Ingrese Coordenada")
        VenLimpiar.geometry("320x320")
        #ingresando los label de las coordenadas
        labelX1=Label(VenLimpiar,text="X1")
        labelX1.config(font=("verdana",12),bg="#ffffff")
        labelX1.place(relx=0.3,rely=0.15)
        
        dato1=Entry(VenLimpiar)
        dato1.place(relx=0.2,rely=0.25,relwidth=0.2,relheight=0.10)
        dato1.config(justify="center",state="normal",font=("Verdana",12))
        
        coma1=Label(VenLimpiar,text=",")
        coma1.config(font=("verdana",12),bg="#ffffff")
        coma1.place(relx=0.48,rely=0.30)
        
        parentesis1=Label(VenLimpiar,text="(")
        parentesis1.config(font=("verdana",32),bg="#ffffff")
        parentesis1.place(relx=0.10,rely=0.20)

        parentesis2=Label(VenLimpiar,text=")")
        parentesis2.config(font=("verdana",32),bg="#ffffff")
        parentesis2.place(relx=0.83,rely=0.20)
    
        dato2=Entry(VenLimpiar)
        dato2.place(relx=0.6,rely=0.25,relwidth=0.2,relheight=0.10)
        dato2.config(justify="center",state="normal",font=("Verdana",12))
                        
        labelY1=Label(VenLimpiar,text="Y1")
        labelY1.config(font=("verdana",12),bg="#ffffff")
        labelY1.place(relx=0.65,rely=0.15)
                
        labelX2=Label(VenLimpiar,text="X2")
        labelX2.config(font=("verdana",12),bg="#ffffff")
        labelX2.place(relx=0.3,rely=0.6)

        labelY2=Label(VenLimpiar,text="Y2")
        labelY2.config(font=("verdana",12),bg="#ffffff")
        labelY2.place(relx=0.65,rely=0.6)
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
    if bandera ==True:
        label2['text']=letra
    
    label2=Label(ventana1,text="Imagen Matriz Resultado")
    label2.pack()
    label2.config(font=("verdana",18),bg="#ffffff")
    label2.place(relx=0.65,rely=0.9)
    #Creando el menu de operaciones 
    menuArchivo=Menu(menubar, tearoff=0)
    menuArchivo.add_command(label="Rotacion Horizontal de una Imagen",command=rotacionH)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Rotación Vertical de una Imagen",command=rotacionV)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Transpuesta de una Imagen",command=transpuesta)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Limpiar la Zona de una Imagen", command=limpiar)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Agregar Línea Horizontal a una Imagen",command=agregarH)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Agregar Línea Vertical a una Imagen",command=agregarV)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Agregar rectangulo",command=agregarRec)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Agregar Triángulo Rectangulo",command=agregarTRec)
    #menuArchivo.geometry("10x300")
    #  Creando los titulos del menu
    menubar.add_cascade(label="Cargar Archivo", command=lectura)
    menubar.add_cascade(label="Operaciones",menu=menuArchivo)
    menubar.add_cascade(label="Reporte")
    menubar.add_cascade(label="Ayuda")
    root.mainloop()    
menus()
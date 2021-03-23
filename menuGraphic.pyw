from tkinter import * 
respuesta=""
def menus():
    def lectura():
        from archivoLectura import lecturaM
        root.destroy()
        lecturaM()
        menus()
        #print("hola mundo")
    def rotacionH():
        from archivoLectura import lista
        from operacionalMatriz import horizontal
        root.destroy()
        busca()
        horizontal(respuesta)
        print(respuesta)
        menus()
    def rotacionV():
        print("rotacion Vertical")
    def transpuesta():
        print("transpuesta")
    def limpiar():
        print("Limpiar")
    def agregarH():
        print("Agregar Linea Horizontal")
    def agregarV():
        print("Agregar Linea Vertical")
    def agregarRec():
        print("Agregar Rectangulo")
    def agregarTRec():
        print("Agregar Triangulo Rectangulo")
    def busca():
        venP=Tk()
        label=Label(venP,text="Ingrese el nombre  de la Matriz")
        label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        label.config(justify="center" , state="normal",font=("Verdana",12))
    
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
    
    root=Tk()
    root.geometry('600x300')
    root.title("Menu Principal")
    menubar=Menu(root)
    root.configure(menu=menubar)
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
    menubar.configure()
    root.mainloop()    
menus()
from tkinter import * 
def lectura():
    from archivoLectura import lectura
    lectura()
   #print("hola mundo")
def rotacionH():
    from archivoLectura import lista
    for a in lista.iterar():
        print(a)
    #print("rotacion Horizontal")
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
# Creando los titulos del menu
menubar.add_cascade(label="Cargar Archivo", command=lectura)
menubar.add_cascade(label="Operaciones",menu=menuArchivo)
menubar.add_cascade(label="Reporte")
menubar.add_cascade(label="Ayuda")
menubar.configure()
root.mainloop()    

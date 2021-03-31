from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def lecturaM():
    import xml.etree.ElementTree as ET
    from archivoLectura import lista
    #from menuGraphic import bandera
    leer=Tk()
    leer.title("Abrir Archivo")
    leer.withdraw()
    leer.filename=filedialog.askopenfilename(initialdir="c:/Desktop", title="Selelcionar Archivo",filetypes=(("Archivo xml","*.xml"),("all files","*.*")))
    #leer.destroy()
    
    if leer.filename == "":
        messagebox.showerror(message="Archivo no seleccionado")
        leer.destroy()
    else:
        leer.destroy()
        Archivo=open(leer.filename,"r")
        tree=ET.parse(Archivo)
        raiz=tree.getroot()
        nombre=""
        columna=""
        filas=""
        image=""
        for hijo in raiz:
            if hijo.tag == "matriz":
                for nieto in hijo:
                    if nieto.tag=="nombre":
                        nombre=nieto.text
                        print(nieto.text)
                    elif nieto.tag=="filas":
                        filas=nieto.text
                        print(nieto.text)
                    elif nieto.tag=="columnas":
                        columna=nieto.text
                        print(nieto.text)
                    elif nieto.tag=="imagen":
                        image=nieto.text
                        image=image.replace(" ", "")
                        image=image.replace("\t","")
                        print(image)
                    else: continue
                if nombre!="" and filas!="" and columna!="" and image!="":
                    lista.add(nombre,filas,columna,image)
                    nombre=""
                    filas=""
                    columna=""
                    image=""
                else:
                    if nombre!="":
                        print("no existe el nombre de la matriz")
                        continue
            else:
                continue
    leer.mainloop()
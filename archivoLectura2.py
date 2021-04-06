from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def lecturaM():
    import xml.etree.ElementTree as ET
    from archivoLectura import lista
    from archivoLectura import fechaHora
    from inicio import report
    #from menuGraphic import bandera
    leer=Tk()
    leer.title("Abrir Archivo")
    leer.withdraw()
    leer.filename=filedialog.askopenfilename(initialdir="c:/Desktop", title="Selelcionar Archivo",filetypes=(("Archivo xml","*.xml"),("all files","*.*")))
    #leer.destroy()
    def cerrar_app():
            leer.destroy()
            #menus()
            
    leer.protocol("WM_DELETE_WINDOW", cerrar_app)      
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
                        if nieto.text!="":
                            nombre=nieto.text
                            print(nieto.text)
                        else:
                            report.add(''+str(fechaHora())+'Error: una matriz no contiene nombre')
                    elif nieto.tag=="filas":
                        if (nieto.text).isdigit():
                            filas=nieto.text
                            #print(nieto.text)
                        elif nieto.text=="":
                            report.add(''+str(fechaHora())+'Error: la fila de la matriz '+nombre+' no contiene un numero')
                        else:
                            report.add(''+str(fechaHora())+'Error: la fila de la matriz '+nombre+' no es un numero')
                    elif nieto.tag=="columnas":
                        if (nieto.text).isdigit():
                            columna=nieto.text
                            #print(nieto.text)
                        elif nieto.text=="":
                            report.add(''+str(fechaHora())+'Error: la Columna de la matriz '+nombre+' no contiene un numero')
                        else:
                            report.add(''+str(fechaHora())+'Error: la Columna de la matriz '+nombre+' no es un numero')
                            #print("no es un numero")
                    elif nieto.tag=="imagen":
                        if nieto.text!="":
                            image=nieto.text
                            image=image.replace(" ", "")
                            image=image.replace("\t","")
                            print(image)
                        else:
                            report.add(''+str(fechaHora())+'Error: la matriz no contiene una imagen para procesar')
                    else: continue
                if nombre!="" and filas!="" and columna!="" and image!="":
                    dato=verific(image)
                    if int(filas)==dato[0] and int(columna)==dato[1]:
                        if lista.buscar2(nombre)==False:
                            lista.add(nombre,filas,columna,image)
                            mensje=''+str(fechaHora())+''+nombre+' - Espacios LLenos:'+str(dato[2])+' - Espacios Vacios:'+str(dato[3])
                            report.add(mensje) 
                            print(report.tamaño)
                            nombre=""
                            filas=""
                            columna=""
                            image=""
                        else:
                             report.add(''+str(fechaHora())+'Error: No se pudo guardar La matriz '+str(nombre)+' porque ya existe')
                             continue
                    else:
                        report.add(''+str(fechaHora())+'Error: No se pudo guardar La matriz '+str(nombre)+' fila o columna no coicide con la Imagen')
                        continue
                else:
                    report.add(''+str(fechaHora())+'Error: No se pudo guardar la matriz hace falta un elemento')
                    continue
            else:
                report.add(''+str(fechaHora())+'Error: No contiene tag "matriz" una de  de las matrices archivo .xml')
                for nieto in hijo:
                    if nieto.tag=="nombre":
                        if nieto.text!="":
                            nombre=nieto.text
                            print(nieto.text)
                        else:
                            report.add(''+str(fechaHora())+'Error: una matriz no contiene nombre')
                    elif nieto.tag=="filas":
                        if (nieto.text).isdigit():
                            filas=nieto.text
                            #print(nieto.text)
                        elif nieto.text=="":
                            report.add(''+str(fechaHora())+'Error: la fila de la matriz '+nombre+' no contiene un numero')
                        else:
                            report.add(''+str(fechaHora())+'Error: la fila de la matriz '+nombre+' no es un numero')
                    elif nieto.tag=="columnas":
                        if (nieto.text).isdigit():
                            columna=nieto.text
                            #print(nieto.text)
                        elif nieto.text=="":
                            report.add(''+str(fechaHora())+'Error: la Columna de la matriz '+nombre+' no contiene un numero')
                        else:
                            report.add(''+str(fechaHora())+'Error: la Columna de la matriz '+nombre+' no es un numero')
                            #print("no es un numero")
                    elif nieto.tag=="imagen":
                        if nieto.text!="":
                            image=nieto.text
                            image=image.replace(" ", "")
                            image=image.replace("\t","")
                            print(image)
                        else:
                            report.add(''+str(fechaHora())+'Error: la matriz no contiene una imagen para procesar')
                    else: continue
                if nombre!="" and filas!="" and columna!="" and image!="":
                    dato=verific(image)
                    if int(filas)==dato[0] and int(columna)==dato[1]:
                        if lista.buscar2(nombre)==False:
                            lista.add(nombre,filas,columna,image)
                            mensje=''+str(fechaHora())+''+nombre+' - Espacios LLenos:'+str(dato[2])+' - Espacios Vacios:'+str(dato[3])
                            report.add(mensje) 
                            print(report.tamaño)
                            nombre=""
                            filas=""
                            columna=""
                            image=""
                        else:
                             report.add(''+str(fechaHora())+'Error: No se pudo guardar La matriz '+str(nombre)+' porque ya existe')
                             continue
                    else:
                        report.add(''+str(fechaHora())+'Error: No se pudo guardar La matriz '+str(nombre)+' fila o columna no coicide con la Imagen')
                        continue
                else:
                    report.add(''+str(fechaHora())+'Error: No se pudo guardar la matriz hace falta un elemento')
                    continue
        Archivo.close()
    leer.mainloop()
def verific(picture):
    from listaSimpleAuxiliar import listaEnlazadaMatriz as ListaAux
    matrizOriginal=ListaAux()
    picture= picture.split("\n")
    picture.pop(0)
    numero=int(len(picture))
    picture.pop(numero-1)
    columna=int(len(picture[0]))
    fila=int(len(picture))
    #picture=picture.remove("")
    for x in range(fila-1):
        for y in range(columna-1):
            if picture[x][y]=="*":
                matrizOriginal.add(x+1,y+1,picture[x][y]) 
    llenos=matrizOriginal.tamaño
    vacios=(fila*columna)-matrizOriginal.tamaño 
    return fila,columna,llenos,vacios 
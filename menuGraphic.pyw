from tkinter import * 
root=Tk()
root.geometry('600x300')
menubar=Menu(root)
root.configure(menu=menubar)
menuArchivo=Menu(menubar, tearoff=0)

# Creando los titulos del menu
menubar.add_cascade(label="Cargar Archivo")
menubar.add_cascade(label="Operaciones")
menubar.add_cascade(label="Reporte")
menubar.add_cascade(label="Ayuda")
root.mainloop()    

import graphviz
from graphviz import Digraph
from graphviz import Source
from graphviz import render
import os.path as path
import os
def crearDot(lista,fila,columna,sizeMatriz,name):
    graph='digraph {\n\ttbl [\n\tsize="4,4"\n\tshape=plaintext\n\tlabel=<\n\n\t\t'
    graph+='<table border="0" color="green" cellpadding="10" cellborder="1" cellspacing="0">\n\t'
    graph1=''
    for x in range(fila+1):
        graph1+='<tr>'
        for y in range(columna+1):
            if x==0 and y==0:
                graph1+='<td bgcolor = "red" color="black"> A </td>'
            elif x==0 and y>0:
                graph1+='<td color="green">'+str(y)+'</td>'
            elif x>0 and y==0:
                graph1+='<td color="green"> '+str(x)+' </td>'
            else:
                if lista.buscar(x,y)==True:
                    graph1+='<td color="blue"> * </td>'
                else:
                    graph1+='<td color="blue">   </td>'
            if y==columna:
                graph1+='</tr>\n\t\t\t'
    graph2='</table>\n\t\t>];\n}' 
    imagen=graph+graph1+graph2
    #f= open(name+".dot","w+")
    #f.write(imagen)
    #f.close()   
    #os.system("fdp -Tpng -o "+name+".png "+name+".dot")
    Grafico(imagen,name)   
def crearDot2(lista,fila,columna,sizeMatriz,name,x1,y1,x2,y2):
    graph='digraph {\n\ttbl [\n\tsize="4,4"\n\tshape=plaintext\n\tlabel=<\n\n\t\t'
    graph+='<table border="0" color="green" cellpadding="10" cellborder="1" cellspacing="0">\n\t'
    graph1=''
    for x in range(fila+1):
        graph1+='<tr>'
        for y in range(columna+1):
            if x==0 and y==0:
                graph1+='<td bgcolor = "red" color="black"> A </td>'
            elif x==0 and y>0:
                graph1+='<td color="green">'+str(y)+'</td>'
            elif x>0 and y==0:
                graph1+='<td color="green"> '+str(x)+' </td>'
            else:
                if lista.buscar(x,y)==True:
                    graph1+='<td color="blue"> * </td>'
                else:
                    if x>=int(x1) and  x<=int(x2) and y>=int(y1) and y<=int(y2):
                        graph1+='<td color="blue" bgcolor="#eeeeee">   </td>'
                    else:    
                        graph1+='<td color="blue">   </td>'
            if y==columna:
                graph1+='</tr>\n\t\t\t'
    graph2='</table>\n\t\t>];\n}' 
    imagen=graph+graph1+graph2
    #f= open(name+".dot","w+")
    #f.write(imagen)
    #f.close()   
    #os.system("fdp -Tpng -o "+name+".png "+name+".dot")
    Grafico(imagen,name)       
def crearDot3(lista,fila,columna,sizeMatriz,name,x1,y1,x2,y2):
    graph='digraph {\n\ttbl [\n\tsize="4,4"\n\tshape=plaintext\n\tlabel=<\n\n\t\t'
    graph+='<table border="0" color="green" cellpadding="10" cellborder="1" cellspacing="0">\n\t'
    graph1=''
    for x in range(fila+1):
        graph1+='<tr>'
        for y in range(columna+1):
            if x==0 and y==0:
                graph1+='<td bgcolor = "red" color="black"> A </td>'
            elif x==0 and y>0:
                graph1+='<td color="green">'+str(y)+'</td>'
            elif x>0 and y==0:
                graph1+='<td color="green"> '+str(x)+' </td>'
            else:
                if lista.buscar(x,y)==True:
                    if x>=int(x1) and  x<=int(x2) and y>=int(y1) and y<=int(y2):
                        graph1+='<td color="blue" bgcolor="#eeeeee"> * </td>'
                    else:
                        graph1+='<td color="blue"> * </td>'
                else:
                    graph1+='<td color="blue">   </td>'
            if y==columna:
                graph1+='</tr>\n\t\t\t'
    graph2='</table>\n\t\t>];\n}' 
    imagen=graph+graph1+graph2
    #f= open(name+".dot","w+")
    #f.write(imagen)
    #f.close()   
    #os.system("fdp -Tpng -o "+name+".png "+name+".dot")    
    Grafico(imagen,name) 
def crearDot4(lista,fila,columna,sizeMatriz,name,x1,y1,x2,y2):
    graph='digraph {\n\ttbl [\n\tsize="4,4"\n\tshape=plaintext\n\tlabel=<\n\n\t\t'
    graph+='<table border="0" color="green" cellpadding="10" cellborder="1" cellspacing="0">\n\t'
    graph1=''
    for x in range(fila+1):
        graph1+='<tr>'
        for y in range(columna+1):
            if x==0 and y==0:
                graph1+='<td bgcolor = "red" color="black"> A </td>'
            elif x==0 and y>0:
                graph1+='<td color="green">'+str(y)+'</td>'
            elif x>0 and y==0:
                graph1+='<td color="green"> '+str(x)+' </td>'
            else:
                if lista.buscar(x,y)==True:
                    if x==int(x1) and y>=int(y1) and y<=int(y2):
                        graph1+='<td color="blue" bgcolor="#eeeeee"> * </td>'
                    elif y==int(y1) and x>=int(x1) and x<=int(x2):
                        graph1+='<td color="blue" bgcolor="#eeeeee"> * </td>'
                    elif y==int(y2) and x>=int(x1) and x<=int(x2):
                        graph1+='<td color="blue" bgcolor="#eeeeee"> * </td>'
                    elif x==int(x2) and y>=int(y1) and y<=int(y2):
                        graph1+='<td color="blue" bgcolor="#eeeeee"> * </td>'
                    else:    
                        graph1+='<td color="blue"> * </td>'
                else:
                    graph1+='<td color="blue">   </td>'
            if y==columna:
                graph1+='</tr>\n\t\t\t'
    graph2='</table>\n\t\t>];\n}' 
    imagen=graph+graph1+graph2
    #f= open(name+".dot","w+")
    #f.write(imagen)
    #f.close()   
    #os.system("fdp -Tpng -o "+name+".png "+name+".dot")
    Grafico(imagen,name)   
def crearDot5(lista,fila,columna,sizeMatriz,name,x1,y1,x2,y2):
    graph='digraph {\n\ttbl [\n\tsize="4,4"\n\tshape=plaintext\n\tlabel=<\n\n\t\t'
    graph+='<table border="0" color="green" cellpadding="10" cellborder="1" cellspacing="0">\n\t'
    graph1=''
    n=1
    for x in range(fila+1):
        graph1+='<tr>'
        bandera=False
        for y in range(columna+1):
            if x==0 and y==0:
                graph1+='<td bgcolor = "red" color="black"> A </td>'
            elif x==0 and y>0:
                graph1+='<td color="green">'+str(y)+'</td>'
            elif x>0 and y==0:
                graph1+='<td color="green"> '+str(x)+' </td>'
            else:
                if lista.buscar(x,y)==True:
                    if x==int(x1) and y==int(y1): 
                        graph1+='<td color="blue" bgcolor="#eeeeee"> * </td>'
                    elif y==int(y1)  and x>int(x1) and x<int(x2):
                        graph1+='<td color="blue" bgcolor="#eeeeee"> * </td>'
                    elif y==(int(y1)+n) and y<int(y2) and x>int(x1) and x<int(x2) and bandera == False:
                        graph1+='<td color="blue" bgcolor="#eeeeee"> * </td>'
                        bandera=True
                        n+=1
                    elif x==int(x2) and y>=int(y1) and y<=int(y2):
                        graph1+='<td color="blue" bgcolor="#eeeeee"> * </td>'
                    else:                   
                        graph1+='<td color="blue"> * </td>'
                else:
                    graph1+='<td color="blue">   </td>'
            if y==columna:
                graph1+='</tr>\n\t\t\t'
    graph2='</table>\n\t\t>];\n}' 
    imagen=graph+graph1+graph2
    #f= open(name+".dot","w+")
    #f.write(imagen)
    #f.close()   
    #os.system("fdp -Tpng -o "+name+".png "+name+".dot")
    Grafico(imagen,name)      
def crearDot6(lista,lista1,fila,columna,x1,y1,sizeMatriz,name):
    graph='digraph {\n\tsize="8,8"\n\tlabel="'+str(sizeMatriz)+'"\n\ttbl [\n\tshape=plaintext\n\tlabel=<\n\n\t\t'
    graph+='<table border="0" color="green" cellpadding="10" cellborder="1" cellspacing="0">\n\t'
    graph1=''
    for x in range(int(fila)+1):
        graph1+='<tr>'
        for y in range(int(columna)+1):
            if x==0 and y==0:
                graph1+='<td bgcolor = "red" color="black"> A </td>'
            elif x==0 and y>0:
                graph1+='<td color="green">'+str(y)+'</td>'
            elif x>0 and y==0:
                graph1+='<td color="green"> '+str(x)+' </td>'
            else:
                if lista.buscar(x,y)==True:
                    graph1+='<td color="blue"> * </td>'
                else:
                    graph1+='<td color="blue">   </td>'
            if y==int(columna):
                graph1+='</tr>\n\t\t\t'
    graph2='</table>\n\t\t>];' 
    imagen=graph+graph1+graph2
    graph='\n\ttbl1 [\n\tshape=plaintext\n\tlabel=<\n\n\t\t'
    graph+='<table border="0" color="green" cellpadding="10" cellborder="1" cellspacing="0">\n\t'
    graph1=''
    for i in range(int(x1)+1):
        graph1+='<tr>'
        for j in range(int(y1)+1):
            if i==0 and j==0:
                graph1+='<td bgcolor = "red" color="black"> A </td>'
            elif i==0 and j>0:
                graph1+='<td color="green">'+str(j)+'</td>'
            elif i>0 and j==0:
                graph1+='<td color="green"> '+str(i)+' </td>'
            else:
                if lista1.buscar(i,j)==True:
                    graph1+='<td color="blue"> * </td>'
                else:
                    graph1+='<td color="blue">   </td>'
            if j==int(y1):
                graph1+='</tr>\n\t\t\t'   
    graph2='</table>\n\t\t>];\n}'    
    imagen+=graph+graph1+graph2          
    #f= open(name+".dot","w+")
    #f.write(imagen)
    #f.close()   
    #os.system("fdp -Tpng -o "+name+".png "+name+".dot")
    Grafico(imagen,name)       
def Grafico(graphi,name):
    
    if  path.exists('\\grafo\\'+name+'.dot') and path.exists('\\grafo\\'+name+'.dot.png'): 
        os.remove('\\grafo\\'+name+'.dot.png')
        os.remove('\\grafo\\'+name+'.dot')   
      #d = Digraph(format='png')
        d=Source(graphi)
        #d.source(grafo)
        #d.format='png'
        d.render(name+'.dot',format='png',view=False) 
        #d.render(''+name+'.gv',ruta,format='svg',view=False)
        #render('dot', 'png',name+'.gv') 
    else:
      #d = Digraph(format='png')
      d=Source(graphi)
      #d.source(grafo)
      #d.format='png'
      #d.format='pdf'
      d.render(name+'.dot',format='png',view=False)
      #d.render(''+name+'.gv',ruta,format='svg',view=False)
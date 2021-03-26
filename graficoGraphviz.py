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
            if y==sizeMatriz-2:
                graph1+='</tr>\n\t\t\t'
    graph2='</table>\n\t\t>];\n}' 
    imagen=graph+graph1+graph2
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
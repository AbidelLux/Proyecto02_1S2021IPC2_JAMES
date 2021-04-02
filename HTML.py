
import webbrowser
def pageweb():
    from inicio import report
    #from lista import evalue
    #from lista import tipo
    #aux=""
    mensaje=""
    f = open('Reporte.html','w')
    mensaje ="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        body
        {
            background-color: #fff6f1;
            font-family: "helvetica",Arial;
        }
        #contenido
        {
            width:960px;
            margin: 0 auto;
            text-align:center;
        }
        h1
        {
            color:#e44e2d;
        }
        #textPr
        {
            width:800px;
            height:400px;
            background-color:#1d1d1d;
            color:#fff;
            margin: 0 auto;
            text-align:left;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.5)
        }
    </style>
    </head>
    <body>
    <div id="contenido">
        <header>
            <hgroup>
                <h1>Reporte Del Proyecto</h1>
            </hgroup>
        </header>
        <section>
            <div id="textPr">
                <article><br>
        """

    
       
    mensaje2="\n<p>"
    for n in report.iterar():
            mensaje2+=n+'<br>'
      
    mensaje3="""
    </p>
    </article>
            </div>        
            </section>
             </div>
            </body>
        </html>
    """       
     
    unir=mensaje+mensaje2+mensaje3
    f.write(unir)
    f.close()   


    #Cambia la ruta para indicar la localización del archivo
    #nombreArchivo = 'file:///Users/username/Desktop/programming-historian/' + 'holamundo.html'
    #webbrowser.open_new_tab(nombreArchivo)
    #d=webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
    #d.open_new_tab('file:/Reporte.html')
    webbrowser.open_new_tab('Reporte.html')
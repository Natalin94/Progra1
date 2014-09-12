__author__ = 'Natalin'

#Nombre: Natalin Viquez Lopez
#Fecha: 30/08/2014
#Horas trabajadas:

"""
def grabartxt():
    archi=open('datos.txt','a')
    archi.write('Linea 1\n')
    archi.write('Linea 2\n')
    archi.write('Linea 3\n')
    archi.close()
"""

listaPalabrasPythonCondicionales=["if","else"]
listaNuevoLenguajeCondicionales= ["si","sino"]
listaPalabrasPythonBucles=["while","for"]
listaNuevoLenguajeBucles = ["mientras","para"]
listaPalabrasPythonTipVariable= ["int", "str", "float"]
listaNuevoLenguajeTipVariable=["enteros", "letras", "decimal"]
listaPalabrasPythonSintaxis=[":", " ","print", "return", "break", "(" , ")"]
listaNuevoLenguajeSintaxis= [";", "_", "imprimir", "retornar", "abandonar", "$","#"]
listaPalabrasPythonFunciones= ["def"]
listaNuevoLenguajeFunciones= ["funcion"]


def menu():
    print("Bienvenido, seleccione la opcion que desea hacer:")
    seleccion=int(input("1)Nuevo Archivo \n2)Compilador"))
    lista=[]
    listaAux=[]
    if seleccion== 1:
        nuevo = input("Digite el nuevo codigo:\n")
        lista.extend(nuevo.split(" "))
        print(lista)
        for elemento in lista:
            if elemento in listaNuevoLenguajeCondicionales:
                listaAux.append(listaPalabrasPythonCondicionales[listaNuevoLenguajeCondicionales.index(elemento)])
            elif elemento in listaNuevoLenguajeBucles:
                listaAux.append(listaPalabrasPythonBucles[listaNuevoLenguajeBucles.index(elemento)])
            elif elemento in listaNuevoLenguajeSintaxis:
                listaAux.append(listaPalabrasPythonSintaxis[listaNuevoLenguajeSintaxis.index(elemento)])
            elif elemento in listaNuevoLenguajeFunciones:
                listaAux.append(listaPalabrasPythonFunciones[listaNuevoLenguajeFunciones.index(elemento)])
            else:
                listaAux.append(elemento)
                for i in listaAux:
                    print(i)


        print(listaAux)


"""
        for element in nuevo:
            if nuevo[:nuevo.find(" ")] in listaBucles:
                posicion=int(listaBucles.index(nuevo[:nuevo.find(" ")]))
                codigoFinal= nuevo.replace(nuevo[:nuevo.find(" ")], listaBucles[posicion +1])
                #codigoFinal2= codigoFinal.replace(codigoFinal[codigoFinal.find(" "):],"")
                print(codigoFinal)


            if nuevo[:nuevo.find(" ")] in listaCondicionales:
                posicion=int(listaCondicionales.index(nuevo[:nuevo.find(" ")]))
                codigoFinal= nuevo.replace(nuevo[:nuevo.find(" ")], listaCondicionales[posicion +1])
                codigoFinal2= codigoFinal.replace(codigoFinal[codigoFinal.find(" "):], "ksks")
                print(codigoFinal)


            #archi=open('datos.txt','w')
            #archi.close()

        for ele in nuevo:
            #if ele in listaCondicionales:
                    archi=open('datos.txt','a')
                    archi.write('nfn\n')
                    archi.write('kkkk\n')
                    archi.write('jkk\n')
                    archi.close()
                    """
menu()

# -*- coding: utf-8 -*-
dict = {}
estadoI=[]
estadoF=[]
import array
from typing import DefaultDict
def extendedTransitionFunction(state,cad):
    conjuntoEstadosFinal=[]
    # Si la cadena es vacía, regresaremos el estado
    if len(cad)==0:
        return state
    # Si la cadena tiene un valor, se ejecutará la función de transición simple
    elif len(cad)==1:
        print("𝛿*(",state,",",cad,")=",simpleTransitionFunction(state,cad))
        return simpleTransitionFunction(state,cad)
    else:
        #Extraer el ultimo elemento de la cadena y guardar el resto
        x=len(cad)-1
        resto = cad[:x]
        ultimo = cad[-1]
        #Utilizamos recursividad para llegar a tener un solo carácter
        aux=extendedTransitionFunction(state,resto)
        #Para cada estado en aux(conjunto de estados), ejecutaremos la 'SimpleTransitionFunction'  
        for r in aux:
           aux2 = simpleTransitionFunction(r,ultimo)
           #Unimos los estados que nos regrese la 'SimpleTransitionFunction' por cada iteración
           conjuntoEstadosFinal = union(conjuntoEstadosFinal,aux2)
        print("𝛿*(",state,",",resto+ultimo,")=",conjuntoEstadosFinal)
        return conjuntoEstadosFinal

def union(set1,set2):
    finalSet=[]  
    #Comprobamos el tipo de dato recibido (string o list)
    if(isinstance(set1,str)== True):
        #Si el string viene vacio lo volvemos una list vacia
        if(len(set1)==0):
            set1=[]
        elif(len(set1)==1):
        #Si el length es igual a uno lo dejamos como esta  
            set1 = set1
        else:
        #Si el length es mayor lo separamos por comas
            set1=set1.split(',')
        if(len(set2)==0):
            set2 = []
        elif(len(set2)==1):
            set2 = set2
        else:
            set2=set2.split(',')
        #Finalmente sumamos ambas listas y eliminamos los repetidos
        finalSet=set1+set2 
        # Eliminamos los valores repetidos
        finalSet=list(set(finalSet))
    else:
        # Si el tipo de dato es de tipo 'list', concatenamos directamente las listas
        finalSet=set1+set2
        # Eliminamos los valores repetidos
        finalSet=list(set(finalSet))
    return finalSet

def simpleTransitionFunction(state,car):
    #Aplicamos la simple transition function regresando un conjunto de estados llamando a dict (transitionTable) con el estado y el caracter recibido
    # En caso de que el estado no exista o el carácter no pertenezca al estado o no exista, regresamos una lista vacía 
    global dict
    try:
        return dict[state][car]
    except KeyError:
        return []
 
def crear_transitionTable(info_ndfa):
    global estadoI
    global estadoF
    #Creamos un conjunto de estados
    setOfStates = info_ndfa[0].split('\n') 
    setOfStates = setOfStates[0].split(',')
    #Guardamos el numero total de estados
    numberOfStates = len(setOfStates)
    #Creamos dos variables globales, una que contenga los estados finales y una los iniciales que usaremos en la funcion main
    estadoI=info_ndfa[2]
    estadoF=info_ndfa[3]
    #Creamos el diccionario
    transitionTable = {}
    state=0
    x = 4
    ###
    # A lo largo de estos dos whiles vamos a recorrer el txt a partir de la linea 4
    # Creando la transition table
    # Para crearla vamos a usar diccionarios anidados
    # El while de adentro se usa para obtener los caracteres con sus estados correspodientes
    # El while de afuera usa como key el estado en el que se esta iterando y como contenido el diccionario temporal creado en el while de adentro
    # ###
    while numberOfStates >= 1:
        diccionarioTemporal = {}
        length = len(info_ndfa)  #=longitud total del arreglo
        y=4
        while length > x:
            stateName = info_ndfa[y].split(',')
            #Aqui la y significa 4 porque es la linea a partir de la cual se indica la evaluacion de la transition funtion
            #EX. q0,a=>q0,q1,q3
            if(setOfStates[state]==stateName[0]):
                #Comparamos el conjunto de estados recibido en la primera linea del archivo con el primer estado que aparece en 
                #la evaluacion de la transition funtion ejemplo: setOfStates[state]=q0, stateName[0]=q0
                str=info_ndfa[y].split('\n')
                #En la linea de abajo separamos el string en dos ejemplo:  q0,a= y q0,q1,q3 
                str=str[0].split('>')
                #Una vez separado obtenemos una lista con dos elementos y tomamos solo los estados del final ejemplo q0,q1,q3 
                str=str[1].split(',')
                diccionarioTemporal[info_ndfa[y][3]]=str 
                #En la variable diccionario temporal guardamos el caracter ejemplo info_ndfa[y][3] = a como key
                #Y el conjunto de estados que se encuentra en la variable str ejemplo ['q0', 'q1', 'q3']
            y=y+1 #Pasammos a la siguiente linea
            length = length -1 #Cambiamos al siguiente estado
        length=len(info_ndfa)
        y=4    
        transitionTable[setOfStates[state]] = diccionarioTemporal 
        #Añadimos un elemento al diccionario usando como key el estado en el cual estamos iterando
        #El diccionario temporal que creamos y llenamos en el while anterior lo pasamos como contenido
        #Vaciamos el diccionario temporal y actualizamos variables
        diccionarioTemporal = {}
        state=state+1
        numberOfStates=numberOfStates-1
    return transitionTable
         
def leer_info(nombreArchivo):
    fda = []
    f = open(nombreArchivo, 'r')
    for line in f:
        fda.append(line)
    f.close()
    return fda

# Creamos el menú de opciones
def main():
    print("Autores: ")
    print("Bruno Jimenez          A01748931")
    print("Roberto Castro         A01748559")
    #Importamos la transition table (dict), y el estado inicial y los estado(s) finales
    global dict
    global estadoI
    global estadoF
    nfda = []
    print('Introduce el nombre del archivo')
    nombreArchivo = input()
    nfda = leer_info(nombreArchivo)
    dict=crear_transitionTable(nfda)
    ans = False
    while not ans:
        print("""
        1 Show transition table
        2 Simple transition function
        3 Union
        4 Extended transition function
        5 Exit""")
        opcion=input("What would you like to do? ")
        if opcion=='1':
            print("Transition table: ")
            print(dict)
        if opcion=='2':
            str=input("Insert an state and a character in format q0,a: ")
            str=str.split(',')
            stf=simpleTransitionFunction(str[0],str[1])
            print("The set of states for ",str," are: ")
            print(stf)
        if opcion=='3':
            str=input("Insert first set of states (q0,q1,...,): ")
            str2=input("Insert second set of states (q0,q1,...,): ")
            finalSet=union(str,str2)
            print(finalSet)
        if opcion=='4':
            string=False
            state=input("Insert an state: ")
            cad=input("Insert a string: ")
            out=extendedTransitionFunction(state,cad)
            #Para saber si el string es valido primero debemos saber si el estado del cual partimos es el inicial
            if(state in estadoI):
                for r in out:
                    #Comprobamos si en la lista de estados que recibimos se encuentra el final para saber si el string es aceptado o no
                    if (r in estadoF):
                        string=True
                        break   
                if(string==True):
                    print("String accepted!")
                else:
                    print("String unaccepted")
        if opcion=='5':
            print("Goodbye!!!")
            ans = True


main()

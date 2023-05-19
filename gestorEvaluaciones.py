from puntaje import Puntaje
from federado import Federado
import csv

class gestorEvaluacion:

    def cargarPuntajes(puntajes):
        
        with open("evaluacion.csv") as archivo:
                reader = csv.reader(archivo, delimiter=';')
                for fila in reader:
                        unPuntaje= Puntaje(str(fila[0]), fila[1], float(fila[2]),float(fila[3]),float(fila[4]))
                        puntajes.append(unPuntaje)
        return puntajes
        
    puntajeMayor= Puntaje(' ', ' ', 0, 0, 0)   

    def promedio(puntajes):
        for i in range(len(puntajes)):
            sum= puntajes[i].get_valor1 + puntajes[i].get_valor2 + puntajes[i].get_valor3
            prom= sum/3
                
        return prom

    def get_federadoByDNI(federados, dni):
        i=0
        while federados[i].get_dni() != dni:
            i+=1
        return federados[i]

    
    def mayorPuntaje__gt__(puntajes, federados):
        
        for i in range(len(puntajes)-1):
            if puntajes[i].promedio() > puntajes[i+1].promedio():
                puntajeMayor= puntajes[i]
            else:
                puntajeMayor = puntajes[i+1]
            #federadoMayoPuntaje = federados puntajeMayor.get_dni()
        i=0
        while puntajeMayor.get_dni() != federados[i].get_dni():
            i+=1

        federadoMayoPuntaje = federados[i]
        print(f'El patinador con mayor puntuacion fue: {federadoMayoPuntaje.get_nom()} {federadoMayoPuntaje.get_apell()} en el estilo {puntajeMayor.get_estilo()} del club {federadoMayoPuntaje.get_club()}')
                                                    

    def listarEstilos(puntajes, federados):
       #buscar el nombre de quienes estan en estilo L y en estilo E
        nombreAcomparar= ' '
        bandera= False
        for i in range(len(puntajes)):
            if puntajes[i].get_estilo() == 'L':
                nombreAcomparar= federados[i].get_nom()
            for j in range(len(puntajes)):
                if (puntajes[j].get_estilo() == 'E'):
                  if nombreAcomparar== federados[j].get_nom():
                    print(f'{nombreAcomparar} patina en estilo Libre y en Escuela.')
                    bandera= True                   
        if bandera == False:
            print(f'Nadie patina en ambos estilos.')


    def valoracionesDeJueces(puntajes):
        #Dado el DNI de un inscripto y un estilo, mostrar las 3 valoraciones dadas por los jueces.
        DNIinscripto=input(str('Ingrese el DNI del inscripto: '))
        estiloIngresado=input(str('Ingrese el estilo del inscripto: '))

        for i in range(len(puntajes)):
            if (puntajes[i].get_dni() == DNIinscripto) and (puntajes[i].get_estilo() == estiloIngresado) :
                print(f'Los puntajes dados por los jueces son: {puntajes[i].get_valor1()} - {puntajes[i].get_valor2()} - {puntajes[i].get_valor3()}.')
                      
                      

            

           
                    
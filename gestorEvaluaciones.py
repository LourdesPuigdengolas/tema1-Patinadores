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
       
        for i in range(len(puntajes)):
            if puntajes[i].get_estilo() == 'L':
                nombreAcomparar= federados[i].get_nom()
        for i in range(len(puntajes)):
            if (puntajes[i].get_estilo() == 'E'):
                nombreAcomparar2= federados[i].get_nom()
        if nombreAcomparar == nombreAcomparar2:
            print(f'{federados[i].get_nom()} patina en estilo Libre y en Escuela.')


            ''' elif puntajes[i].get_estilo() =='E':
                print(f'{federados[i].get_nom()} patina en estilo Escuela.')'''


    
                      
                      

            

           
                    
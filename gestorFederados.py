from federado import Federado
from puntaje import Puntaje
import csv

class ManejadorFederados:
     
    def cargarFederados(federados):
 
        with open("federados.csv") as archivo:
            reader = csv.reader(archivo, delimiter=';')
            for fila in reader:
                    unFederado= Federado(fila[0], fila[1], fila[2], fila[3], fila[4])
                    federados.append(unFederado)
        return federados
  
    '''def get_puntajeByDNI(puntajes, dni):     esto se haría si solo hubiera un puntaje por patinador
        i=0
        while puntajes[i].get_dni() != dni:
            i+=1
        return puntajes[i]'''

    def listarPorEstilosYEdad(federados, puntajes):
        estilo= str(input('Ingrese el estilo: '))
        ed= str(input('Ingrese la edad: '))
        existePatinadorConEstiloYedad= False   
        for i in range(len(federados)):
            if (federados[i].get_edad() == ed):
                for j in range(len(puntajes)):
                    if puntajes[j].get_dni() == federados[i].get_dni():
                        if puntajes[j].get_estilo() == estilo:
                            print(f'El/la patinador/a {federados[i].get_apell()} {federados[i].get_nom()} DNI: {federados[i].get_dni()}')
                            existePatinadorConEstiloYedad= True
                    
        if existePatinadorConEstiloYedad == False:
                print(f'No existe ningún patinador con esa edad en ese estilo.')
   

   
            

  
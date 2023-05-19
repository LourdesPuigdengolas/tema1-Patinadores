import csv
from gestorFederados import ManejadorFederados
from gestorEvaluaciones import gestorEvaluacion

if __name__=='__main__':
    
    federados=[]
    # Carga federados a la lista
    federados= ManejadorFederados.cargarFederados(federados)

    puntajes=[]
    # Carga puntajes a la lista
    puntajes=gestorEvaluacion.cargarPuntajes(puntajes)
       
    print(f'-------MENU-------:')
    opcion=int(input(' -1: Listar \n -2: Mayor puntaje\n -3: Estilos\n -4: Puntajes \n -0: Salir \n  - Ingrese la opcion que desea:- '))
    while opcion !=0:
        if opcion ==1:
            ManejadorFederados.listarPorEstilosYEdad(federados, puntajes)

        elif opcion==2:
            #prom=gestorEvaluacion.promedio(puntajes)
            gestorEvaluacion.mayorPuntaje__gt__(puntajes, federados)

        elif opcion==3:
            gestorEvaluacion.listarEstilos(puntajes, federados)

        elif opcion ==4:
            gestorEvaluacion.valoracionesDeJueces(puntajes)
        else:
            print(f'Opcion incorrecta!')
        print(f'-------MENU-------:')
        opcion=int(input(' -1: Listar \n -2: Mayor puntaje \n -3: Estilos\n -4: Puntajes \n -0: Salir \n  -Ingrese la opcion que desea: - '))
           




        
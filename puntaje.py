class Puntaje:
    __dni=' '
    __estilo=''
    __valor1=float
    __valor2= float
    __valor3=float
    def __init__(self,dni,estilo,valor1,valor2,valor3):
        self.__dni=dni
        self.__estilo= estilo
        self.__valor1=valor1
        self.__valor2=valor2
        self.__valor3=valor3
    
    
    def get_dni(self):
        return self.__dni
    def get_estilo(self):
        return self.__estilo
    def get_valor1(self):
        return self.__valor1
    def get_valor2(self):
        return self.__valor2
    def get_valor3(self):
        return self.__valor3
        
    def promedio(self):
        promedio= (self.__valor1 + self.__valor2 + self.__valor3)/3
        return promedio

    

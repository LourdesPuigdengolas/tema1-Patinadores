class Federado:
    __apell=''
    __nom=''
    __dni=''
    __edad=''
    __club=''
    def __init__(self, apell,nom,dni,edad,club):
        self.__apell=apell
        self.__nom=nom
        self.__dni=dni
        self.__edad= edad
        self.__club=club

    def get_apell(self):
        return self.__apell
    
    def get_nom(self):
        return self.__nom
        
    def get_dni(self):
        return self.__dni
    
    def get_edad(self):
        return self.__edad
    
    def get_club(self):
        return self.__club
    

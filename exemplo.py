class Carro:
    def __init__(self, marca, modelo, placa):
        self.__marca=marca
        self.__modelo=modelo
        self.__placa=placa
        self.__velocidade=0
    def imprimir(self):
        print(f'Marca: {self.__marca}, Modelo: {self.__modelo}, Placa: {self.__placa}')
        
    def acelerar(self, incremento):
        self.__velocidade+=incremento
        
        print(f'O carro acelerou para { self.__velocidade} km/h')

    def frear(self, decremento):
        self.__velocidade-=decremento
        if self.__velocidade<0:
            self.__velocidade=0
        print(f'O carro freou para { self.__velocidade} km/h')
    def set_marca(self,marca):
        
        self.__marca=marca
        
    def get_marca(self):
        return self.__marca
    
c=Carro("Vw", "Gol", "ABC10J10")
c.imprimir()
c.acelerar(10)
c.frear(2)
c.set_marca("Fiat")
print("A nova marca do carro é :" + c.get_marca())

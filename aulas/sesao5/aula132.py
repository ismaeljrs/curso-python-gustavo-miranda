#_cor nao ultilize este atributo e protegido pela class ele e da class 1 ou 2 andelaines nao devem ser usados fora da class 

class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self): #   protegido , coltor a funcionar , ele pode mudar na hr que quiser ele estar protegido
        print('Protey')
        return self._cor
    @cor.setter # <- nome da property e tem o setter e o metodo dentro do self ele tem que reseber um valor 
    def cor(self, valor):
        self._cor = valor
        
    
caneta = Caneta('azul')
caneta.cor = 'Rosa'
print(caneta.cor)

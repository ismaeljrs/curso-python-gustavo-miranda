




class Caneta:
    def __init__(self, cor):
        self.cor = cor

    def get_cor(self): #   protegido , coltor a funcionar , ele pode mudar na hr que quiser ele estar protegido
        print('get cor')
        return self.cor
    
caneta = Caneta('azul')
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('propety')
        return self.cor_tinta

def mostrar(caneta):
    return caneta.cor

caneta = Caneta('Azul')
# caneta.cor = 'rosa'

print(caneta.cor)
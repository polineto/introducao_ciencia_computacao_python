def main():
    carro1 = Carro('brasilia', 1968, 'amarela', 80)
    carro2 = Carro('fuscao', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, velmax):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velmax = velmax
        self.vel = 0

 #   def imprima(self):
 #       if self.vel == 0:
 #           print( '%s %s %d' %(self.modelo, self.cor, self.ano) )
 #       elif self.vel < self.velmax:
 #           print( '%s %s indo a %d Km/h' %(self.modelo, self.cor, self.vel) )
 #       else:
 #           print( '%s %s indo muito raaaapiiiidoooo!' %(self.modelo, self.cor) )
    # ao inves de print, poderiamos usar o método especial __str__
    def __str__(self):
        if self.vel == 0:
            s = '%s %s %d' %(self.modelo, self.cor, self.ano)
        elif self.vel < self.velmax:
            s = '%s %s indo a %d Km/h' %(self.modelo, self.cor, self.vel)
        else:
            s = '%s %s indo muuuuuiiiiito rapido!' %(self.modelo, self.cor)
        return s

    def acelere(self, velocidade):
        self.vel = velocidade
        if self.vel > self.velmax:
            self.vel = self.velmax
        #self.imprima()
        print(self) # o método especial __str__ permite isso

    def pare(self):
        self.vel = 0
        #self.imprima()
        print(self) # o método especial __str__ permite isso

main()

class Triangulo:
    def __init__(self, a, b, c): 
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self): 
        lados = [self.a, self.b, self.c]
        if self.a == self.b and self.b == self.c:
            tipo = 'equilátero'
        elif self.a not in [self.b, self.c] and self.b not in [self.a, self.c]:
            tipo = 'escaleno'
        else:
            tipo = 'isósceles'
        return tipo

#    def tipo_lado(self):
#        print(self)
    

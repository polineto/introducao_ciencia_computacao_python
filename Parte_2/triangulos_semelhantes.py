class Triangulo:
    def __init__(self, a, b, c): 
        self.a = a 
        self.b = b 
        self.c = c
        self.lados = [self.a, self.b, self.c]

    def semelhantes(self, t):
        list1 = sorted(self.lados)
        list2 = sorted(t.lados)
        return (list1[0] / list2[0]) == (list1[1] / list2[1]) == (list1[2] / list2[2])
        

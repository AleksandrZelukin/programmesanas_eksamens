class Kubs:
    def __init__(self,malas,skaitlis,krasa):
        self.malas = malas
        self.skaitlis = skaitlis
        self.krasa = krasa
    def tilpums(self):
        return self.malas**3

a = Kubs(23,2,"red")

print(a.krasa,a.tilpums())
        

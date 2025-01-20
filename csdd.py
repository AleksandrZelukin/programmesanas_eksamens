class Automobilis:
    def __init__(self,zimols,reg_datums,masa,degviels):
        self.zimols = zimols
        self.reg_datums = reg_datums
        self.masa = masa
        self.degviels = degviels
    def auto_ipasibas(self):
        print("Zimols:", self.zimols)
        print("Reģistrācijas datums:", self.reg_datums)
        print("Pilna masa:", self.masa)
        print("Degviela tips:", self.degviels)

auto1 = Automobilis("BMW","12.01.1998",1380,"D")
auto2 = Automobilis("Mazda","09.09.2003",1200,"B")
auto3 = Automobilis("Honda","10.12.2013",1280,"D")

print(auto1.auto_ipasibas())
print(auto2.auto_ipasibas())
print(auto3.auto_ipasibas())
        

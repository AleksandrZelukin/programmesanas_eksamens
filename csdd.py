# 1.1. Uzrakstīt programmas koda bloku, kas definē piemērotu klasi informācijai par
# transportlīdzekļiem CSDD datubāzē atbilstoši zemāk norādītajai informācijai, kā arī definēt šai
# klasei metodi, ar kuru izvada šādai klasei atbilstoša objekta īpašību vērtības. (4 punkti)
# 1.2. Izveidot vienu klases objektu ar zemāk minētiem testa datiem. (1 punkts)
# 1.3. Izmantot objekta metodi, lai izvadītu ekrānā visas definētās objekta īpašības. (1 punkts)
# Apstrādājamā informācija par transportlīdzekli – zīmols, modelis, reģistrācijas datums CSDD
# datubāzē formātā dd.mm.gggg, pilna masa kilogramos (bez mērvienības), degvielas veida
# apzīmējums (iespējamie apzīmējumi: B – benzīns, BG – benzīns/gāze, D – dīzeļdegviela,
# E – elektriskais, BE – benzīna hibrīds, DE – dīzeļa hibrīds).
# 
# Testa dati:
# zīmols: Audi
# modelis: A4
# reģistrācijas datums: 22.10.2019
# pilna masa: 1800
# degvielas veids: BG


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
        

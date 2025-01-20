# Uzrakstīt programmas koda bloku, 
# kas definē piemērotu klasi informācijai 
# par transportlīdzekļiem CSDD datubāzē 
# atbilstoši zemāk norādītajai informācijai, 
# kā arī definēt šai klasei metodi, 
# ar kuru izvada šādai klasei atbilstoša objekta īpašību vērtības. (4 punkti) 
# 1.2. Izveidot vienu klases objektu ar zemāk minētiem testa datiem. (1 punkts) 
# 1.3. Izmantot objekta metodi, lai izvadītu ekrānā visas definētās 
# objekta īpašības. (1 punkts) 
# Apstrādājamā informācija par transportlīdzekli – 
# zīmols, modelis, reģistrācijas datums CSDD datubāzē formātā dd.mm.gggg, 
# pilna masa kilogramos (bez mērvienības), degvielas veida apzīmējums 
# Iespējamie apzīmējumi: 
# B – benzīns, 
# BG – benzīns/gāze, 
# D – dīzeļdegviela, 
# E – elektriskais, 
# BE – benzīna hibrīds, 
# DE – dīzeļa hibrīds.

from datetime import datetime

class Transportlidzeklis:
    def __init__(self, zimols, modelis, registracijas_datums, pilna_masa, degvielas_veids):
        self.zimols = zimols
        self.modelis = modelis
        self.registracijas_datums = datetime.strptime(registracijas_datums, "%d.%m.%Y").date()
        self.pilna_masa = pilna_masa
        self.degvielas_veids = degvielas_veids

    def izvadit_ipasibas(self):
        print(f"Zīmols: {self.zimols}")
        print(f"Modelis: {self.modelis}")
        print(f"Reģistrācijas datums: {self.registracijas_datums.strftime('%d.%m.%Y')}")
        print(f"Pilna masa: {self.pilna_masa} kg")
        print(f"Degvielas veids: {self.degvielas_veids}")

# Testa dati:

# Zīmols: "Toyota"
# Modelis: "Corolla"
# Reģistrācijas datums: "15.06.2020"
# Pilna masa: 1500
# Degvielas veids: "B"

transportlidzeklis = Transportlidzeklis(
    zimols="Toyota",
    modelis="Corolla",
    registracijas_datums="15.06.2020",
    pilna_masa=1500,
    degvielas_veids="B"
)

# Metodes izmantošana īpašību izvadīšanai
transportlidzeklis.izvadit_ipasibas()

# Rezultāts
# Izpildot šo kodu, tiks izvadīts:
#     Zīmols: Toyota
#     Modelis: Corolla
#     Reģistrācijas datums: 15.06.2020
#     Pilna masa: 1500 kg
#     Degvielas veids: B

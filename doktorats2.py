class Doktorats:
    def __init__(self, nosaukums, pacientu_skaits):
        self.nosaukums  = nosaukums
        self.pacientu_skaits = pacientu_skaits
    
    def ievadi_datus(self):
        self.nosaukums = input("Ievadiet doktorāta nosaukumu: ")
        self.pacientu_skaits = int(input("Ievadiet pacientu skaitu: "))
    def get_info(self):
        return f"Doktorats {self.nosaukums} apkālpo {self.pacientu_skaits} pacientus"
    
print("Ievadiet doktorāta datus:")
doktorats = Doktorats("", 0)
doktorats.ievadi_datus()
print(doktorats.get_info())

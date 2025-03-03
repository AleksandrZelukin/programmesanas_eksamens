class Doktorats:
    def __init__(self, nosaukums, pacienti):
        self.nosaukums = nosaukums
        self.pacienti = pacienti
    def ievadi_datus():
        nosaukums = input("Ievadiet doktorāta nosaukumu: ")
        pacienti = input("Ievadiet pacientu skaitu: ")
        return Doktorats(nosaukums, pacienti)
    def izdrukat_datus(self):
        print(f"Doktorāts {self.nosaukums} apkalpo {self.pacienti} pacientus.")

doktorats = Doktorats.ievadi_datus()
doktorats.izdrukat_datus()



    
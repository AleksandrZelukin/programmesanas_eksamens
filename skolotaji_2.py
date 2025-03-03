class Skolotajs:
    def __init__(self, stundu_skaits_nedela, skolotaja_tips):
        self.stundu_skaits_nedela = stundu_skaits_nedela
        self.skolotaja_tips = skolotaja_tips

class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, stundu_skaits_nedela, klase):
        super().__init__(stundu_skaits_nedela, 1)
        self.uzvards = uzvards
        self.klase = klase

    def izdruka(self):
        print(f"""Sākumskolas skolotājs: {self.uzvards}, 
              Klase: {self.klase},
              Stundu skaits nedēļā: {self.stundu_skaits_nedela}""")

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, pirmais_prieksmets, otrais_prieksmets, stundu_skaits_pirmais, stundu_skaits_otrais):
        super().__init__(stundu_skaits_pirmais + stundu_skaits_otrais, 3)
        self.uzvards = uzvards
        self.pirmais_prieksmets = pirmais_prieksmets
        self.otrais_prieksmets = otrais_prieksmets
        self.stundu_skaits_pirmais = stundu_skaits_pirmais
        self.stundu_skaits_otrais = stundu_skaits_otrais

    def kop_stundas(self):
        return self.stundu_skaits_pirmais + self.stundu_skaits_otrais

    def izdruka(self):
        print(f"""Vidusskolas skolotājs: {self.uzvards}, 
              Pirmais priekšmets: {self.pirmais_prieksmets}, 
              Otrais priekšmets: {self.otrais_prieksmets}, 
              Kopējais stundu skaits nedēļā: {self.kop_stundas()}""")

def ievadi_datus():
    skolotaji = []
    while True:
        tips = input("""Ievadiet skolotāja tipu 
                     1 - sākumskolas, 
                     3 - vidusskolas, 
                     0 - beigt: """)
        if tips == '0':
            break
        elif tips == '1':
            uzvards = input("Ievadiet skolotāja uzvārdu: ")
            stundu_skaits_nedela = int(input("Ievadiet stundu skaitu nedēļā: "))
            klase = input("Ievadiet klasi: ")
            skolotaji.append(SakumskolasSkolotajs(uzvards, stundu_skaits_nedela, klase))
        elif tips == '3':
            uzvards = input("Ievadiet skolotāja uzvārdu: ")
            pirmais_prieksmets = input("Ievadiet pirmā priekšmeta nosaukumu: ")
            otrais_prieksmets = input("Ievadiet otrā priekšmeta nosaukumu: ")
            stundu_skaits_pirmais = int(input("Ievadiet stundu skaitu pirmajā priekšmetā nedēļā: "))
            stundu_skaits_otrais = int(input("Ievadiet stundu skaitu otrajā priekšmetā nedēļā: "))
            skolotaji.append(VidusskolasSkolotajs(uzvards, pirmais_prieksmets, otrais_prieksmets, stundu_skaits_pirmais, stundu_skaits_otrais))
        else:
            print("Nepareizs tips, mēģiniet vēlreiz.")
    return skolotaji

def izdruka_skolotaji(skolotaji):
    for skolotajs in skolotaji:
        skolotajs.izdruka()

skolotaji = ievadi_datus()
izdruka_skolotaji(skolotaji)

# Izvades piemērs:

# Sākumskolas (tips – 1) skolotājs Bērziņš māca 15 stundas 2.a klasē.

# Vidusskolas (tips – 3) skolotājs Ozols māca šādus priekšmetus: matemātika un datorika, kopā 20 stundas.


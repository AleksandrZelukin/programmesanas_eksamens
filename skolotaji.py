# Bāzes klase Skolotajs
class Skolotajs:
    def __init__(self, uzvards, stundu_skaits_nedela):
        self.uzvards = uzvards
        self.stundu_skaits_nedela = stundu_skaits_nedela
        self.skolotaja_tips = 0  # Tiks definēts atvasinātajās klasēs

    def print_info(self):
        raise NotImplementedError("Šī metode jādefinē atvasinātajās klasēs")


# Atvasinātā klase SakumskolasSkolotajs
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, stundu_skaits_nedela, klase):
        super().__init__(uzvards, stundu_skaits_nedela)
        self.skolotaja_tips = 1  # Sākumskolas skolotājs
        self.klase = klase

    def print_info(self):
        print(f"Skolotāja tips: Sākumskolas skolotājs")
        print(f"Uzvārds: {self.uzvards}")
        print(f"Stundu skaits nedēļā: {self.stundu_skaits_nedela}")
        print(f"Pasniedz visus priekšmetus {self.klase}. klasē")


# Atvasinātā klase VidusskolasSkolotajs
class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, pirmais_prieksmets, otrais_prieksmets, stundu_skaits_pirmais, stundu_skaits_otrais):
        super().__init__(uzvards, stundu_skaits_pirmais + stundu_skaits_otrais)
        self.skolotaja_tips = 3  # Vidusskolas skolotājs
        self.pirmais_prieksmets = pirmais_prieksmets
        self.otra_prieksmets = otrais_prieksmets
        self.stundu_skaits_pirmais = stundu_skaits_pirmais
        self.stundu_skaits_otrais = stundu_skaits_otrais

    def print_info(self):
        print(f"Skolotāja tips: Vidusskolas skolotājs")
        print(f"Uzvārds: {self.uzvards}")
        print(f"Pasniedz priekšmetus: {self.pirmais_prieksmets} un {self.otra_prieksmets}")
        print(f"Kopējais stundu skaits nedēļā: {self.stundu_skaits_nedela}")


# Galvenā programmas daļa
if __name__ == "__main__":
    # Ievade un apstrāde sākumskolas skolotājam
    uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
    stundu_skaits_nedela = int(input("Ievadiet stundu skaitu nedēļā: "))
    klase = input("Ievadiet klasi, kurā sākumskolas skolotājs pasniedz: ")
    sakumskolas_skolotajs = SakumskolasSkolotajs(uzvards, stundu_skaits_nedela, klase)

    # Ievade un apstrāde vidusskolas skolotājam
    uzvards = input("\nIevadiet vidusskolas skolotāja uzvārdu: ")
    pirmais_prieksmets = input("Ievadiet pirmo priekšmetu: ")
    otrais_prieksmets = input("Ievadiet otro priekšmetu: ")
    stundu_skaits_pirmais = int(input("Ievadiet stundu skaitu pirmajam priekšmetam nedēļā: "))
    stundu_skaits_otrais = int(input("Ievadiet stundu skaitu otrajam priekšmetam nedēļā: "))
    vidusskolas_skolotajs = VidusskolasSkolotajs(uzvards, pirmais_prieksmets, otrais_prieksmets, stundu_skaits_pirmais, stundu_skaits_otrais)

    # Izdruka sākumskolas skolotājam
    print("\n--- Sākumskolas skolotāja informācija ---")
    sakumskolas_skolotajs.print_info()

    # Izdruka vidusskolas skolotājam
    print("\n--- Vidusskolas skolotāja informācija ---")
    vidusskolas_skolotajs.print_info()
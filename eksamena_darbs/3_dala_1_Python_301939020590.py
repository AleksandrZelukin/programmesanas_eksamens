class Gramata:
    def __init__(self, nosaukums="Nav norādīts", lappusu_skaits=0, ISBN="Nav norādīts",
                 autors=None, zanrs=None, izd_gads=None, pieejamibas_statuss=None):
        self.nosaukums = nosaukums
        self.lappusu_skaits = lappusu_skaits
        self.ISBN = ISBN
        self.autors = autors
        self.zanrs = zanrs
        self.izd_gads = izd_gads
        self.pieejamibas_statuss = pieejamibas_statuss
        if nosaukums != "Nav norādīts" and lappusu_skaits != 0 and ISBN != "Nav norādīts":
            print(f'Grāmata "{self.nosaukums}" ir veiksmīgi izveidota.')

    def izvadit(self):
        print(f'Grāmatas autors: {self.autors}')
        print(f'Grāmatas nosaukums: "{self.nosaukums}"')
        print(f'Grāmatas izdošanas gads: {self.izd_gads}')

    def aprekinat(self, kaveto_dienu_skaits):
        maksa = self.lappusu_skaits * 0.01 * kaveto_dienu_skaits
        return round(maksa, 2)

class Fantazija(Gramata):
    def aprekinat(self, kaveto_dienu_skaits):
        pamata_maksa = super().aprekinat(kaveto_dienu_skaits)
        fantasijas_maksa = pamata_maksa + pamata_maksa * 0.01
        return round(fantasijas_maksa, 2)

class GramatuKatalogs:
    def __init__(self):
        self.gramatas = []

    def pievienot(self, gramata):
        self.gramatas.append(gramata)
        print(f'Grāmata "{gramata.nosaukums}" ir veiksmīgi pievienota.')

    def atjauninat_statusu(self, ISBN, jauns_statuss):
        for g in self.gramatas:
            if str(g.ISBN) == str(ISBN):
                g.pieejamibas_statuss = jauns_statuss
                print(f'Grāmatai ar ISBN "{ISBN}" statuss ir atjaunināts uz "{jauns_statuss}".')
                return
        print(f'Grāmata ar ISBN "{ISBN}" nav atrasta katalogā.')

    def nonemt(self, ISBN):
        for i, g in enumerate(self.gramatas):
            if str(g.ISBN) == str(ISBN):
                del self.gramatas[i]
                print(f'Grāmata ar ISBN "{ISBN}" ir veiksmīgi nodzēsta no kataloga.')
                return
        print(f'Grāmata ar ISBN "{ISBN}" nav atrasta katalogā.')

epifanijas = Gramata(
    nosaukums="Epifānijas",
    lappusu_skaits=304,
    ISBN=9789934036101,
    autors="Imants Ziedonis",
    zanrs="dzeja",
    izd_gads=2022,
    pieejamibas_statuss="pieejama"
)

epifanijas.izvadit()

maksa_epifanijas = epifanijas.aprekinat(5)
print(f'Grāmatas "{epifanijas.nosaukums}" kavējuma maksa ir {maksa_epifanijas:.2f} EUR.')

harijs = Fantazija(
    nosaukums="Harijs Poters un Filozofu akmens",
    lappusu_skaits=223,
    ISBN=9780747532699,
    autors="Dž. K. Roulinga",
    zanrs="fantāzija",
    izd_gads=1997,
    pieejamibas_statuss="pieejama"
)


maksa_harijs = harijs.aprekinat(10)
print(f'Grāmatas "{harijs.nosaukums}" kavējuma maksa ir {maksa_harijs:.2f} EUR.')

katalogs = GramatuKatalogs()

katalogs.pievienot(epifanijas)

katalogs.pievienot(harijs)

katalogs.atjauninat_statusu(9780747532699, "nav pieejama")

katalogs.nonemt(9789934036101)

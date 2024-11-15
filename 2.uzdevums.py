# Noliktavā paredzēts uzstādīt iepakošanas robotu, kura uzdevums ir iepakot taisnstūra
# formas kastēs iespējami daudz no vienādiem kubveida klucīšiem veidotu dažādu taisnstūra
# paralēlskaldņa formas bloku. Kastes bloku iepakošanai tiek izvēlētas tā, ka to visi malu garumi
# ir proporcionāli klucīša izmēram (kastes jebkuras malas garums, kas dalīts ar klucīša malas
# garumu, ir vesels skaitlis). Klucīši var būt dažādās krāsās, bet bloks drīkst būt veidots tikai
# no vienādas krāsas klucīšiem. Viens bloks var būt veidots no viena, diviem, trīs vai četriem
# klucīšiem.
# Programmētāju komandai dots uzdevums izveidot datorprogrammu minētā robota darbināšanai.
# Tev kā programmētāju komandas dalībniekam ir izvēlētā programmēšanas valodā jāsastāda
# kods, kas realizē tālāk minētos uzdevumus.
# VISC Vaļņu ielā 2, Rīgā, LV-1050
# 29481647123802948164712380294816471238029481647123802948164720
# Eksāmens programmēšanā (augstākais līmenis) Skolēna darba lapa 2023 7
# 29481647123802948164712380294816471238029481647123802948164720
# 2.1. Definēt:
# • klasi kubs (1 punkts), kurai ir īpašības (1 punkts):
# o malas garums centimetros, vesels skaitlis intervālā no 2 līdz 10 ieskaitot;
# o krāsas nosaukums (viens vārds) – teksts;
# • metodes:
# o aprekinat_tilpumu, kura aprēķina un atgriež veselu skaitli – kuba tilpumu
# kubikcentimetros (1 punkts);
# o metode, kura likvidē objektu un ekrānā izvada paziņojumu, ka objekts likvidēts,
# paziņojumā norādot likvidētā objekta krāsu (1 punkts);
# o metode, kura inicializē klases kubs īpašības (1 punkts).
# 2.2. Izveidot klases kubs konstruktoru, kas veic saņemto datu (argumentu) kontroli, izvadot
# atbilstošu paziņojumu (1 punkts) un uzstādot minimālo nosacījumiem atbilstošo vērtību
# (1 punkts), ja malas garums neatbilst nosacījumiem.
# 2.3. Izveidot jaunu klases kubs objektu kubg, kura krāsa ir zaļa un malas garums
# 10 centimetri (1 punkts).
# 2.4. Izveidot jaunu klases kubs objektu kubr, kura krāsa ir sarkana un malas garums
# 1 centimetrs (1 punkts).
# 2.5. Izvadīt ekrānā objekta kubg krāsu un tilpumu (1 punkts).
# 2.6. Izvadīt ekrānā objekta kubr malas garumu (1 punkts).
# 2.7. Dzēst objektu kubr (1 punkts).
# 2.8. Pārbaudīt, ka objekts kubr vairs nav pieejams, un izvadīt ekrānā atbilstošu paziņojumu
# (1 punkts).
# 2.9. Izvadīt ekrānā objekta kubg malas garumu (1 punkts).
# 2.10. Definēt klasi bloks (1 punkts), kura manto klasi kubs (1 punkts) un kurai ir:
# • īpašības:
# • privātas (1 punkts):
# o kubu skaits blokā, vesels skaitlis intervālā no 1 līdz 4 ieskaitot;
# • publiskas (1 punkts):
# o nosaukums, kurš veidots no kuba krāsas un kubu skaita apvienojuma, piemēram,
# orange4;
# o forma, vesels divciparu skaitlis ar iespējamām vērtībām 11, 12, 13, 14 un 22, kur
# pirmais cipars norāda vertikālā stāvoklī novietota bloka platumu (klucīšos), bet otrais –
# bloka augstumu (klucīšos);
# o derīgums – vesels skaitlis, noklusētā vērtība 0, bet tiek uzstādīta uz 1, ja formas
# parametrs neatbilst noteikumiem;
# • metode (1 punkts):
# o tilpums, kura aprēķina un atgriež veselu skaitli – bloka tilpumu kubikcentimetros.
# 2.11. Izveidot klases bloks konstruktoru, kas veic saņemto datu (argumentu) kontroli, izvadot
# atbilstošu paziņojumu, ja:
# 2.11.1. parametra forma vērtība neatbilst nosacījumiem (1 punkts) un uzstāda objekta
# parametra derīgums vērtību uz 0, citādi uzstāda derīguma vērtību uz 1 (1 punkts);
# 2.11.2. kubu skaits blokā neatbilst nosacījumiem (1 punkts).
# VISC Vaļņu ielā 2, Rīgā, LV-1050
# 29481647123802948164712380294816471238029481647123802948164720
# Eksāmens programmēšanā (augstākais līmenis) Skolēna darba lapa 2023 8
# 29481647123802948164712380294816471238029481647123802948164720
# 2.12. Izveidot klases bloks objektu, kas sastāv no 3 oranžas krāsas kubiem ar malas garumu
# 5 centimetri, formas numuru 13, un piešķirt tam nosacījumiem atbilstošu nosaukumu (4 punkti).
# 2.13. Izvadīt ekrānā izveidotā objekta nosaukumu un tilpumu (1 punkts).
# 2.14. Izveidot klases bloks objektu, kas sastāv no 5 zilas krāsas kubiem ar malas garumu
# 7 centimetri, formas numuru 23, un piešķirt tam nosacījumiem atbilstošu nosaukumu (2 punkti).
# 2.15. Izvadīt ekrānā izveidotā objekta nosaukumu un derīgumu (1 punkts).
# 2.16. Nomainīt objektam formas numuru uz 12 (1 punkts).
# 2.17. Izvadīt ekrānā izveidotā objekta nosaukumu un derīgumu (1 punkts)

class Kubs:
    def __init__(self, malas_garums, krasa):
        # 2.2. Datu kontrole
        if not (2 <= malas_garums <= 10):
            print(f"Malas garums {malas_garums} nav derīgs. Uzstādīts minimālais derīgais garums - 2.")
            malas_garums = 2
        self.malas_garums = malas_garums
        self.krasa = krasa

    def aprekinat_tilpumu(self):
        return self.malas_garums ** 3

    def __del__(self):
        print(f"Kubs ar krāsu {self.krasa} likvidēts.")


kubg = Kubs(10, "zaļa")

kubr = Kubs(1, "sarkana")

print(f"Objekta kubg krāsa: {kubg.krasa}")
print(f"Objekta kubg tilpums: {kubg.aprekinat_tilpumu()} cm³")

print(f"Objekta kubr malas garums: {kubr.malas_garums} cm")

del kubr #Objekta kubr dzēšana un 2.8. Pārbaude
try:
    print(kubr.malas_garums)
except NameError:
    print("Objekts kubr vairs nav pieejams.")

#Izvade objekta kubg malas garumam 
print(f"Objekta kubg malas garums: {kubg.malas_garums} cm")

#Klases Bloks definīcija un mantošana no Kubs
class Bloks(Kubs):
    def __init__(self, malas_garums, krasa, kubu_skaits, forma):
        super().__init__(malas_garums, krasa)
        
        # Privātā īpašība
        if not (1 <= kubu_skaits <= 4):
            print(f"Kubu skaits {kubu_skaits} nav derīgs. Uzstādīts noklusējums - 1.")
            self.__kubu_skaits = 1
        else:
            self.__kubu_skaits = kubu_skaits

        # Publiskās īpašības
        self.nosaukums = f"{krasa}{self.__kubu_skaits}"
        if forma not in [11, 12, 13, 14, 22]:
            print(f"Forma {forma} nav derīga. Uzstādīts derīgums uz 0.")
            self.derigums = 0
        else:
            self.derigums = 1
        self.forma = forma

    def tilpums(self):
        return self.__kubu_skaits * super().aprekinat_tilpumu()

#Izveidot Bloks objektu ar 3 oranžiem kubiem
bloks1 = Bloks(5, "oranža", 3, 13)
print(f"Bloka nosaukums: {bloks1.nosaukums}")
print(f"Bloka tilpums: {bloks1.tilpums()} cm³")

#Izveidot Bloks objektu ar 5 ziliem kubiem
bloks2 = Bloks(7, "zila", 5, 23)
print(f"Bloka nosaukums: {bloks2.nosaukums}")
print(f"Bloka derīgums: {bloks2.derigums}")

#Mainīt formas numuru uz 12 un izvadīt īpašības
bloks2.forma = 12
bloks2.derigums = 1 if bloks2.forma in [11, 12, 13, 14, 22] else 0
print(f"Bloka nosaukums: {bloks2.nosaukums}")
print(f"Bloka derīgums: {bloks2.derigums}")


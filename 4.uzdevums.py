# Jums jāizveido programma, kurai, ievadot vārdu, tas tiek novietots datu struktūrā atbilstoši
# latviešu alfabētam. Vietu alfabētā nosaka ievadītā vārda pirmais burts.
# Ja vārda pirmais burts atkārtojas, proti, tiek ievadīts vārds, kura vieta sarakstā jau ir aizņemta,
# vārdu apmaina pret ievadīto. Pārbaudīt lietotāja ievadi, lai lietotājs nevarētu ievadīt nederīgas
# vērtības. Par derīgu vērtību tiek uzskatīts tikai viens latviešu vārds, kurš sākas ar lielo burtu.
# Programmai jāpaziņo, ja ievadītā vērtība neatbilst minētajiem nosacījumiem, tad programmai
# jāpieprasa ievadīt jaunu vērtību. Ievadot vārdu, ir jāizvada programmas darbības soļi,
# piemēram, ja vārds vēl nav ievietots, programma izvada teikumu „Pievienoju vārdu 1. vietā”.
# Ņemt vērā, ka vārdu uzskaite alfabētā sākas ar kārtas skaitļa vietu Nr. 1.
# Programma darbojas, līdz tiek pilnībā aizpildīts viss alfabēta saraksts.
# Lai pārbaudītu programmas darbību, varat izmantot doto vārdu sarakstu:
# Ainaži, Saulkrasti, Dobele, Sigulda, Tukums, Liepāja, Talsi, Ludza, Cēsis, Gulbene, Ventspils,
# Vecumnieki, Engure, Ērgļi, Staicele, Kuldīga, Aizpute, Krāslava, Madona, Jūrmala, Rīga.
# Punkts par katru no šādām programmas darbībām:
# Vārda ievads
# 2.1. Nodrošināt vārda ievadīšanu.
# 2.2. Pārbaudīt lietotāja ievadīto vērtību, vai tas ir vārds (visas citas vērtības netiek ieskaitītas
# kā pareizas).
# 2.3. Katru reizi ievadīt tikai vienu vārdu, nevis vārdu virkni.
# 2.4. Pārbaudīt, vai vārda pirmais burts ir lielais burts.
# 2.5. Atkārtoti ievadīt vērtību, ja ievadītā vērtība bijusi kļūdaina.
# Datu struktūra
# 2.6. Izveidot datu struktūru, kurā uzglabāt latviešu alfabētu un tam atbilstošā sākumburta
# pozīcijas kārtas numuru.
# 2.7. Izveidot datu struktūru, kurā glabāt jauno izveidoto sarakstu.
# 2.8. Noteikt ievadītā vārda pirmo burtu.
# 2.9. Ja vārda pozīcija sarakstā jau ir aizņemta ar kādu vārdu, tad to aizvietot ar ievadīto vārdu.
# 2.10. Ja vārda pozīcijas sarakstā vārda nav, tad tajā tiek ievietots ievadītais vārds.
# 2.11. Pārbaudītais vārds tiek ievietots alfabēta secības atbilstošajā pozīcijā, ņemot vērā tā
# pirmo burtu.
# 2.12. Izdrukāt katru programmas darbību kā lasāmu teikumu.
# 2.13. Izvadīt kļūdas paziņojumu, ja ievadītais vārds neatbilst noteikumiem.
# 2.14. Datu struktūrā nedrīkst būt nultais elements.
# 2.15. Programma darbojas, līdz viss saraksts ir aizpildīts.

# Latviešu alfabēts un datu struktūras
alphabet = [
    "A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", 
    "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"
]

# Tukša datu struktūra vārdu glabāšanai
words = [None] * len(alphabet)

def get_valid_word():
    """Pieprasa un validē lietotāja ievadīto vārdu."""
    while True:
        word = input("Ievadiet latviešu valodas vārdu (sākas ar lielo burtu): ").strip()
        
        # Validācijas soļi
        if not word.isalpha():
            print("Kļūda: Jāievada tikai viens vārds, bez cipariem vai simboliem.")
        elif len(word.split()) > 1:
            print("Kļūda: Jāievada tikai viens vārds, nevis vārdu virkne.")
        elif word[0].isupper() is False:
            print("Kļūda: Vārds jāsāk ar lielo burtu.")
        else:
            return word

def add_word_to_list(word):
    """Pievieno vārdu sarakstam vai aizvieto esošu ierakstu."""
    first_letter = word[0].upper()
    
    # Atrodam vārda pozīciju alfabētā
    if first_letter in alphabet:
        index = alphabet.index(first_letter)
        if words[index] is None:
            words[index] = word
            print(f"Pievienoju vārdu {word} {index + 1}. vietā.")
        else:
            print(f"Aizvietoju vārdu {words[index]} ar {word} {index + 1}. vietā.")
            words[index] = word
    else:
        print(f"Kļūda: Burts {first_letter} nav latviešu alfabētā.")

# Galvenā programmas cilpa
print("Programma darbojas, līdz saraksts ir pilnībā aizpildīts.")
while None in words:
    word = get_valid_word()
    add_word_to_list(word)

# Izvada galīgo sarakstu
print("\nVārdu saraksts atbilstoši latviešu alfabētam:")
for i, word in enumerate(words, start=1):
    print(f"{i}. {word}")

#Piemērs
# Ievadiet latviešu valodas vārdu (sākas ar lielo burtu): Ainaži
# Ievadiet latviešu valodas vārdu (sākas ar lielo burtu): Saulkrasti
# ...

# Pievienoju vārdu Ainaži 1. vietā.
# Pievienoju vārdu Saulkrasti 22. vietā.
# ...
# Vārdu saraksts atbilstoši latviešu alfabētam:
# 1. Ainaži
# 2. None
# ...
# 22. Saulkrasti
# ...


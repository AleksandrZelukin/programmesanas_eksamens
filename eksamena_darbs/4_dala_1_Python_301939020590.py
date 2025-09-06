import requests
import json
import random

BOOKS_URL = "https://pro2025.azurewebsites.net/books"
JOURNALS_URL = "https://pro2025.azurewebsites.net/journals"

def get_books():
    response = requests.get(BOOKS_URL)
    if response.status_code == 200:
        print("Pieprasījums veiksmīgs (statusa kods 200).")
        return response.json()
    else:
        print(f"Kļūda! Statusa kods: {response.status_code}")
        return []

def print_books(books):
    for book in books:
        title = book.get("nosaukums", "")
        year = book.get("gads", "")
        pages = book.get("lappuses", "")
        print(f'Grāmata "{title}" ({year}), {pages} lpp.')

def save_titles_to_json(books, filename="nosaukumi.json"):
    titles = [book.get("nosaukums", "") for book in books]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(titles, f, ensure_ascii=False, indent=2)

def find_oldest_book(books):
    oldest = min(books, key=lambda b: b.get("gads", float("inf")))
    print(f'Visvecākā grāmata: {oldest.get("nosaukums", "")}')

def print_pages_and_avg_price(books):
    total_pages = sum(book.get("lappuses", 0) for book in books)
    prices = [book.get("cena", 0) for book in books if "cena" in book]
    avg_price = sum(prices) / len(prices) if prices else 0
    print(f'Kopējais lappušu skaits: {total_pages}')
    print(f'Vidējā cena: {avg_price:.2f}')

def garakais_nosaukums(books):
    return max(books, key=lambda b: len(b.get("nosaukums", "")))

def build_books_data(books):
    data = []
    for book in books:
        new_book = book.copy()
        if not new_book.get("autors"):
            new_book["autors"] = "Nav norādīts"
        data.append(new_book)
    return data

def print_authors_alphabetically(books_data):
    authors = sorted(set(book["autors"] for book in books_data))
    for author in authors:
        print(author)

def print_most_books_author(books_data):
    author_count = {}
    for book in books_data:
        author = book.get("author", book.get("autors", "Nav norādīts"))
        author_count.setdefault(author, []).append(book.get("name", book.get("nosaukums", "")))
    max_author = max(author_count.items(), key=lambda x: len(x[1]))
    author, titles = max_author
    print(f'Autors, kuram ir visvairāk grāmatu ({len(titles)}), - {author}:')
    for i, title in enumerate(titles, 1):
        print(f'{i}. "{title}"')

def get_journals():
    response = requests.get(JOURNALS_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Kļūda! Statusa kods: {response.status_code}")
        return []

def random_journals(journals, n=10):
    sample = random.sample(journals, min(n, len(journals)))
    return [{"nosaukums": j.get("name", ""), "izdevējs": j.get("publisher", "")}
            for j in sample]

def add_journal(journal_list):
    name = input("Ievadi žurnāla nosaukumu: ")
    publisher = input("Ievadi izdevēju: ")
    journal_list.insert(0, {"nosaukums": name, "izdevējs": publisher})

def delete_last_journal(journal_list):
    if journal_list:
        journal_list.pop()

def main():
    
    books = get_books()
    if not books:
        return

    
    print_books(books)

   
    save_titles_to_json(books)

   
    find_oldest_book(books)

    
    print_pages_and_avg_price(books)

    
    longest = garakais_nosaukums(books)
    print(f'Garākā nosaukuma grāmatas autors: {longest.get("autors", "Nav norādīts")}, gads: {longest.get("gads", "")}')

    
    books_data = build_books_data(books)

    
    print("Autori alfabētiskā secībā:")
    print_authors_alphabetically(books_data)

    
    print_most_books_author(books_data)

    
    journals = get_journals()
    journal_list = random_journals(journals, 10)
    print("Nejauši izvēlēti 10 žurnāli:")
    for j in journal_list:
        print(f'{j["nosaukums"]} ({j["izdevējs"]})')

    add_journal(journal_list)
    print("Pēc pievienošanas:")
    for j in journal_list:
        print(f'{j["nosaukums"]} ({j["izdevējs"]})')

    delete_last_journal(journal_list)
    print("Pēc pēdējā žurnāla dzēšanas:")
    for j in journal_list:
        print(f'{j["nosaukums"]} ({j["izdevējs"]})')

if __name__ == "__main__":
    main()
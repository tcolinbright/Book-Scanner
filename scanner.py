import csv
import requests
from bs4 import BeautifulSoup

def get_book_info_from_isbnsearch(isbn):
    url = f"https://isbnsearch.org/isbn/{isbn}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    book_info = {}
    book_info['title'] = soup.find('h1').text
    for div in soup.find_all('div', class_='bookinfo'):
        for p in div.find_all('p'):
            label, value = p.text.split(': ', 1)
            book_info[label] = value

    return book_info

def write_book_info_to_csv(isbn, bin_number, book_info):
    with open('books.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([isbn, bin_number] + list(book_info.values()))

def main():
    while True:
        isbn = input('Enter ISBN (or "q" to quit): ')
        if isbn.lower() == 'q':
            break

        book_info = get_book_info_from_isbnsearch(isbn)
        print(f"Here is the book information for ISBN {isbn}:")
        for key, value in book_info.items():
            print(f"{key}: {value}")

        confirmation = input("Is this correct? (Y/n): ")
        if confirmation.lower() != 'n':
            bin_number = input('Enter bin number: ')
            write_book_info_to_csv(isbn, bin_number, book_info)
        else:
            print("Please re-enter the correct ISBN.")

if __name__ == "__main__":
    main()

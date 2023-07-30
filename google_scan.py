

import csv
import requests
from creds import *



def get_book_info(isbn):
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}')
    return response.json()

def parse_book_info(json_response):
    volume_info = json_response['items'][0]['volumeInfo']
    title = volume_info.get('title')
    authors = volume_info.get('authors')
    publish_date = volume_info.get('publishedDate')
    page_count = volume_info.get('pageCount')
    image_links = volume_info.get('imageLinks')
    return title, authors, publish_date, page_count, image_links

def write_book_info_to_csv(isbn, bin_number, book_info):
    with open('g_books.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([isbn, bin_number] + list(book_info))

def main():
    while True:
        isbn = input('Enter ISBN (or "q" to quit): ')
        if isbn.lower() == 'q':
            break
        bin_number = input('Enter bin number: ')
        book_info = get_book_info(isbn)
        parsed_book_info = parse_book_info(book_info)
        write_book_info_to_csv(isbn, bin_number, parsed_book_info)

if __name__ == "__main__":
    main()

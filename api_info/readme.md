# Using Google Books ISBN API

Requirements:

- ISBN
- Google API Key
- Python 3

Example Information:

ISBN: 9781501143632

Title: "There's No Such Thing As Bad Weather"
Subtitle: "A Scandinavian Mom's Secret's for Raising Healthy, Resilient, and Confidnt Kids"
Author: McGurk, Linda Akeson


API Format:

https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}

...with example ISBN
https://www.googleapis.com/books/v1/volumes?q=isbn:9781501143632&key={api_key}
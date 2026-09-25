"""openlib_getter.app.main

Simple runner for the Open Library fetcher.

This module configures an `Openlibrary_client` with an author and sort
order, fetches search results from Open Library, and writes them to
`books.csv` using the provided saver.

Usage:
	python3 app/main.py

Adjust the `AUTHOR` and `SORT` constants below to change the query.
"""

from request import Openlibrary_client
from saver import to_csv

AUTHOR = "tolkien"
SORT = "new"

openlib_c = Openlibrary_client(author=AUTHOR, sort=SORT)
response_json = openlib_c.logic()

docs_parser = openlib_c.parser(response=response_json)
save_csv = to_csv()
save_csv.saver(data=openlib_c.RESULTS)
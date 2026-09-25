# OpenLib Getter

A tiny utility to fetch search results from the Open Library API by author
and save the results to a CSV file.

##### more about `Tolkien`:

- John Ronald Reuel Tolkien (3 January 1892 – 2 September 1973) was an English writer and academic philologist. He was the author of the high fantasy works `The Hobbit` (1937) and `The Lord of the Rings` (1954–1955).

![dd](https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d4/J._R._R._Tolkien%2C_ca._1925.jpg/250px-J._R._R._Tolkien%2C_ca._1925.jpg)
Features
- Query Open Library search by author and sort order
- Collect up to 50 documents from the response
- Persist results to `books.csv` as CSV rows

Requirements
- Python 3.8+
- requests (install with `pip install requests`)

Quickstart
1. Install dependencies:

```bash
python3 -m pip install requests
```

2. Run the script:

```bash
python3 app/main.py
```

3. After running, open `books.csv` in the repo root to inspect results.

Configuration
- Edit `app/main.py` to change the `AUTHOR` and `SORT` constants.
  - `AUTHOR` — author search term (e.g. `tolkien`)
  - `SORT` — sort order passed to the API (e.g. `new`)

Notes
- The project is intentionally minimal and designed as a small
  demonstration. It does not provide robust error handling or retries
  for failed HTTP calls; consider adding those for production use.

License
- Public domain / permissive for personal use. No warranty.
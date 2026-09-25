"""app.request

Small Open Library client for searching by author and sort order.

Classes:
    Openlibrary_client: fetches search results and keeps a limited
        list of docs in the `RESULTS` attribute.

This module relies on the `requests` package to perform HTTP calls.
"""

import requests


class Openlibrary_client:
    """Client to query Open Library search API and collect results.

    Attributes:
        RESULTS (list): accumulated list of document dicts collected from
            the search results. The parser appends up to 50 items.
    """

    RESULTS = []

    def __init__(self, author, sort):
        """Create a client for the given author and sort order.

        Args:
            author (str): author name used in the search query.
            sort (str): sort parameter for the Open Library API (e.g. "new").
        """
        self.author = author
        self.sort = sort

    def logic(self):
        """Perform the HTTP GET request to the Open Library search API.

        Returns:
            dict: parsed JSON response from the API.
        """
        __BASE_URL = (
            f"https://openlibrary.org/search.json?author={self.author}&sort={self.sort}"
        )

        response = requests.request("GET", __BASE_URL)

        return response.json()

    def parser(self, response):
        """Extract up to 50 docs from the API response into `RESULTS`.

        The method appends document dicts from `response['docs']` to the
        module-level `RESULTS` list until 50 items have been collected.

        Args:
            response (dict): JSON decoded response containing a `docs` list.
        """
        docs = response["docs"]

        counter = 1
        for doc in docs:
            if counter > 50:
                break
            self.RESULTS.append(doc)
            counter += 1
"""app.saver

Helpers to persist collected Open Library docs to CSV.

The module exposes a minimal `to_csv` class with a static `saver`
method that writes a list of dict-like objects to `books.csv`.
"""

import csv


class to_csv:
    """CSV writer helper.

    The `saver` method will inspect the keys of the provided data
    items to determine CSV headers and write all rows to `books.csv`.
    """

    @staticmethod
    def saver(data):
        """Write a list of dictionaries to `books.csv`.

        Args:
            data (list): iterable of dict-like objects to write as rows.
        """
        fieldnames = []

        for item in data:
            for key in item:
                if key not in fieldnames:
                    fieldnames.append(key)

        with open("books.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)
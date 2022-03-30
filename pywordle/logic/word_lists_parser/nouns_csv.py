import csv
from pathlib import Path

from pywordle.globals import WORKING_DIR

from pywordle.logic.word_lists_parser.base_parser import BaseParser, NormalizedSet


class NounsParser(BaseParser):
    @staticmethod
    def get_words() -> NormalizedSet:
        file = Path(WORKING_DIR) / "doc" / "word_lists" / "nouns.csv"

        german_nouns = []

        with file.open(newline="", mode="r", encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')

            for row in reader:
                word = row[0]
                pos = row[1]

                if "Substantiv" in pos:
                    german_nouns.append(word)

        return NormalizedSet(german_nouns)

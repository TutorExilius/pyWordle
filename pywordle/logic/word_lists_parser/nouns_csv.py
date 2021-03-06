"""The parser for nouns.csv"""

import csv
from pathlib import Path

from pywordle.logic.word_lists_parser.base_parser import (BaseParser,
                                                          NormalizedSet)
from pywordle.my_globals import WORKING_DIR


class NounsParser(BaseParser):  # pylint: disable=too-few-public-methods
    """The nouns.csv Parser"""

    @staticmethod
    def get_words() -> NormalizedSet:
        file = Path(WORKING_DIR) / "doc" / "word_lists" / "nouns.csv"

        german_nouns = []

        with file.open(newline="", mode="r", encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')

            for row in reader:
                word = row[0]
                pos = row[1]

                if pos == "Substantiv":
                    german_nouns.append(word)

        return NormalizedSet(german_nouns)

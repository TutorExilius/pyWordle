"""The parser for word_list_1.txt"""

from pathlib import Path

from pywordle.logic.word_lists_parser.base_parser import (BaseParser,
                                                          NormalizedSet)
from pywordle.my_globals import WORKING_DIR


class WordList1Parser(BaseParser):  # pylint: disable=too-few-public-methods
    """The word_list_1.txt Parser"""

    @staticmethod
    def get_words() -> NormalizedSet:
        file_path = Path(WORKING_DIR) / "doc" / "word_lists" / "word_list_1.txt"

        german_nouns = []

        with file_path.open(mode="r", encoding="utf8") as file:
            ignore_lines = 1

            for line in file:
                if ignore_lines > 0:
                    ignore_lines -= 1
                    continue

                line = line.strip()

                if line:
                    parts = line.split()
                    german_noun = parts[-1]
                    german_nouns.append(german_noun)

        return NormalizedSet(german_nouns)

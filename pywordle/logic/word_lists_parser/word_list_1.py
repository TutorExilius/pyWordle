from pathlib import Path

from pywordle.globals import WORKING_DIR
from pywordle.logic.word_lists_parser.base_parser import BaseParser, NormalizedSet


class WordList1Parser(BaseParser):
    @staticmethod
    def get_words() -> NormalizedSet:
        file = Path(WORKING_DIR) / "doc" / "word_lists" / "word_list_1.txt"

        german_nouns = []

        with file.open(mode="r", encoding="utf8") as f:
            ignore_lines = 1

            for line in f:
                if ignore_lines > 0:
                    ignore_lines -= 1
                    continue

                line = line.strip()

                if line:
                    parts = line.split()
                    german_noun = parts[-1]
                    german_nouns.append(german_noun)

        return NormalizedSet(german_nouns)

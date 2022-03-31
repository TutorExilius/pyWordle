from pywordle.logic import db_manager as dbm
from pywordle.logic.word_lists_parser.nouns_csv import NounsParser
from pywordle.logic.word_lists_parser.word_list_1 import WordList1Parser


def upper(word):
    return word.replace("ß", "ẞ").upper()


german_nouns = WordList1Parser.get_words() | NounsParser.get_words()
dbm.add_word_list([upper(word) for word in german_nouns])

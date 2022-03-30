from abc import ABC


class NormalizedSet(set[str]):
    def __init__(self, word_list: list[str]) -> None:
        super().__init__(NormalizedSet._normalized_list(word_list))

    @staticmethod
    def _normalized_list(word_list: list[str]) -> list[str]:
        """Remove words with len != 5 and keep words that contains only 'allowed_characters':
                abcdefghijklmnopqrstuvwxyzäöüß

        :param word_list: List of words
        :type word_list: list[str]
        :return: A list of worlds with a len of 5 and 'allowed_characters'
        :rtype list[str]
        """

        allowed_characters = "abcdefghijklmnopqrstuvwxyzäöüß"

        word_list_ = [
            word.lower()
            for word in word_list
            if len(word) == 5 and all(ch in allowed_characters for ch in word.lower())
        ]

        return word_list_


class BaseParser(ABC):
    def __init__(self) -> None:
        self.word_list: list[str] = []

    @staticmethod
    def get_words() -> NormalizedSet:
        raise NotImplementedError()

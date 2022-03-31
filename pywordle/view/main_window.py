"""The main window widget"""

import re
from enum import IntEnum

from PySide2.QtWidgets import QMainWindow, QWidget

from pywordle.logic import db_manager
from pywordle.model.models import Word
from pywordle.view.ui.ui_main_window import Ui_MainWindow


class GueissingPositionState(IntEnum):
    """Guessed states"""

    UNKNOWN = 0
    CORRECT_POSITION = 1
    EXIST_ON_OTHER_POSITION = 2
    DOES_NOT_EXIST = 3


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main window widget."""

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setupUi(self)

        self.random_word: None | Word = db_manager.get_random_word()

        if self.random_word is None:
            raise ValueError("No word in database found.")

    def validate_guessing(self, word: str) -> list[GueissingPositionState]:
        """Validated word against random word.

        :param word: Guessed word.
        :type word: str
        :return: List of guessed postion states.
        :rtype: list[GueissingPositionState]
        """

        random_word: str = self.random_word.word if self.random_word is not None else ""

        guessed_positions = list(
            map(
                lambda ch_tuple: ch_tuple[0] == ch_tuple[1],
                zip(random_word, word),
            )
        )
        # convert bool to GueissingPositionState
        guessed_positions_states = [
            GueissingPositionState(int(guessed_position))
            for guessed_position in guessed_positions
        ]

        for position, position_state in enumerate(guessed_positions_states):
            if position_state == GueissingPositionState.CORRECT_POSITION:
                continue

            letter = word[position]

            other_positions = [ch.start() for ch in re.finditer(letter, random_word)]
            other_positions = list(
                filter(
                    lambda other_position: guessed_positions_states[other_position]
                    == GueissingPositionState.UNKNOWN,
                    other_positions,
                )
            )

            # update guessed_positions_states with other position found
            if other_positions:
                guessed_positions_states[
                    position
                ] = GueissingPositionState.EXIST_ON_OTHER_POSITION

        # update unknowns to GueissingPositionState.DOES_NOT_EXIST
        for position, guessed_positions_state in enumerate(guessed_positions_states):
            if guessed_positions_state == GueissingPositionState.UNKNOWN:
                guessed_positions_states[
                    position
                ] = GueissingPositionState.DOES_NOT_EXIST

        return guessed_positions_states

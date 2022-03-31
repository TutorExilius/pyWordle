"""The main window widget"""

import re
from enum import IntEnum
from functools import partial

from PySide2.QtWidgets import QMainWindow, QMessageBox, QPushButton, QWidget

from pywordle.logic import db_manager
from pywordle.logic.helper import get_app_version
from pywordle.model.models import Word
from pywordle.my_globals import WORKING_DIR
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
        self.setWindowTitle(
            f"{self.windowTitle()} v{get_app_version(working_dir=WORKING_DIR)}"
        )

        self.random_word: None | Word = db_manager.get_random_word()

        if self.random_word is None:
            raise ValueError("No word in database found.")

        print("Random word:", self.random_word.word)

        self._current_run = 1
        self._input_rows = {
            1: self.frame_run_1,
            2: self.frame_run_2,
            3: self.frame_run_3,
            4: self.frame_run_4,
            5: self.frame_run_5,
            6: self.frame_run_6,
        }

        self._current_row = self._input_rows[self._current_run]
        self._current_field = self._get_first_or_selected_input_field()

        # connections
        self.actionAbout_Qt.triggered.connect(  # pylint: disable=no-member
            lambda *args, **kwargs: QMessageBox.aboutQt(self)
        )

        for frame in self._input_rows.values():
            for child in frame.children():
                if isinstance(child, QPushButton):
                    child.clicked.connect(  # pylint: disable=no-member
                        self._update_current_field
                    )

        for child in self.frame_inputs.children():
            if isinstance(child, QPushButton):
                input_letter = child.text()

                if input_letter == "DEL":
                    child.clicked.connect(  # pylint: disable=no-member
                        self._delete_and_update_field
                    )
                elif input_letter == "SEND":
                    child.clicked.connect(  # pylint: disable=no-member
                        self._validate_and_send
                    )
                else:
                    child.clicked.connect(  # pylint: disable=no-member
                        partial(self._set_field_value, input_letter)
                    )

    def _validate_and_send(self) -> None:
        """Validate input row and send if word is exists."""

        word = "".join([field.text() for field in self._get_sorted_input_fields()])

        if db_manager.exist(word):
            result_list = self.validate_guessing(word)
            self._colorize_input_row(result_list)
            all_correct = all(
                result == GueissingPositionState.CORRECT_POSITION
                for result in result_list
            )

            self._select_next_input_row(all_correct)
        else:
            self._not_a_word()
            print("not a word")

    def _colorize_input_row(self, result_list: list[GueissingPositionState]) -> None:
        input_fields = self._get_sorted_input_fields()
        colors = {
            GueissingPositionState.CORRECT_POSITION: "#228B22",  # green
            GueissingPositionState.EXIST_ON_OTHER_POSITION: "#FFD700",  # yellow/gold
            GueissingPositionState.DOES_NOT_EXIST: "#a0a0a0",  # gray
        }

        for i, field in enumerate(input_fields):
            guessing_state = result_list[i]
            new_style_sheet = (
                field.styleSheet()
                .replace(  # first replace for QPushButton
                    "background-color: white",
                    f"background-color: {colors[guessing_state]}",
                )
                .replace(  # second replace for QPushButton:focus
                    "background-color: white",
                    f"background-color: {colors[guessing_state]}",
                )
            )
            field.setStyleSheet(new_style_sheet)

    def _delete_and_update_field(self) -> None:
        """Clean current focused field and focus field before."""

        if self._current_field is None:
            self._current_field = self._get_first_or_selected_input_field(
                use_reversed=True
            )

        self._current_field.setText("")
        # self._select_next_input_field(use_reversed=True)

    def _update_current_field(self) -> None:
        """Is updating the current field."""

        self._current_field = self._get_first_or_selected_input_field()

    def _set_field_value(self, letter: str) -> None:
        """Set current fields value.

        :param letter: The input letter.
        :type letter: str
        """

        if self._current_field is None:
            return

        self._current_field.setText(letter)
        self._select_next_input_field()

    def _get_sorted_input_fields(self, use_reversed: bool = False) -> list[QPushButton]:
        input_fields = [
            child
            for child in self._current_row.children()
            if isinstance(child, QPushButton)
        ]

        input_fields = sorted(
            input_fields,
            key=lambda input_field: input_field.objectName(),
            reverse=use_reversed,
        )

        return input_fields

    def _select_next_input_field(self, use_reversed: bool = False) -> None:
        """Select next input field in row.
        If reversed is False, get next field in right direction,
        if reversed is True, get next field in left direction.
        If last field is reached, focus will be removed.
        """

        if self._current_field is None:
            self._current_field = self._get_first_or_selected_input_field(
                use_reversed=use_reversed
            )
            return

        input_fields = self._get_sorted_input_fields(use_reversed=use_reversed)

        for input_field in input_fields:
            if use_reversed is False:
                field_source = self._current_field.objectName()
                field_target = input_field.objectName()
            else:
                field_source = input_field.objectName()
                field_target = self._current_field.objectName()

            if field_source >= field_target:
                continue

            self._current_field = input_field
            self._current_field.setFocus()
            break
        else:
            if use_reversed is False:
                self._current_field.clearFocus()
                self._current_field = None

    def _select_next_input_row(self, guessed: bool) -> None:
        """Select next row. If last row is reached, switch to game_over state."""

        if guessed:
            self._game_won()
            self.close()
        elif self._current_run == 6:
            self._game_lost()
            self.close()
        else:
            self._current_run += 1
            self._current_row.setEnabled(False)
            self._current_row = self._input_rows[self._current_run]
            self._current_row.setEnabled(True)
            self._select_next_input_field()

    def _game_won(self) -> None:
        """Show game won dialog."""

        msg_box = QMessageBox(self)
        msg_box.setText("You nailed it<br>Congratulation!")
        msg_box.setWindowTitle("Congratulation!")
        msg_box.exec_()

    def _game_lost(self) -> None:
        """Show game lost dialog."""

        msg_box = QMessageBox(self)
        msg_box.setText("You loose :(")
        msg_box.setWindowTitle("Game Over")
        msg_box.exec_()

    def _not_a_word(self) -> None:
        """Show not a word dialog."""

        msg_box = QMessageBox(self)
        msg_box.setText("Not a word!")
        msg_box.setWindowTitle("Nope")
        msg_box.exec_()

    def _get_first_or_selected_input_field(
        self, use_reversed: bool = False
    ) -> QPushButton:
        """Get first or selected input field (QPushButton) of current activated
        input row (QFrame).

        :return: The current input field.
        :rtype: QPushButton
        :raise: ValueError
        """

        input_fields = self._get_sorted_input_fields(use_reversed=use_reversed)

        focused_input_fields = [
            input_field for input_field in input_fields if input_field.hasFocus()
        ]

        if len(focused_input_fields) > 1:
            raise ValueError("Invalid state: more than one QPushButton is selected.")

        if focused_input_fields:
            return focused_input_fields[0]

        return input_fields[0]

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
                    != GueissingPositionState.CORRECT_POSITION,
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

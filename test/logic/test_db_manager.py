"""All tests for DBManager"""

import pytest
from pywordle.logic.db_manager import exist, get_random_word, add_word
from pywordle.model.models import Base, Word
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestDBManager:
    """Testclass for DBManager (db_manager.py)"""

    @pytest.fixture(autouse=True)
    def _setup(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(engine)
        self.objects = [
                Word(word="KATZE"),
                Word(word="HUNDI"),
            ]
        self._fill_db()

    def _fill_db(self):
        with self.Session() as session:
            session.bulk_save_objects(self.objects)
            session.commit()

    def test_add_word(self, mocker):
        session = self.Session()
        mocker.patch(
            "pywordle.logic.db_manager.Session"
        ).return_value.__enter__.return_value = session

        new_word = "KATER"
        assert not exist(new_word)
        add_word(new_word)
        assert exist(new_word)

    def test_exist(self, mocker):
        session = self.Session()
        mocker.patch(
            "pywordle.logic.db_manager.Session"
        ).return_value.__enter__.return_value = session
        assert exist("HUNDI")
        assert not exist("ABCDE")

    def test_get_random_word(self, mocker):
        session = self.Session()
        mocker.patch(
            "pywordle.logic.db_manager.Session"
        ).return_value.__enter__.return_value = session

        for _ in range(10):
            assert get_random_word().word in [word.word for word in self.objects]


"""All tests for DBManager"""

import pytest
from pywordle.logic.db_manager import exist
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
        self._fill_db()

    def _fill_db(self):
        with self.Session() as session:
            objects = [
                Word(word="KATZE"),
                Word(word="HUNDI"),
            ]
            session.bulk_save_objects(objects)
            session.commit()

    def test_exist(self, mocker):
        session = self.Session()
        mocker.patch(
            "pywordle.logic.db_manager.Session"
        ).return_value.__enter__.return_value = session
        assert exist("HUNDI")

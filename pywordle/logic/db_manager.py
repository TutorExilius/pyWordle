from datetime import datetime
from typing import List

from more_itertools import chunked

from pywordle import globals
from pywordle.model.models import Word
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

engine = create_engine(globals.DATABASE_URL)
Session = sessionmaker(engine)


def add_word(word: str, ignore_unique_constraint_exception=False) -> None:
    with Session() as session:
        if ignore_unique_constraint_exception:
            session_add = session.add

            def add(*args, **kwargs):
                try:
                    session_add(args, kwargs)
                except:  # ignore exception
                    pass

            session.add = add

        session.add(
            Word(
                word=word,
                created_at=datetime.utcnow(),
            )
        )
        session.commit()


def add_word_list(word_list: List[str]) -> None:
    bulk_size = 1000
    words = [
        Word(word=word, created_at=datetime.utcnow())
        for word in word_list
    ]

    chunks = chunked(words, bulk_size)

    print(len(words))
    with Session() as session:
        i = 0
        for chunk in chunks:
            session.bulk_save_objects(chunk, return_defaults=False)

        session.commit()


def delete_word(word_id: int) -> None:
    with Session() as session:
        word = session.query(Word).get(word_id)
        session.delete(word)
        session.commit()

def set_enable(word_id: int, enable: bool) -> None:
    with Session() as session:
        word = session.query(Word).get(word_id)
        word.enabled = enable
        session.commit()

def set_nsfw(word_id: int, is_nsfw: bool) -> None:
    with Session() as session:
        word = session.query(Word).get(word_id)
        word.nsfw = is_nsfw
        session.commit()

def get_word_case_insensitive(word: str) -> Word|None:
    with Session() as session:
        word = session.query(Word).filter(func.lower(Word.word) == func.lower(word)).one_or_none()

    return word

def get_random_word(beginning_letter=None) -> Word|None:
    with Session() as session:
        if beginning_letter is None:
            word = session.query(Word).order_by(func.random()).first()
        else:
            word = session.query(Word).filter(Word.word.startswith(beginning_letter)).order_by(func.random()).first()

    return word


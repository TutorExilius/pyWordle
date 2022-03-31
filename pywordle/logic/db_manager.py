"""
DB Manager
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, List

from more_itertools import chunked
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from pywordle import my_globals
from pywordle.model.models import Word

engine = create_engine(my_globals.DATABASE_URL)
Session = sessionmaker(engine)


def add_word(word: str, ignore_unique_constraint_exception: bool = False) -> None:
    """Add given word to database.

    :param word: Word to add
    :type word: str
    :param ignore_unique_constraint_exception:
        If true, ignore insert exceptions,
        if false, raise insetr exceptions like UNIQUE CONSTRAINT errors etc.
    :type ignore_unique_constraint_exception: bool
    """

    with Session() as session:
        if ignore_unique_constraint_exception:
            session_add = session.add

            def add(*args: list[Any], **kwargs: dict[Any, Any]) -> None:
                try:
                    session_add(args, kwargs)
                except SQLAlchemyError:  # nolint # noqa
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
    """Add words of list to database (bulk insert).

    :param word_list: List of words
    :type word_list: list[str]
    """

    bulk_size = 1000
    words = [Word(word=word, created_at=datetime.utcnow()) for word in word_list]

    chunks = chunked(words, bulk_size)

    print(len(words))
    with Session() as session:
        for chunk in chunks:
            session.bulk_save_objects(chunk, return_defaults=False)

        session.commit()


def delete_word(word_id: int) -> None:
    """Delete word by given word_id.

    :param word_id: ID of the word.
    :type word_id: int
    """

    with Session() as session:
        word = session.query(Word).get(word_id)
        session.delete(word)
        session.commit()


def set_enable(word_id: int, enable: bool) -> None:
    """Set enable flag of word by given word_id.

    :param word_id: ID of the word.
    :type word_id: int
    :param enable: Enable flag
    :type enable: bool
    """

    with Session() as session:
        word = session.query(Word).get(word_id)
        word.enabled = enable
        session.commit()


def set_nsfw(word_id: int, is_nsfw: bool) -> None:
    """Set nsfw flag of word by given word_id.

    :param word_id: ID of the word.
    :type word_id: int
    :param is_nsfw: NSFW flag
    :type is_nsfw: bool
    """

    with Session() as session:
        word = session.query(Word).get(word_id)
        word.nsfw = is_nsfw
        session.commit()


def get_random_word(
    allow_nsfw_words: bool = True,
    allow_disabled_words: bool = False,
) -> None | Word:
    """Get a random word from database.

    :return:
        A random word record, that is enabled and nsfw flag will
        be ignored (default).
        If allow_nsfw_words is True (default), all words (nsfw included)
        will be considered.
        If allow_nsfw_words is False, words with nsfw=True
        will be ignored.

        If allow_disabled_words is True, all words (disabled included)
        will be considered.
        If allow_disabled_words is False (default), disabled words
        will be ignored.
    :rtype: None | Word
    """

    with Session() as session:
        query = session.query(Word)

        if not allow_nsfw_words:
            query = query.filter(Word.nsfw.is_(False))

        if not allow_disabled_words:
            query = query.filter(Word.enabled.is_(True))

        word = query.order_by(func.random()).first()

    return word

"""SQLAlchemy database models"""

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        MetaData, String)
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

Base: DeclarativeMeta = declarative_base(metadata=meta)


class BaseModel(Base):  # pylint: disable=too-few-public-methods
    """The base model for all SQLAlchemy database models."""

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())


class Word(BaseModel):  # pylint: disable=too-few-public-methods
    """The Word model"""

    __tablename__ = "words"

    word = Column(
        String(5, collation="NOCASE"),
        unique=True,
        nullable=False,
    )

    @validates("word")
    def validate_word(self, _: str, value: str) -> str:  # pylint: disable=no-self-use
        """Validate the word attribute and check the lenght (len==5 required).

        :param value: The corresponding value of column 'word'.
        :type value: str
        :return: The validated word(str).
        :rtype: str
        :raise: ValueError
        """

        if len(value) != 5:
            raise ValueError(
                f"Lenght error - word: '{value}'. The word length must be exact 5!"
            )

        return value

    enabled = Column(Boolean, default=True)
    nsfw = Column(Boolean, default=False)
    results = relationship(
        "Result", back_populates="word", cascade="all, delete-orphan"
    )


class Result(BaseModel):  # pylint: disable=too-few-public-methods
    """The Result model"""

    __tablename__ = "results"

    word_id = Column(Integer, ForeignKey("words.id", ondelete="cascade"))
    word = relationship("Word", back_populates="results")

    guessed_in_run = Column(Integer, nullable=True, default=None)

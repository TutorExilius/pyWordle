from sqlalchemy import Boolean, Column, DateTime, Integer, MetaData, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
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


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())


class Word(BaseModel):
    __tablename__ = "words"

    word = Column(
        String(5, collation='NOCASE'),
        unique=True,
        nullable=False,
    )

    @validates('word')
    def validate_word(self, column, value):
        if len(value) != 5:
            raise ValueError(f"Lenght error - word: '{value}'. The word length must be exact 5!")

        return value

    enabled = Column(Boolean, default=True)
    nsfw = Column(Boolean, default=False)
    results = relationship("Result", back_populates="word", cascade="all, delete-orphan")


class Result(BaseModel):
    __tablename__ = "results"

    word_id = Column(Integer, ForeignKey('words.id', ondelete="cascade"))
    word = relationship("Word", back_populates="results")

    guessed_in_run = Column(Integer, nullable=True, default=None)

import ormar
from databases import Database

import ormar_postgres_full_text

from .meta import meta

database = Database("postgresql://test:test@localhost:5432/test")


class FulltextModel(ormar.Model):
    class Meta:
        database = database
        metadata = meta

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    text: str = ormar_postgres_full_text.TSVector()

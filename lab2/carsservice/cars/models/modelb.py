import os
from peewee import Model, PostgresqlDatabase

pp = ''.join('DATA_BASE_PORT')
pg_db = PostgresqlDatabase(
    os.getenv('DATA_BASE_NAME'),
    user=os.getenv('DATA_BASE_USER'),
    password=os.getenv('DATA_BASE_PASS'),
    host=os.getenv('DATA_BASE_HOST'),
    port=int(os.getenv(pp))
)


class BaseModel(Model):
    class Meta:
        database = pg_db
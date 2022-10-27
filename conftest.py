import pytest
import psycopg2
from db_config import *

@pytest.fixture()
def setup():
    conn = psycopg2.connect(
        database=db_config["database"],
        user=db_config["user"],
        host=db_config["host"],
        password=db_config["password"]
    )

    cur = conn.cursor()

    yield cur
    conn.commit()

    # Close communication with the database

    cur.close()
    conn.close()

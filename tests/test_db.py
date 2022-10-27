import pytest


@pytest.mark.database
class TestDataBase:

    def test_create_table(self, setup):
        setup.execute("CREATE TABLE table_for_test (id serial PRIMARY KEY, num integer, data varchar);")

    def test_insert_values(self, setup):
        setup.execute("INSERT INTO table_for_test (num, data) VALUES (%s, %s)",(100, "abc'def"))

    def test_get_value(self, setup):
        setup.execute("SELECT * FROM table_for_test;")
        print(setup.fetchone())

# def test_drop_table(setup):
#     setup.execute("DROP TABLE table_for_test")
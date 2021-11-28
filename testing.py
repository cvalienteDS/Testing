import unittest
import db_module
import sqlite3

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        conn = sqlite3.connect(':memory:')

        cls.c = conn.cursor()

        sql_file = open("data.db.sql")
        sql_as_string = sql_file.read()
        cls.c.executescript(sql_as_string)

        # c.execute("""CREATE TABLE products (product_id text primary key, name text)""")
        # c.execute("""CREATE TABLE visits (user_id INTEGER, YearMonthDay TEXT, product_id TEXT, price text, purchased text)""")
        # with conn:
        #     c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        cls.c.close()

    def test_mean_bought_given_user(self):
        self.assertEqual(db_module.DB.mean_bought_given_user('U90'), 41.245625)
        self.assertIsInstance(db_module.DB.mean_bought_given_user('U90'), float)

    def test_sales_mean_by_month_given_year(self):
        self.assertEqual(db_module.DB.sales_mean_by_month_given_year('2021'), 48.100087197811526)
        self.assertIsInstance(db_module.DB.sales_mean_by_month_given_year('2021'), float)

    def test_sales_mean_by_product(self):
        self.assertEqual(db_module.DB.sales_mean_by_product(), [('Bolso', 25.019287128712886), ('Perfume', 45.03208015267181), ('Gafas', 77.02116883116881)])
        self.assertIsInstance(db_module.DB.sales_mean_by_product(), list)


if __name__ == '__main__':
    unittest.main()

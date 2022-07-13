import unittest
from db import db_module


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up environment for testing: Creating and populating sqlite test database')
        cls.test_db_instance = db_module.DB()   # creates an in memory sqlite database

        cls.cur = cls.test_db_instance.cur

        with open("data.db.sql") as sql_file:
            sql_as_string = sql_file.read()
            cls.cur.executescript(sql_as_string)  # executes external script to populate test database

    @classmethod
    def tearDownClass(cls):
        print('Closing sqlite test database connection')
        cls.test_db_instance.con.close()

    def test_mean_bought_given_user(self):
        actual = self.test_db_instance.mean_bought_given_user(user='U90')
        expected = 41.245625
        with self.subTest():
            self.assertEqual(actual, expected)
            self.assertIsInstance(self.test_db_instance.mean_bought_given_user(user='U90'), float, f'Actual output is not an instance of {float}')

    def test_sales_mean_by_month_given_year(self):
        with self.subTest():
            actual = self.test_db_instance.sales_mean_by_month_given_year('2021')
            expected = 48.100087197811526
            self.assertEqual(actual, expected)
            self.assertIsInstance(actual, float, f'Actual output is not an instance of {float}')

    def test_sales_mean_by_product(self):
        with self.subTest():
            actual = self.test_db_instance.sales_mean_by_product()
            expected = [('Bolso', 25.019287128712886), ('Perfume', 45.03208015267181), ('Gafas', 77.02116883116881)]
            self.assertEqual(actual, expected)
            self.assertIsInstance(actual, list, f'Actual output is not an instance of {list}')


if __name__ == '__main__':
    unittest.main()

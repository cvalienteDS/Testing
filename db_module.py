import sqlite3
import logging
import sys
import os

logger = logging.getLogger(__name__)


class DB:
    def __init__(self,
                 path):
        self.path = path
        self.cur = self.db_connect()

    def db_connect(self):
        if os.path.isfile(self.path):
            con = sqlite3.connect(self.path)
            cur = con.cursor()
        else:
            logger.error("Error during db connection. Filename doesnt exist: {}".format(self.path))
            sys.exit(1)
        return cur

    def mean_bought_given_user(self, user):
        try:
            str(user)
        except ValueError:
            logger.error("User argument {} can´t be converted to string".format(user))

        try:
            self.cur.execute(
                """
                SELECT avg(price) AS MEAN_BOUGHT
                FROM visits
                WHERE purchased = 'True' and user_id = :user
                """
                , {"user": user}
            )
        except sqlite3.Error as e:
            logger.error(e)
        try:
            return self.cur.fetchone()[0]
        except TypeError:
            return None

    def sales_mean_by_month_given_year(self, year):
        try:
            str(year)
        except ValueError:
            logger.error("Year argument {} can´t be converted to string".format(year))

        try:
            self.cur.execute(
                """
            WITH CTE AS (
                SELECT avg(price) AS SALES_MEAN  
                FROM visits
                WHERE purchased = 'True' and SUBSTR(YearMonthDay, 1, 4) = :year
                GROUP BY SUBSTR(YearMonthDay, 6, 2) 
                )
            SELECT avg(SALES_MEAN) AS MONTHLY_MEAN FROM CTE
                """
                , {"year": year}
            )
        except sqlite3.Error as e:
            logger.error(e)

        try:
            return self.cur.fetchone()[0]
        except TypeError:
            return None

    def sales_mean_by_product(self):
        try:
            self.cur.execute(
                """
                SELECT name, avg(price) AS SALES_MEAN
                FROM visits v
                LEFT JOIN products p ON v.product_id = p.product_id
                WHERE purchased = 'True'
                GROUP BY v.product_id
                """
            )
        except sqlite3.Error as e:
            logger.error(e)

        try:
            return self.cur.fetchall()
        except:
            return None

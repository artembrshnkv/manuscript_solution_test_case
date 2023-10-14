import sqlite3 as sq

from excel_sheet import wb_data
from utils import sheet_titles, generate_barcode, isg_table_rows, country_table_rows


with sq.connect(database='manuscript_solution_test_case.db') as conn:
    cur = conn.cursor()

    def create_isg_tabel():
        cur.execute("""CREATE TABLE IF NOT EXISTS ISG(
        ID_ISG INTEGER PRIMARY KEY, 
        NAME_ISG TEXT NOT NULL
        )
        """)

    def create_country_table():
        cur.execute("""
        CREATE TABLE IF NOT EXISTS COUNTRY(
        ID_COUNTRY INTEGER PRIMARY KEY AUTOINCREMENT, 
        NAME_COUNTRY TEXT UNIQUE NOT NULL
        )
        """)

    def create_goods_table():
        cur.execute("""
        CREATE TABLE IF NOT EXISTS GOODS(
        ID_TOVAR INTEGER NOT NULL, 
        NAME_TOVAR TEXT NOT NULL, 
        BARCODE INTEGER,
        ID_COUNTRY INTEGER REFERENCES COUNTRY(ID_COUNTRY), 
        ID_ISG INTEGER REFERENCES ISG(ID_ISG)
        )
        """)


    def insert_values_to_isg_table(data):
        for row in data:
            cur.execute("""
            INSERT INTO ISG (ID_ISG, NAME_ISG) VALUES(?, ?)
            """,
                        (row[0], row[1])
                        )
            conn.commit()

    def insert_values_to_country_table(data):
        for country in data:
            cur.execute("""
            INSERT INTO COUNTRY (NAME_COUNTRY) VALUES (? )
            """,
                        (country, )
                        )
            conn.commit()

    def get_country_id_by_name(country_name):
        cur.execute("""
        SELECT ID_COUNTRY FROM COUNTRY
        WHERE NAME_COUNTRY = (?)
        """,
                    (country_name, )
                    )

        return cur.fetchone()[0]


    def insert_values_to_goods_table(data):
        for row in data:
            cur.execute("""
            INSERT INTO GOODS VALUES (?, ?, ?, ?, ?)
            """,
                        (row[sheet_titles['ID_TOVAR']],
                         row[sheet_titles['TOVAR']],
                         generate_barcode(row),
                         get_country_id_by_name(row[sheet_titles['COUNTRY']]),
                         row[sheet_titles['ID_ISG']]
                         )
                        )
        conn.commit()

    def select_goods_by_countries():
        cur.execute("""
        SELECT NAME_COUNTRY, count(GOODS.ID_COUNTRY) as quantity
        FROM GOODS JOIN COUNTRY ON COUNTRY.ID_COUNTRY = GOODS.ID_COUNTRY
        GROUP BY NAME_COUNTRY
        ORDER BY quantity DESC
        """)
        return cur.fetchall()

quantity_by_countries = select_goods_by_countries()

if __name__ == '__main__':
    print(quantity_by_countries)






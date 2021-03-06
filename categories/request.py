import sqlite3
from models import Category
import json


def get_all_categories():

    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
        SELECT
            c.id,
            c.label
        FROM Categories c
        ORDER BY label ASC
        """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)
    return json.dumps(categories)


def create_new_category(new_cat):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
        INSERT INTO Categories
            ( label )
        Values
            (?);
        """, (new_cat['label'],))
        id = db_cursor.lastrowid
        new_cat['id'] = id
    return json.dumps(new_cat)

from dataclasses import dataclass,field
from datetime import datetime
from typing import Union
import sqlite3
import os

@dataclass
class Database():
    dbname: str = field()
    tablename: str = field(default='Classified')
    conn: sqlite3.Connection = field(init=False, repr=False)
    c: sqlite3.Cursor = field(init=False, repr=False)

    def __post_init__(self):
        self.conn = sqlite3.connect(self.dbname)
        self.c = self.conn.cursor()

    @property
    def size(self):         # Size in MB #
        try:
            with self.conn:
                self.c.execute('SELECT page_count * page_size FROM pragma_page_count() , pragma_page_size')
                size_info = self.c.fetchone()
                size = size_info[0] / 1024 / 1024
                return size
        except sqlite3.Error as e:
            return (0, e)

    @property
    def last_mod(self) -> Union[datetime, tuple]:
        try:
            time_stat = datetime.fromtimestamp(os.stat(self.dbname).st_mtime)
            return time_stat

        except OSError as e:
            return (0, e)

    @property
    def default_routing(self):
        return (f'DEFAULT ROUTING ALL METHODS TO "{self.tablename}"')

    def query(self, *querys: str) -> list:
        result = []
        for i, query in enumerate(querys):
            if not isinstance(query, str):
                result.append({f'query{i+1}': (0.0, TypeError)})
            try:
                with self.conn:
                    self.c.execute(query)
                    if self.c.rowcount == 1:
                        result.append({f'query{i+1}': self.c.fetchone()})
                    else:
                        result.append({f'query{i+1}': self.c.fetchall()})

            except sqlite3.Error as e:
                result.append({f'query{i+1}': (0, e)})
        return result

    def addtable(self, optional_tablename=None):
        if optional_tablename is None:
            try:
                with self.conn:
                    self.c.execute(f"CREATE TABLE IF NOT EXISTS {self.tablename} "
                                   "(ID INTEGER PRIMARY KEY,Content BLOB ,Key TEXT )")
                return 11
            except sqlite3.Error as e:
                return (0.0, e)

        else:
            try:
                with self.conn:
                    self.c.execute(f"CREATE TABLE IF NOT EXISTS {optional_tablename} "
                                   "(ID INTEGER PRIMARY KEY,"
                                   "Content BLOB ,"
                                   " Key TEXT )")
                    self.tablename = optional_tablename
                return 1

            except sqlite3.Error as e:
                return (0, e)

    def insert(self, content, key, optional_table_name=None):
        if optional_table_name is None:
            try:
                with self.conn:
                    self.c.execute(f"INSERT INTO {self.tablename} (Content ,Key) VALUES (? , ?) ", (content, key))

                return 11
            except sqlite3.Error as e:
                return (0.0, e)

        else:
            try:
                with self.conn:
                    self.c.execute(f"INSERT INTO {optional_table_name} (Content ,Key) VALUES (? , ?) ",
                                   (content, key))
                return 1
            except sqlite3.Error as e:
                return (0, e)

    def update(self, column_name: str, new_column_val: str, ID: int, optional_table_name=None):
        if optional_table_name is None:
            try:
                with self.conn:
                    self.c.execute((f'UPDATE {self.tablename} SET ? = ? WHERE ID = ? '),
                                   (column_name, new_column_val, ID))
                    return 11

            except sqlite3.Error as e:
                return (0.0, e)

        else:
            try:
                with self.conn:
                    self.c.execute((f'UPDATE {optional_table_name} SET ? = ? WHERE ID = ? '),
                                   (column_name, new_column_val, ID))
                    return 1

            except sqlite3.Error as e:
                return (0, e)

    def content(self, optional_tablename=None):
        if optional_tablename is None:
            try:
                with self.conn:
                    self.c.execute(f'SELECT * FROM {self.tablename} ')
                    for row in self.c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return (0.0, e)

        else:
            try:
                with self.conn:
                    self.c.execute(f'SELECT * FROM {optional_tablename} ')
                    for row in self.c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return (0, e)

    def show_contents(self, *optional_tablenames):
        if optional_tablenames:
            try:
                for arg in optional_tablenames:
                    with self.conn:
                        self.c.execute(f'SELECT * FROM {arg} ')
                        for row in self.c.fetchall():
                            yield {arg: row}

            except sqlite3.Error as e:
                return (0.0, e)

        else:
            try:
                with self.conn:
                    self.c.execute(f'SELECT * FROM {self.tablename} ')
                    for row in self.c.fetchall():
                        yield {self.tablename: row}

            except sqlite3.Error as e:
                return (0, e)

    def show_tables(self) -> tuple:
        try:
            with self.conn:
                self.c.execute("SELECT name FROM sqlite_master WHERE type= 'table' ")
                for row in self.c.fetchall():
                    yield row

        except sqlite3.Error as e:
            return (0, e)

    def dropall(self):
        try:
            with self.conn:
                self.c.execute("SELECT name FROM sqlite_master WHERE type= 'table' ")
                for table in self.c.fetchall():
                    self.c.execute(f'DROP TABLE {table[0]}')
                return 1

        except sqlite3.Error as e:
            return (0, e)

    def drop_table(self, *table_names):
        if table_names:
            try:
                for arg in table_names:
                    with self.conn:
                        self.c.execute(f"DROP TABLE {arg}")
                return 1
            except sqlite3.Error as e:
                return (0.0, e)

        else:
            try:
                with self.conn:
                    self.c.execute(f'DROP TABLE {self.tablename}')
                    return 1

            except sqlite3.Error as e:
                return (0, e)

    def drop_content(self, ID, optional_table_name=None):
        if optional_table_name is None:
            try:
                with self.conn:
                    self.c.execute(f'DELETE FROM {self.tablename} WHERE ID = {ID}')
                return 11

            except sqlite3.Error as e:
                return (0.0, e)

        else:
            try:
                with self.conn:
                    self.c.execute(f'DELETE FROM {optional_table_name} WHERE ID = {ID}')
                return 1

            except sqlite3.Error as e:
                return (0, e)

if __name__ == '__main__':
    conn = Database('test.db')
    conn.addtable()
    key = '#5482A'
    conn.insert('some encrypted content of bytes or strings',key)
    for e in conn.show_tables():
        print(e)
    print(conn.size)
    query1 = 'SELECT COUNT(*) AS cc ,content FROM DoesntExist WHERE key = "#5482A" ORDER BY cc DESC '
    print(conn.query(query1))
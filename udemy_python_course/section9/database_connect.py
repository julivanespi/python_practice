import sqlite3


def main():
    database = sqlite3.connect("information.db")
    database.row_factory = sqlite3.Row
    database.execute("create table Admin(Name text, Age int)")
    database.commit()


if __name__ == "__main__":
    pass

    
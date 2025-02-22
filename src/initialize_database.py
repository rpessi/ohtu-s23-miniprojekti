from database_connection import get_db_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS book_references
    """)

    cursor.execute("""
        DROP TABLE IF EXISTS article_references
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS reference_tags
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS tag_relations
    """)

    connection.commit()


def create_tables(connection):
    """
    Here we create the tables for all the supported reference types
    """

    cursor = connection.cursor()

    # create the book_references table
    cursor.execute("""
        CREATE TABLE book_references (
            ref_key TEXT PRIMARY KEY,
            author TEXT,
            title TEXT,
            year INTEGER,
            publisher TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE article_references (
            ref_key TEXT PRIMARY KEY,
            author TEXT,
            title TEXT,
            journal TEXT,
            year INTEGER,
            volume INTEGER,
            pages TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE reference_tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE tag_relations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_id INT,
            ref_key TEXT
        )
    """)

    connection.commit()


def initialize_database():
    connection = get_db_connection()

    drop_tables(connection)
    create_tables(connection)

from database.db import connect


def initialize():

    conn = connect()
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module TEXT NOT NULL,
            action TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)


    cursor.execute(
        "PRAGMA table_info(history)"
    )


    columns = [
        row[1]
        for row in cursor.fetchall()
    ]


    if "status" not in columns:

        cursor.execute(
            """
            ALTER TABLE history
            ADD COLUMN status TEXT DEFAULT 'UNKNOWN'
            """
        )


    if "created_at" not in columns:

        cursor.execute(
            """
            ALTER TABLE history
            ADD COLUMN created_at
            TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            """
        )


    conn.commit()
    conn.close()


    print(
        "[✓] Database migration completed."
    )


if __name__ == "__main__":
    initialize()

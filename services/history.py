from database.db import connect


def add_history(module, action, status):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(module, action, status)
        VALUES (?, ?, ?)
        """,
        (module, action, status)
    )

    conn.commit()
    conn.close()


def get_history(limit=20):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, module, action, status, created_at
        FROM history
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

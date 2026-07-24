import sys
import os

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from database.db import connect
from services.history import add_history, get_history


def main():

    print("=" * 60)
    print("BlackShield Database Test")
    print("=" * 60)


    try:

        conn = connect()

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            """
        )


        tables = cursor.fetchall()

        conn.close()


        print("\nDatabase Connection: OK")


        if ("history",) in tables:

            print(
                "History Table: OK"
            )

        else:

            print(
                "History Table: Missing"
            )

            return



        print(
            "\nTesting write..."
        )


        add_history(
            "TEST",
            "Database Check",
            "SUCCESS"
        )


        print(
            "Write: OK"
        )


        print(
            "\nTesting read..."
        )


        data = get_history(5)


        if data:

            print(
                "Read: OK"
            )


            print("\nLatest Entry:")

            print(data[0])


        else:

            print(
                "Read Failed"
            )


    except Exception as e:

        print(
            "\nDatabase Error:"
        )

        print(e)



    print("\n" + "=" * 60)



if __name__ == "__main__":
    main()

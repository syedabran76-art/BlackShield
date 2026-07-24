import os
import json

from utils.helpers import separator


NAME = "Reports"
VERSION = "1.0.0"
DESCRIPTION = "Report management system."
AUTHOR = "BlackShield Team"


REPORT_DIR = "reports"


def list_reports():

    separator()

    print("BlackShield Reports")

    separator()


    if not os.path.exists(REPORT_DIR):

        print("Reports directory does not exist.")

        input("\nPress Enter to continue...")

        return



    reports = os.listdir(REPORT_DIR)


    if not reports:

        print("No reports available.")

    else:

        for index, report in enumerate(reports, 1):

            print(
                f"{index}. {report}"
            )


        choice = input(
            "\nOpen report number (0 cancel): "
        )


        if choice.isdigit():

            number = int(choice)


            if number > 0 and number <= len(reports):

                path = os.path.join(
                    REPORT_DIR,
                    reports[number - 1]
                )


                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as file:

                        data = file.read()

                        print("\n")
                        print(data)


                except Exception as e:

                    print(
                        f"Error: {e}"
                    )


    separator()

    input(
        "\nPress Enter to continue..."
    )



def register(menu):

    menu.register(
        "View Reports",
        list_reports
    )

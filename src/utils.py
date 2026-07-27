import pandas as pd


def create_dataframe(hours, attendance, previous, sleep):

    df = pd.DataFrame({

        "Feature": [
            "Study Hours",
            "Attendance",
            "Previous Marks",
            "Sleep Hours"
        ],

        "Value": [
            hours,
            attendance,
            previous,
            sleep
        ]

    })

    return df
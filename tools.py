from config import STUDENT_DATA


def get_student_data():
    return STUDENT_DATA


def get_total_expenses():
    data = STUDENT_DATA

    total = (
        data["food"]
        + data["travel"]
        + data["study_materials"]
        + data["other"]
    )

    return total


def get_balance():
    data = STUDENT_DATA

    total = get_total_expenses()

    return data["monthly_allowance"] - total
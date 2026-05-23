import openpyxl


def get_test_data():

    workbook = openpyxl.load_workbook(
        "testdata/test_data.xlsx"
    )

    sheet = workbook.active

    data = {

        "condition_index": int(
            sheet["A2"].value
        ),

        "mobile": str(
            sheet["B2"].value
        ),

        "location": str(
            sheet["C2"].value
        )

    }

    return data
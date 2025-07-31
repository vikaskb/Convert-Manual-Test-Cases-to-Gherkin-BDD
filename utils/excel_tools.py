import pandas as pd


def read_excel_test_cases(excel_file, sheet_name='RegressionTests'):
    test_cases = []
    # Read the Excel file and return a DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')
    
    for index, row in df.iterrows():
        test_case = {
            "Test Case Name": row['TestName'],
            "Description": row['Description']
        }
        test_cases.append(test_case)
    return test_cases

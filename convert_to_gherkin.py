from utils.excel_tools import *
from utils.json_tools import *
from utils.write_file import *
from utils.ai_tools import *
from utils.gherkin_tools import *

if __name__ == "__main__":
    input_excel = 'data/regression_tests.xlsx'
    input_json = 'data/regression_test_cases.json'

    # convert_regression_tests_to_gherkin(input_excel)
    excel_test_cases = read_excel_test_cases(input_excel)
    json_test_cases = read_json_test_cases(input_json)

    test_cases = excel_test_cases + json_test_cases

    for test_case in test_cases:
        print(f"Processing test case: {test_case['Test Case Name']}")
        response = get_gherkin_suggestions(test_case) # Using Open AI API to get Gherkin suggestions
        steps = extract_gherkin_steps(response) # Extracting Gherkin steps from the response
        
        generate_gherkin_feature(test_case['Test Case Name'], steps)

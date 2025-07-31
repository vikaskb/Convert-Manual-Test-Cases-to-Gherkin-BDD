import json

def read_json_test_cases(json_file):
    test_cases_list = []
    with open(json_file, 'r') as f:
        test_cases = json.load(f)
    
    for test_case in test_cases:
        test_case = {
            "Test Case Name": test_case['Test Case Id'],
            "Description": test_case
        }
        test_cases_list.append(test_case)
    return test_cases_list

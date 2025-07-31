
# Automate Regression Test Case Conversion to Gherkin

This project demonstrates how to automate the conversion of manual regression test cases into Gherkin-style BDD feature files using AI-powered automation.

## Project Structure

- **data/**: Contains sample data (Excel and JSON file) for regression test cases.
- **utils/**: Includes utility scripts for reading files, AI processing and writing feature files.
- **README.md**: Project documentation.

## Tools & Technologies

- **Python**: Programming language used for the automation script.
- **Pandas**: For reading and processing Excel files.
- **OpenAI (GPT)**: AI tool for generating Gherkin steps based on test case descriptions.
descriptions.
- **Gherkin Syntax**: BDD syntax for automated test case definition.

## How it Works

1. **Input**: The regression test cases are stored in an Excel file.
2. **Processing**:
   - **AI**: AI tools (OpenAI GPT) are used to generate Gherkin steps.
3. **Output**: The script generates feature files in the Gherkin syntax.

## Running the Project

1. Clone or download the repository.
2. Install the required Python libraries:
   ```
   pip install -r configs/requirements.txt
   ```
3. Add your OpenAI API key to the `configs/credentials.json` file.
4. Run the script:
   ```
   python convert_to_gherkin.py
   ```
   This will read the files in `data/`, convert the test cases to Gherkin syntax, and generate `.feature` files for each test case under `feature_files` directory with filename as test case name.


def generate_gherkin_feature(test_name, steps):
    # Generate Gherkin feature file
    feature_content = f"Feature: {test_name}\n\n"
    # feature_content += steps
    for step in steps:
        feature_content += f"{step['keyword']} {step['text']}\n"

    # Save to file
    with open(f"feature_files/{test_name}.feature", 'w') as file:
        file.write(feature_content)
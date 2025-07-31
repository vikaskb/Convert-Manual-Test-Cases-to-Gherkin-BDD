def extract_gherkin_steps(gherkin_output):
    # Define the Gherkin keywords you care about
    gherkin_keywords = ['Scenario','Given', 'When', 'Then', 'And', 'But']
    structured_steps = []
    current_keyword = None

    for line in gherkin_output.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        for keyword in gherkin_keywords:
            if stripped.startswith(keyword):
                step_text = stripped[len(keyword):].strip()
                # Track the main keyword for "And" and "But"
                # if keyword in ['And', 'But'] and current_keyword:
                #     used_keyword = current_keyword
                # else:
                #     used_keyword = keyword
                #     current_keyword = keyword
                # structured_steps.append({
                #     "keyword": used_keyword,
                #     "text": step_text
                # })
                structured_steps.append({
                    "keyword": keyword,
                    "text": step_text
                })
                break  # No need to check other keywords once matched

    return structured_steps
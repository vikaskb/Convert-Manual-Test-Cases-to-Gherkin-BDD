import openai
import json

def get_gherkin_suggestions(test_case_description):

    with open('configs/credentials.json', 'r') as f:
        creds = json.load(f)
        API_KEY = creds.get('openai', {}).get('api_key', '')
    if not API_KEY:
        raise ValueError("API key for OpenAI is not set in the credentials file.")
    
    client = openai.OpenAI(
        api_key=API_KEY
    )
    prompt = f"Convert the following test case description into Gherkin BDD steps:\n\n{test_case_description}\n\nGherkin Steps:"
    
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
        ]
    )

    gherkin_steps = response.choices[0].message.content
    return gherkin_steps

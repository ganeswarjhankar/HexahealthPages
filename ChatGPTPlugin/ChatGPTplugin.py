from flask import Flask,request
import openai
openai.api_key = 'GANESWARJHANKAR_OPENAI_API_KEY'
app = Flask(__name__)

@app.route('/fill-data', methods=['POST'])
def fill_data():
    user_input = request.form.get('input')  # User input from the website
    response = openai.Completion.create(
        engine='davinci-codex',  # Use the appropriate engine
        prompt=user_input,
        max_tokens=50  # Adjust the response length as needed
    )
    generated_text = response.choices[0].text.strip()

    # Perform actions with the generated text, such as filling a form field or displaying it on the website

    return generated_text


if __name__ == '__main__':
    app.run()


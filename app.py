import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "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"

# Define function to generate answer from OpenAI API
def generate_answer(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# Define Flask route for answering questions
@app.route('/answer', methods=['POST'])
def answer():
    # Get the question from the request body
    question = request.json['question']

    # Generate the answer using OpenAI API
    answer = generate_answer(question)

    # Return the answer as a JSON object
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)

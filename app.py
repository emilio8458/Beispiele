from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# API-Schlüssel für OpenAI (ersetze dies mit deinem eigenen Schlüssel)
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        answer = response['choices'][0]['message']['content'].strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

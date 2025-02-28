from flask import Flask, render_template, request

app = Flask(__name__)

# Simple chatbot logic
responses = {
    "how do i set up new source in segment": 'Refer this link for more: <a href="https://segment.com/docs/?ref=nav" target="_blank">Segment Documentation</a>',
    "how can i create a user profile in mparticle": 'Refer this link for more: <a href="https://docs.mparticle.com/" target="_blank">mParticle Documentation</a>',
    "how do i build an audience segment in lytics": 'Refer this link for more: <a href="https://docs.lytics.com/" target="_blank">Lytics Documentation</a>',
    "how can i integrate my data with zeotap": 'Refer this link for more: <a href="https://docs.zeotap.com/home/en-us/" target="_blank">Zeotap Documentation</a>',
    "default": "I'm not sure how to answer that. Can you rephrase?"
}

def get_response(user_input):
    return responses.get(user_input.lower(), responses["default"])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return response

if __name__ == '__main__':
    app.run(debug=True)

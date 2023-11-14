from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Assuming your HTML file is in a templates folder

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Retrieve form data from the request
        data = request.get_json()

        # Perform any processing, e.g., interact with your language model
        # For now, just echo the received data
        result = {
            'message': 'Program generated successfully!',
            'data': data
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

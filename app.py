from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()

    if not data or 'input' not in data:
        return jsonify({'error': 'Missing "input" in request body'}), 400

    input_value = data['input']

    if not isinstance(input_value, str):
        return jsonify({'error': '"input" must be a string'}), 400

    reversed_string = input_value[::-1]

    return jsonify({'reversed': reversed_string}), 200

if __name__ == '__main__':
    app.run(debug=True)

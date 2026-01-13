from flask import Flask, render_template, request
from analyzer import analyze_numbers

app = Flask(__name__)

@app.route('/')
def index():
    a = "Thitima"
    return render_template("index.html", name=a)

@app.route('/analyze', methods=['GET', 'POST']) 
def analyze():
    request_data = request.form.get('numbers', '')
    if request_data:
        try:
            # Replace commas with spaces, split on whitespace, ignore empty tokens
            cleaned = request_data.replace(',', ' ')
            tokens = cleaned.split()
            numbers = []
            for token in tokens:
                # convert each token to float (will raise ValueError if invalid)
                numbers.append(float(token))
        except ValueError:
            error_message = "Invalid input. Please enter a list of numbers separated by commas or whitespace."
            return render_template("index.html", error=error_message)
        
        results = analyze_numbers(numbers)
        return render_template("results.html", numbers=numbers, results=results)            
    return render_template("index.html", error="No input provided. Please enter some numbers.")

if __name__ == '__main__':
    app.run(debug=True)


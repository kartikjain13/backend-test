from flask import Flask , jsonify, render_template
import os

app = Flask(__name__)

HISTORY_FILE = "history.txt"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        for entry in history:
            file.write(entry + "\n")


operations_history = load_history()

@app.route('/calculate/<path:operation>')
def calculate(operation):
    operation = operation.replace('plus', '+').replace('minus', '-').replace('into', '*').replace('divide', '/')

    try:
        result = eval(operation)
        operations_history.append(f"{operation}={result}")

        
        if len(operations_history) > 20:
            operations_history.pop(0)

        save_history(operations_history)

        return jsonify({"result": result, "history": operations_history})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/history')
def history():
    history_results = []
    for entry in operations_history:
        equation, result = entry.split('=') if '=' in entry else (entry, '')
        history_results.append({"question": equation, "answer": result})

    return render_template('history.html', history=history_results)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
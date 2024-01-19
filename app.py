from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/result", methods=['GET', 'POST'])
def hi():
    output = None
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operation = request.form['operation']
        print("Received form data - num1:", num1, "num2:", num2, "operation:", operation)
        output = cal(num1, num2, operation)
        print("Calculated output:", output)
    return render_template('result.html', operation=operation, output=output)

def cal(num1, num2, operation):
    if operation == 'addition':
        return num1 + num2
    elif operation == 'subtraction':
        return num1 - num2
    elif operation == 'multiplication':
        return num1 * num2
    elif operation == 'division':
        return num1 / num2

if __name__ == '__main__':
    app.run()
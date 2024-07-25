from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.datetime.now()
    return render_template('index.html', current_time=current_time)

@app.route('/reset', methods=['POST'])
def reset():
    # Lógica para resetar os campos e a pirâmide
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

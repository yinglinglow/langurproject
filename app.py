from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/time/')
def time():
    return render_template('Langurs_time.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/langur/')
def langur():
    return render_template('Langurs.html')

@app.route('/quick/')
def quick():
    return render_template('Langurs_quick.html')

@app.route('/time/')
def time():
    return render_template('Langurs_time.html')

@app.route('/sighting/')
def sighting():
    return render_template('Langurs_action_1st Sighting.html')

@app.route('/defecate/')
def defecate():
    return render_template('Langurs_action_Defecate.html')

@app.route('/feed/')
def feed():
    return render_template('Langurs_action_Feed.html')

@app.route('/mate/')
def mate():
    return render_template('Langurs_action_Mate.html')

@app.route('/play/')
def play():
    return render_template('Langurs_action_Play.html')

@app.route('/rest/')
def rest():
    return render_template('Langurs_action_Rest.html')

@app.route('/travel/')
def travel():
    return render_template('Langurs_action_Travel.html')

@app.route('/vocalise/')
def vocalise():
    return render_template('Langurs_action_Vocalise.html')

if __name__ == '__main__':
    app.run(debug=True)
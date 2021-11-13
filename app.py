from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def splash():
    return render_template('index.html', title='Log in')

@app.route('/home')
def home():
    return "hello there"

if __name__=='__main__':
    app.run(debug=True)